var name = document.getElementById("name");
var password = document.getElementById("password");
var form = document.getElementById("form");
var errorElement = document.getElementById("error");
var ConfirmPassword = document.getElementById("confirm-password");

form.addEventListener("submit", (e) => {
  let messages = [];

  if (password.value.length <= 6) {
    messages.push("Password must be longer than 6 characters");
  }

  if (password.value.length >= 20) {
    messages.push("Password must be less than 20 characters");
  }

  if (password.value === "password") {
    messages.push("Password cannot be password");
  }
  if (password.value.length != 0) {
    if (password.value != ConfirmPassword.value) {
        messages.push("Passwords must match");
    }
  }
  if (messages.length > 0) {
    e.preventDefault();
    errorElement.innerText = messages.join(", ");
  }
  
 
});
