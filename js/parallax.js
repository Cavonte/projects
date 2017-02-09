//function parallax(){
      //var prlx_lyr_1 = document.getElementById('navigation');
      //prlx_lyr_1.style.top = -(window.pageYOffset / 8)+'px';
      //}
      //window.addEventListener("scroll", parallax, false);


$(window).scroll(function(){

var wScroll= $(this).scrollTop();//variave which tracks how far we are
var minus=500;	
//from the top
	
	if (wScroll > $('#wall_1').offset().top && wScroll < $('#content_1').offset().top || wScroll ==0 ) {
			console.log("current section is : wall_1" );
		$('#navHome').addClass('isActive');
	}
	else {
		$('#navHome').removeClass('isActive');
	}
	//when you reach half of the previous wall
	if (wScroll > ($('#content_1').offset().top-minus) && wScroll < $('#wall_2').offset().top) {
		console.log("current section is : content_1" );
		$('#navSkills').addClass('isActive');// hightlight the home element when the detected section is home
		$('.content_1-transition').each(function(i){
			setTimeout(function(){
			$('.content_1-transition').eq(i).addClass('is-showing');
			incre=i;
		}, (700 * (Math.exp(i * 0.14))) - 700);			
		});

		$('.contentTransitionRight').each(function(j){
			setTimeout(function(){
			$('.contentTransitionRight').eq(j).addClass('is-showing-right');
		}, (700 * (Math.exp((j+5) * 0.14))) - 700);			
		});

	} else {
		$('#navSkills').removeClass('isActive');// remove the highlight
		$('.content_1-transition').each(function(i){
			setTimeout(function(){
			$('.content_1-transition').eq(i).removeClass('is-showing');
		}, (700 * (Math.exp(i * 0.14))) - 700);			
		});

		$('.contentTransitionRight').each(function(j){
			setTimeout(function(){
			$('.contentTransitionRight').eq(j).removeClass('is-showing-right');
		}, (700 * (Math.exp((j+5) * 0.14))) - 700);			
		});
	}

	if (wScroll > ($('#wall_2').offset().top-minus) && wScroll < $('#content_2').offset().top ) {
			console.log("current section is : wall_2" );
		$('#navExperience').addClass('isActive');// hightlight the home element when the detected section is home
	$('.content_2-transition').each(function(i){
			setTimeout(function(){
			$('.content_2-transition').eq(i).addClass('is-showing');
		}, (700 * (Math.exp(i * 0.14))) - 700);			
		});
		
	} else {
		$('#navExperience').removeClass('isActive');
		$('.content_2-transition').each(function(i){
			setTimeout(function(){
			$('.content_2-transition').eq(i).removeClass('is-showing');
		}, (700 * (Math.exp(i * 0.14))) - 700);			
		});
	}

	if (wScroll > ($('#content_2').offset().top-minus) && wScroll < $('#wall_3').offset().top) {
		// console.log("current section is : content_2" );
		$('#navProjects').addClass('isActive');
		$('.content_3-transition').each(function(i){
			setTimeout(function(){
			$('.content_3-transition').eq(i).addClass('is-showing');
		}, (700 * (Math.exp(i * 0.14))) - 700);			
		});
	} else {
		$('#navProjects').removeClass('isActive');
		$('.content_3-transition').removeClass('is-showing');
	}

	if (wScroll > $('#wall_3').offset().top && wScroll < $('#content_3').offset().top ) {
		// console.log("current section is : wall_3" );
		$('#navGallery').addClass('isActive');
	}else{
		$('#navGallery').removeClass('isActive');
	}

	if (wScroll > $('#content_3').offset().top && wScroll < $('#wall_4').offset().top) {
		// console.log("current section is : content_3" );
		// $('#navGallery').addClass('isActive');
	}else{
		// $('#navGallery').removeClass('isActive');
	}
	


	// if (wScroll > $('#wall_4').offset().top) {
	// 	console.log("current section is : wall_4" );
	// }	

	
//console.log(wScroll);

});