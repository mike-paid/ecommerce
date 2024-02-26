from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import items,cart
from django.contrib import messages
from .models import user
from django.contrib.auth import authenticate, logout, login as authlogin

# Create your views here.

def signup(request):
    if request.method == "POST":
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        photo = request.FILES.get("photo")
        re_password = request.POST['re_password']
        phone = request.POST['phone']
        password= request.POST['password']


        print(request.POST)

        if password != re_password:
            
            messages.warning(request, "passords must be identical")

        
        elif email =="" or password =="" or phone =="" or firstname =="" or lastname =="":
            
            messages.warning(request, "fields can not be left empty")

        
        elif user.objects.filter(email = email).exists():
            messages.warning(request, "email already exists")
        
        else:
        
            newuser = user.objects.create_user(
                email = email,
                first_name = firstname,
                last_name = lastname,
                photo = photo,
                password = password,
                phone = phone,
            )

            return redirect("/login")
    return render(request, "signup.html")


def login(request):


    if request.method == "POST":
        email = request.POST['email']
        password= request.POST['password']
        
        user = authenticate(email = email, password = password)

        if user == None:
            messages.warning(request, "invalid credentials")
        else:
            authlogin(request, user)
            return redirect("/")
        


    return render(request, "login.html")

def home(request):
    allproducts = items.objects.all()

    if request.user.is_authenticated:

        cartData = cart.objects.filter(user = request.user).all()
    else:
        cartData = []

    if request.method == "POST":
        cart_id = request.POST["product_id"]
        cart_price = request.POST["product_price"]
        cart_title = request.POST["product_title"]

        theproduct = items.objects.filter(id = cart_id).first()
        
        
        if request.user.is_authenticated:
            data = cart.objects.filter(item_id = cart_id, user= request.user).first()
            if data == None:
                cart.objects.create(
                    qty= 1,
                    price = cart_price,
                    title = cart_title,
                    user = request.user,
                    item_id = theproduct,
                    
                )
                return redirect("/")
            else:
                data.Prices = float(data.price) + float(cart_price)
                data.qty = data.qty + 1
                data.save()
                return redirect("/")



        else:
            return redirect("/login")
        
    data ={
        "products": allproducts, "cartTotal": len(cartData)
    }

    return render(request, "index.html", context=data)



def cartPage(request):



  if request.user.is_authenticated:
    productInCart = cart.objects.filter(user_id = request.user).all()
    user = request.user
  else:
    productInCart = []
    user = None

    
  total = 0 
  for each in  productInCart:
    total+=each.price
  

  if request.method == "POST":
    if request.POST.get("add"):
        cart_id = request.POST['add']
        theproduct = cart.objects.filter(id = cart_id).first()

        theproduct.qty = theproduct.qty + 1
        theproduct.price = float(theproduct.price) + float(theproduct.item_id.price)
        theproduct.save()
        return redirect("/cart")

  
    elif request.POST.get("minus"):
        cart_id = request.POST['minus']
        theproduct = cart.objects.filter(id = cart_id).first()
        theproduct.qty = theproduct.qty - 1

        if theproduct.qty < 1:
            theproduct.delete()
            return redirect("/cart")
        else:
            theproduct.price = float(theproduct.price) - float(theproduct.item_id.price)
            theproduct.save()
            return redirect("/cart")
    
  

  data = {
    "cartTotal": len(productInCart),
    "allcarts": productInCart,
    "totalAmount": total,
    "auth": user
  }

  return render(request, "cart.html", context=data)

def logoutUser(request):
    logout(request)
    return redirect("/login")