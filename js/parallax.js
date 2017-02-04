//function parallax(){
      //var prlx_lyr_1 = document.getElementById('navigation');
      //prlx_lyr_1.style.top = -(window.pageYOffset / 8)+'px';
      //}
      //window.addEventListener("scroll", parallax, false);


$(window).scroll(function(){

var wScroll= $(this).scrollTop();	//variave which tracks how far we are
//from the top

	$('#bar').css({
		//'transform' : 'translate('+ wScroll*2 +'%,'+ wScroll*100 +'%)'
	});

	if (wScroll > $('#wall_1').offset().top && wScroll < $('#content_1').offset().top ) {
			console.log("current section is : wall_1" );


	}
	//when you reach half of the previous wall
	if (wScroll > ($('#content_1').offset().top-500) && wScroll < $('#wall_2').offset().top) {
		//console.log("current section is : content_1" );
		$('.content_1-transition').each(function(){
			$('.content_1-transition').addClass('is-showing');
		});
		
	} else {
		$('.content_1-transition').each(function(){
			$('.content_1-transition').removeClass('is-showing');
		});
	}

	if (wScroll > ($('#wall_2').offset().top-500) && wScroll < $('#content_2').offset().top ) {
			console.log("current section is : wall_2" );
	$('.content_2-transition').each(function(){
			$('.content_2-transition').addClass('is-showing');
		});
		
	} else {
		$('.content_2-transition').each(function(){
			$('.content_2-transition').removeClass('is-showing');
		});
	}

	if (wScroll > $('#content_2').offset().top && wScroll < $('#wall_3').offset().top) {
		console.log("current section is : content_2" );
	}

	if (wScroll > $('#wall_3').offset().top && wScroll < $('#content_3').offset().top ) {
		console.log("current section is : wall_3" );
	}

	if (wScroll > $('#content_3').offset().top && wScroll < $('#wall_4').offset().top) {
		console.log("current section is : content_3" );
	}

	if (wScroll > $('#wall_4').offset().top) {
		console.log("current section is : wall_4" );
	}	

	
//console.log(wScroll);

});