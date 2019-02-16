var select = true;
var wScrollTemp = 0;


$(window).scroll(function() {
	var wScroll = $(this).scrollTop();
	//variave which tracks how far we are
	var minus = 500;
	var delay = 700;
	setTimeout(function() {
		$('#content_3').removeClass('beforeloading');
	}, 2000);
	if (Math.abs(wScroll - wScrollTemp) > 10) {
		if (wScroll > ($('#content_1').offset().top - minus) && wScroll < $('#wall_2').offset().top) {
			$('.content_1-transition').each(function(i) {
				setTimeout(function() {
					$('.content_1-transition').eq(i).addClass('is-showing');
					incre = i;
				}, (delay * (Math.exp(i * 0.14))) - delay);
			});
			$('.contentTransitionRight').each(function(j) {
				setTimeout(function() {
					$('.contentTransitionRight').eq(j).addClass('is-showing-right');
				}, (delay * (Math.exp((j + 5) * 0.14))) - delay);
			});
		} else {
			// $('.content_1-transition').each(function(i){
			// 	setTimeout(function(){
			// 	$('.content_1-transition').eq(i).removeClass('is-showing');
			// }, (delay * (Math.exp(i * 0.14))) - delay);			
			// });
			// $('.contentTransitionRight').each(function(j){
			// 	setTimeout(function(){
			// 	$('.contentTransitionRight').eq(j).removeClass('is-showing-right');
			// }, (delay * (Math.exp((j+5) * 0.14))) - delay);			
			// });
		}
		if (wScroll > ($('#wall_2').offset().top - 300) && wScroll < $('#content_2').offset().top) {
			$('.content_2-transition').each(function(i) {
				setTimeout(function() {
					$('.content_2-transition').eq(i).addClass('is-showing');
				}, (delay * (Math.exp(i * 0.14))) - delay);
			});
		} else {
			// $('.content_2-transition').each(function(i){
			// 	setTimeout(function(){
			// 	$('.content_2-transition').eq(i).removeClass('is-showing');
			// }, (delay * (Math.exp(i * 0.14))) - delay);			
			// });
		}
		if (wScroll > ($('#content_2').offset().top - minus) && wScroll < $('#wall_3').offset().top) {
			$('.content_3-transition').each(function(i) {
				setTimeout(function() {
					$('.content_3-transition').eq(i).addClass('is-showing');
				}, (delay * (Math.exp(i * 0.14))) - delay);
			});
		} else {
			//$('.content_3-transition').removeClass('is-showing');
		}
		if (wScroll > ($('#wall_3').offset().top - 700)) {
			$('.content_4-transition').each(function(i) {
				setTimeout(function() {
					$('.content_4-transition').eq(i).addClass('is-showing');
				}, (delay * (Math.exp(i * 0.14))) - delay);
			});
		}

		$('.content_4-transition').each(function(i) {
			setTimeout(function() {
				$('.content_4-transition').eq(i).addClass('is-showing');
			}, 10000);
		});
		//if (wScroll > $('#content_3').offset().top && wScroll < $('#wall_4').offset().top) {
		// console.log("current section is : content_3" );
		//}else{
		//}
		// section dedicated to update the navigation bar on the side.
		if ( (wScroll >= $('#wall_1').offset().top - minus) && wScroll < $('#content_1').offset().top || wScroll == 0) {
			selectNav('#navHome');
		}
		if (wScroll >= ($('#content_1').offset().top -300) && wScroll < $('#wall_2').offset().top) {
			selectNav('#navSkills');
		}
		if (wScroll >= ($('#wall_2').offset().top - 300) && wScroll < $('#content_2').offset().top) {
			selectNav('#navExperience');
		}
		if (wScroll >= ($('#content_2').offset().top - minus) && wScroll < $('#wall_3').offset().top) {
			selectNav('#navProjects');
		}
		if (wScroll >= ($('#wall_3').offset().top - minus) && wScroll < $('#content_3').offset().top) {
			selectNav('#navGallery');
		}
		wScrollTemp = wScroll;
	}
});

function selectNav(nav) {
	setTimeout(function() {
		$('#navGallery').css("font-weight", "normal");
		$('#navGallery').css("font-size", "17px");
	}, 10);
	setTimeout(function() {
		$('#navProjects').css("font-weight", "normal");
		$('#navProjects').css("font-size", "17px");
	}, 10);
	setTimeout(function() {
		$('#navExperience').css("font-weight", "normal");
		$('#navExperience').css("font-size", "17px");
	}, 10);
	setTimeout(function() {
		$('#navSkills').css("font-weight", "normal");
		$('#navSkills').css("font-size", "17px");
	}, 10);
	setTimeout(function() {
		$('#navHome').css("font-weight", "normal");
		$('#navHome').css("font-size", "17px");
	}, 10);
	setTimeout(function() {
		$(nav).css("font-weight", "bold");
		$(nav).css("font-size", "22px");
	}, 10);
}