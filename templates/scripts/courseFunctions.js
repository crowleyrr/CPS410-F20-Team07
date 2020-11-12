/*When the user clicks Search, display the selected data*/ 
var displayAddData = function() {
	
  var courseID = document.getElementById("identifier").value;
  var courseNum = document.getElementById("number").value;

  if(courseNum <= 999 && courseNum >= 0){	
  document.getElementById("addoutput").innerHTML = "Course to add to Student Object: " 
  + courseID 
  + " " + courseNum;
  }
  
  else{
	document.getElementById("addoutput").innerHTML = "Invalid Course Number, must be between 000-999";
  }
}
 
var displayRemoveData = function() {
  var course = document.getElementById("courses").value;

  document.getElementById("removeoutput").innerHTML = "Course to remove from Student Object: " 
  + course;
}

window.onload = function(){
  document.getElementById("add").onclick = displayAddData;
  document.getElementById("remove").onclick = displayRemoveData;
  
}