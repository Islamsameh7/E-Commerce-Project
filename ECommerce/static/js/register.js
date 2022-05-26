var name = document.getElementById('name')
var password = document.getElementById('password')
var form = document.getElementById('form')
var errorElement = document.getElementById('error')

form.addEventListener('submit', (e) => {
  let messages = []


  if (password.value.length <= 6) {
    messages.push('Password must be longer than 6 characters')
  }

  if (password.value.length >= 20) {
    messages.push('Password must be less than 20 characters')
  }

  if (password.value === 'password') {
    messages.push('Password cannot be password')
  }

  if (messages.length > 0) {
    e.preventDefault()
    errorElement.innerText = messages.join(', ')
  }
  var ConfirmPassword = document.getElementById("Confirm-password").value;
  console.log(password.value,ConfirmPassword);

  let message = document.getElementById("message");

  if(password.value.length !=0){
      if(password.value != ConfirmPassword){
          message.textContent ="password doesn't match";
      }
  }
})

