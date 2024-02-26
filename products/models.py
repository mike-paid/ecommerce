from django.db import models
from authentication.models import user
# Create your models here.
class items(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="products")
    datecreated = models.DateTimeField(auto_now_add=True)


class cart(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    item_id = models.ForeignKey(items, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    user = models.ForeignKey(user, on_delete=models.CASCADE)