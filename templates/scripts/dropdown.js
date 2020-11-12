/*When the user clicks Search, display the selected data*/ 
var displayData = function() {
  var course = document.getElementById("courses").value;
  var date = document.getElementById("dates").value;
  var time = document.getElementById("times").value;
  document.getElementById("output").innerHTML = "Course selected: " + course 
  + "<br>" + "Date selected: " + date
  + "<br>" + "Time selected: " + time;
}

window.onload = function(){
  document.getElementById("search").onclick = displayData;
}