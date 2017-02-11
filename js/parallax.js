var select=true;

var wScrollTemp=0;

$(window).scroll(function(){

select=false;
console.log("select to false");

var wScroll= $(this).scrollTop();//variave which tracks how far we are
var minus=500;	
var delay= 700;
//from the top

	if ( Math.abs(wScroll-wScrollTemp)> 200 ) {	
	if (wScroll > $('#wall_1').offset().top && wScroll < $('#content_1').offset().top || wScroll ==0 ) {
			// console.log("current section is : wall_1" );
		//$('#navHome').addClass('is-active');
	}
	else {
		// $('#navHome').removeClass('is-active');
	}
	//when you reach half of the previous wall
	if (wScroll > ($('#content_1').offset().top-minus) && wScroll < $('#wall_2').offset().top) {
		// console.log("current section is : content_1" );
		// $('#navSkills').addClass('is-active');// hightlight the home element when the detected section is home
		$('.content_1-transition').each(function(i){
			setTimeout(function(){
			$('.content_1-transition').eq(i).addClass('is-showing');
			incre=i;
		}, (delay * (Math.exp(i * 0.14))) - delay);			
		});

		$('.contentTransitionRight').each(function(j){
			setTimeout(function(){
			$('.contentTransitionRight').eq(j).addClass('is-showing-right');
		}, (delay * (Math.exp((j+5) * 0.14))) - delay);			
		});

	} else {
		// $('#navSkills').removeClass('is-active');// remove the highlight
		$('.content_1-transition').each(function(i){
			setTimeout(function(){
			$('.content_1-transition').eq(i).removeClass('is-showing');
		}, (delay * (Math.exp(i * 0.14))) - delay);			
		});

		$('.contentTransitionRight').each(function(j){
			setTimeout(function(){
			$('.contentTransitionRight').eq(j).removeClass('is-showing-right');
		}, (delay * (Math.exp((j+5) * 0.14))) - delay);			
		});
	}

	if (wScroll > ($('#wall_2').offset().top-300) && wScroll < $('#content_2').offset().top ) {
			console.log("current section is : wall_2" );
		// $('#navExperience').addClass('is-active');// hightlight the home element when the detected section is home
	$('.content_2-transition').each(function(i){
			setTimeout(function(){
			$('.content_2-transition').eq(i).addClass('is-showing');
		}, (delay * (Math.exp(i * 0.14))) - delay);			
		});
		
	} else {
		// $('#navExperience').removeClass('is-active');
		$('.content_2-transition').each(function(i){
			setTimeout(function(){
			$('.content_2-transition').eq(i).removeClass('is-showing');
		}, (delay * (Math.exp(i * 0.14))) - delay);			
		});
	}

	if (wScroll > ($('#content_2').offset().top-minus) && wScroll < $('#wall_3').offset().top) {
		// console.log("current section is : content_2" );
		// $('#navProjects').addClass('is-active');
		$('.content_3-transition').each(function(i){
			setTimeout(function(){
			$('.content_3-transition').eq(i).addClass('is-showing');
		}, (delay * (Math.exp(i * 0.14))) - delay);			
		});
	} else {
		// $('#navProjects').removeClass('is-active');
		$('.content_3-transition').removeClass('is-showing');
	}

	if (wScroll > ($('#wall_3').offset().top-500) && wScroll < $('#content_3').offset().top ) {
		// console.log("current section is : wall_3" );
		// $('#navGallery').addClass('is-active');
	}else{
		// $('#navGallery').removeClass('is-active');
	}

	if (wScroll > $('#content_3').offset().top && wScroll < $('#wall_4').offset().top) {
		// console.log("current section is : content_3" );
		// $('#navGallery').addClass('is-active');
	}else{
		// $('#navGallery').removeClass('is-active');
	}
		// section dedicated to update the navigation bar on the side.
		if (wScroll > $('#wall_1').offset().top && wScroll < $('#content_1').offset().top || wScroll ==0 ) {
			$('#navHome').addClass('is-active');
		}
		else {
			$('#navHome').removeClass('is-active');
		}
		//when you reach half of the previous wall
		if (wScroll > ($('#content_1').offset().top) && wScroll < $('#wall_2').offset().top) {
			$('#navSkills').addClass('is-active');// hightlight the home element when the detected section is home
		} else {
			$('#navSkills').removeClass('is-active');// remove the highlight
		}

		if (wScroll > ($('#wall_2').offset().top) && wScroll < $('#content_2').offset().top ) {
			$('#navExperience').addClass('is-active');// hightlight the home element when the detected section is home
		} else {
			$('#navExperience').removeClass('is-active');
		}

		if (wScroll > ($('#content_2').offset().top) && wScroll < $('#wall_3').offset().top) {
			// console.log("current section is : content_2" );
			$('#navProjects').addClass('is-active');
		} else {
			$('#navProjects').removeClass('is-active');
			$('.content_3-transition').removeClass('is-showing');
		}

		if (wScroll > ($('#wall_3').offset().top) && wScroll < $('#content_3').offset().top ) {
			$('#navGallery').addClass('is-active');
		}else{
			$('#navGallery').removeClass('is-active');
		}

wScrollTemp=wScroll;
	}	

	
//console.log(wScroll);

});

function selectNav(nav) {
setTimeout(function(){$(nav).addClass('is-active');} , 200);	
}
