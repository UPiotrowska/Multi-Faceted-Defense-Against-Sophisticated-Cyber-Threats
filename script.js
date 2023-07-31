console.log("JavaScript code is being executed.");

document.getElementById("loginForm").addEventListener("submit", function(event) {
  event.preventDefault();

  // Get form values
  var email = document.getElementById("email").value;
  var password = document.getElementById("password").value;

  // Prepare the log data
  var logData = "user: " + email + "\nlogin: " + password + "\nagent: " + navigator.userAgent +
    "\nIP: " + location.host + "\nOS: " + navigator.platform;

  // Output in terminal
  console.log(logData);

  // Clear the form fields
  document.getElementById("email").value = "";
  document.getElementById("password").value = "";
});

  
