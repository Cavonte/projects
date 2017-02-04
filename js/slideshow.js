var myIndex = -1;
var clicking=false;
//showDivs(0);

function plusDivs(n) {
    showDivs(myIndex += n);
    clicking=true;
    console.log("clicking");
    setTimeout(reset, 15000);    
}

function reset(){
    clicking=false;
}

function showDivs(n) {
    var x = document.getElementsByClassName("mySlides w3-animate-zoom");
    //console.log(x.length);
    console.log("asked" + n);
   if (n >= x.length) {myIndex = 0}  //reach the end.
    if (n < 0) {myIndex = x.length-1} ; //someone trying to back, reset to the end of the slide.
    for (var i = 0; i < x.length; i++) {
        x[i].style.display = "none"; 
    }
    console.log("passing" +myIndex);
    x[myIndex].style.display = "block"; 
}

var carousel= function() {  
    //while no one has cliked, change the current picture. and call the method in the next 3 seconds.
    if(!clicking) { 
    console.log("Carousel");
    myIndex+=1;
    showDivs(myIndex);
    }
   setTimeout(carousel,6000); //show the next image.
}      

