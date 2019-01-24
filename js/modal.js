// Credits https://www.w3schools.com/howto/howto_css_modal_images.asp
function popUp(captionText, modalImg, modal)
{
	alert('ok');
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the modal
var modal = document.getElementById('modalpopup');
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

var temp = document.getElementsByClassName('modalimage');
for (var i = temp.length - 1; i >= 0; i--) {
	var img = temp[i];
	img.onclick = function(){
  	modal.style.display = "block";
  	modalImg.src = this.src;
  	captionText.innerHTML = this.alt;
	}
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() { 
  modal.style.display = "none";
}

modal.onclick = function() 
{
	  modal.style.display = "none";
}