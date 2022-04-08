var func = function()
{	

	$('.change_social_panel .change_link').click(function(){
		$('.change_social_panel .change_link').removeClass('active');
		$(this).addClass('active');
		var target = $(this).data('target');
		$('.social_panel').removeClass("active");
		//alert(target)
		$('#'+target).addClass("active");
	});
	$('.news_change').click(function(){
		var target = $(this).data('target');
		if(target=="news-main"){
			$('#news-main').css('display','block');
			$('#news-region').css('display','none');
			$('#country_link').addClass('active');
			$('#region_link').removeClass('active');
		}else{
			$('#news-main').css('display','none');
			$('#news-region').css('display','block');
			$('#country_link').removeClass('active');
			$('#region_link').addClass('active');	
		}
	});
	$('.events-toggle').click(function(){
		var current = $(this);
		var div = current.attr('dava-div-id');
		if(current.hasClass('act') === false){
			$('.events-toggle').removeClass('act');
			current.addClass('act');
			$('#events-list').toggle();
			$('#events-result').toggle();
		}
		return false;
	})

	$('.faq_more_show').click(function(){
		if($('.faq_more_text').css('display') == 'none'){
			$('.faq_del').toggle();
			$('.faq_more_text').slideDown(function(){
				$(this).css('display', 'inline');
			});
		}else{
			$('.faq_more_text').slideUp(function(){
				$('.faq_del').toggle();
			});			
		}
		
		return false;
	})

	
	$('.show_roo_list').click(function(){
		var link = $(this)
		var div_show = link.attr('data-div-show');
		var div_hide = link.attr('data-div-hide');
		$('.show_roo_list').removeClass('act');
		link.addClass('act');


		if($('.'+div_show).css('display') == 'none'){
			$('.'+div_hide).fadeOut("fast", function(){
				$('.'+div_show).fadeIn("fast")
			});
		}

		return false;
	})

	// переключение дивов на странице организация-структура
	$('.toggle-link').bind('click', function(){
		var current = $(this);
		var toggleGroup = current.data('toggle-group');
		var toggleElement = current.data('toggle-element');
		var activeClass = current.data('active-class');
		if($(toggleElement).css('display') == 'none'){
			$('.toggle-link').removeClass('act');
			$('.'+toggleGroup).hide();
			$(current).addClass(activeClass);
			$(toggleElement).show();
		}

		return false;
	})


	
		//slider
		
/*		$('#slider1').anythingSlider({autoPlay: true, hashTags : false, showMultiple : 3, changeBy : 1, theme : "default" });*/
		$('#slider-regions').anythingSlider({buildNavigation : false, showMultiple : 3,  changeBy : 1, resizeContents  : true, autoPlay: false, hashTags : false, theme : "default" });
		$('#slider-regions1').anythingSlider({buildNavigation : false, showMultiple : 3,  changeBy : 1, resizeContents  : true, autoPlay: false, hashTags : false, theme : "default", buildArrows :false });
		$('#slider2').anythingSlider({autoPlay: false, hashTags : false, theme : "gallery"});
		$('#slider3').anythingSlider({autoPlay: false, hashTags : false, theme : "gallery", resizeContents : false});

		$('.footer_slider .arrow.forward').click(function(){
			$('#slider-regions1').data('AnythingSlider').goForward();
		});
		$('.footer_slider .arrow.back').click(function(){
			$('#slider-regions1').data('AnythingSlider').goBack();
		});

		$(".slide-box a").click(function(){
      $(".slide-box div").slideToggle("slow")
    });
		
		$(".slide-box p").click(function(){
      $(".slide-box div").slideToggle("slow")
    });
		
		
		$('ul.tabs').delegate('li:not(.current)', 'click', function() {
			$(this).addClass('current').siblings().removeClass('current')
			.parents('div.gallery-box').find('div.gbox').hide().eq($(this).index()).fadeIn(0);
			return false;
		});
		
		
		//
		$('.viewform').click(function(event){
			$('.overlay').fadeIn('fast',function() {
				$('.boxform').animate({'top':$(window).scrollTop()+100},500);
			});
			event.preventDefault();
		});
		$('.boxclose').click(function(event){
			$('.boxform').animate({'top':'-800px'},500,function(){
				$('.overlay').fadeOut('fast');
			});
			event.preventDefault();
		});
  	
		
		//
		$(".accordion-box div.acc-title").eq(0).addClass("act");
		$(".accordion-box div.acc-drop").eq(0).show();

		$(".accordion-box div.acc-title").click(function(){
			$(this).next("div.acc-drop").slideToggle("slow")
			$(this).toggleClass("act");

			return false;
		});
		
	// поиск по членам реестра
	$('#member_lname').bind('keyup', function(){
		var name_value = $(this).val();
		if(name_value.length > 3){		
			$.ajax({
				type: "POST",
			 	url: "/ajax/members.php",
			 	data: { member_lname: name_value },		  
			 	beforeSend: function ( xhr ) {
			    	$('.member-table img').css('visibility', '');
				}
			}).done(function ( data ) {
				console.log(data.substr(0,5));
				if(data != ''){
					$('.member-table').replaceWith(data);
				}
			});
		}
	})

	// аннотация к книгам в структуре
	$('.book-list span').live('click', function(){
		var link = $(this);
		if(link.hasClass('act') === false){
			link.addClass('act').prev("p").toggle().parents('li').find('span a').replaceWith('<a href="#">Скрыть аннотацию</a>');
		}else{
			link.attr('class', '')
			link.removeClass('act').prev("p").toggle().parents('li').find('span a').replaceWith('<a href="#">Смотреть аннотацию</a>');
		}	
		return false;
	})	



	// добавление еще одного поля ФИО при оплате счетов
	$('.add-bill-field').click(function(){
		var clone = $('.bill-fio-field').last().clone().removeClass('bill-fio-field').addClass('new-fio-field').hide().insertBefore('.add-bill-field');
		$('.new-fio-field .in03').val('');
		$('.new-fio-field').show().removeClass('new-fio-field');
		return false;
	}) 

	$('.edit-bill').click(function(){
		$('.print-bill-form').append('<input type="hidden" value="1" name="edit_bill">').submit();
		return false;
	})


	$('.schet-b input').click(function(){
		var errors = false;
		var fioField = 0;
		$('.schet-form input[type="text"]').not('.bill-fio').each(function(){
			if($(this).val().trim() == ''){
				$(this).addClass('error-field');
				errors = true;
			}else{
				$(this).removeClass('error-field');
			}
		})

		$('.schet-form input.bill-fio').each(function(){
			if($(this).val().trim() != ''){
				fioField++;
			}
		})

		if(fioField <= 0){
			$('.schet-form input.bill-fio').first().addClass('error-field');
			errors = true;
		}else{
			$('.schet-form input.bill-fio').removeClass('error-field');
		}



		if(errors === true){
			return false;
		}
	})
};

$(func);

//Функции скрытия/показа карты/списка отделений
function show_map(link){
	link=$(link);
	$(".map-box .title a").removeClass("act");
	link.addClass("act");	
	$("#ro-listbox").fadeOut("fast", function(){
		$(".department-box").fadeIn("fast");
		$(".map-box .map").fadeIn("fast");
	});
}
function show_map_list(link){
	link=$(link);
	$(".map-box .title a").removeClass("act");
	link.addClass("act");
	$(".department-box").fadeOut("fast");
	$(".map-box .map").fadeOut("fast",function(){
		$("#ro-listbox").fadeIn("fast");
	});
}
function show_more_rubric(link){
	link=$(link);
	link.parent().hide();
	$(".news-box-menu li.hidden-rubric").parent().removeClass("all");
	$(".news-box-menu li.hidden-rubric").fadeIn();
	$(".news-box-menu").addClass('padding-key');
	$("#more-rubrics").slideDown();
}

//
function isd(block){
	block="#"+block;
	$(block).slideToggle();
}
$(document).ready(function() {
	
	$("a.inline").fancybox({
		'hideOnContentClick': true
	});
	
});



