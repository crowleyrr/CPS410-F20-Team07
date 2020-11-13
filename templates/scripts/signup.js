/*When the user clicks Signup, display the information that they input*/ 
var displayData = function() {
	
  var fname = document.getElementById("fname").value;
  var lname = document.getElementById("lname").value;
  var email = document.getElementById("email").value;
  var university = document.getElementById("university").value;
  var type;
  if(document.getElementById("student").checked){
	  type="student";
  }
  else if(document.getElementById("tutor").checked){
	  type="tutor";
  }
  else{
	  alert("You must indicate whether you are a student or a tutor in order to sign up.");
  }
  
  var username = document.getElementById("username").value;
  var pass = "Super secret password!"

	alert("First name:" + fname
	 + "\nLast name: " + lname
	 + "\nEmail: " + email
	 + "\nUniversity: " + university
	 + "\nType: " + type
	 + "\nUsername: " + username
	 + "\nPassword: " + pass);
}


window.onload = function(){
  document.getElementById("signup").onclick = displayData;
}