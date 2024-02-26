

AOS.init()

document.getElementById("pay-btn").onclick = function () {
    let amount = document.getElementById("payamt").innerText
    let email = document.getElementById("email").innerText
    
    
  let handler = PaystackPop.setup({
    key: 'pk_test_3ee4abeb1cda9a6af8476325fe622b544e7e6283', // Replace with your public key
    email: email,
    amount: amount * 100,
    ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      let message = 'Payment complete! Reference: ' + response.reference;
      alert(message);
    }
  });

  handler.openIframe();
}



