var eventIndex = 1;
showEvent(eventIndex);

function plusEvent(n) {
  showEvent(eventIndex += n);
}

function currentEvent(n) {
  showEvent(eventIndex = n);
}

function showEvent(n) {
  var i;
  var slides = document.getElementsByClassName("EventPart");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {eventIndex = 1}    
  if (n < 1) {eventIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[eventIndex-1].style.display = "block";  
  dots[eventIndex-1].className += " active";
}