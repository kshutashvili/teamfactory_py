$(document).ready(function(){
	var i=0;
	$('#others').click(function(){
		$('.many_event').slideToggle(600);
		$('.many_event').css('display' ,  'flex');
		if(i % 2 == 0)
			{
				$('#arrow').css('transform', 'rotate(180deg)');
				
			}
		else
			{
				$('#arrow').css('transform', 'none');
				
			}
		i++;
	}
)});

 
$(document).ready(function(){
	$("nav").on("click","a", function (event) {
		//отменяем стандартную обработку нажатия по ссылке
		event.preventDefault();

		//забираем идентификатор бока с атрибута href
		var id  = $(this).attr('href'),

		//узнаем высоту от начала страницы до блока на который ссылается якорь
			top = $(id).offset().top;
		
		//анимируем переход на расстояние - top за 1500 мс
		$('body,html').animate({scrollTop: top}, 1500);
	});
});



$(document).ready(function(){
  $('body').append('<a href="#" id="go-top" title="Вверх"></a>');
});

$(function() {
 $.fn.scrollToTop = function() {
  $(this).hide().removeAttr("href");
  if ($(window).scrollTop() >= "250") $(this).fadeIn("slow")
  var scrollDiv = $(this);
  $(window).scroll(function() {
   if ($(window).scrollTop() <= "250") $(scrollDiv).fadeOut("slow")
   else $(scrollDiv).fadeIn("slow")
  });
  $(this).click(function() {
   $("html, body").animate({scrollTop: 0}, "slow")
  })
 }
});

$(function() {
 $("#go-top").scrollToTop();
});


$(document).ready(function(){
	$('#id').click(function(){
		$('#want_learn_modal').css('display' , 'block');
	})
})


// function windowSize(){
//     if ($(window).width() <= '660'){
//     	alert('asdasdasd');
//         $('header').css('background' , 'url(static/image/mobile_header.png)');
//     } 
// }


function back_photo()
{
	if($(window).width() <= 1024)
	{
		$('header').css('background' , 'url(/static/image/tablet_header.png)');
		$('header').css('background-size' , '100%');
		$('header').css('background-repeat' , 'no-repeat');
	}
	if( $(window).width() <= 660)
	{
		$('header').css('background' , 'url(/static/image/tablet_header.png)');
		$('header').css('background-size' , '100%');
		$('header').css('background-repeat' , 'no-repeat');
		$('.author').each(function(index , value){
			$(this).css('background' , 'url(/static/image/mob_aut_back.png)');
		});
		$('.photo').each(function(index , value){
			$(this).css('background' , 'url(/static/image/back_photo_mob.png)');
			$(this).css('background-size' , 'contain');
			$(this).css('background-repeat' , 'no-repeat');
		});
		// var all_authors = $('.author');
		// for(var i = 0; i < all_authors.length; i++)
		// {
		// 	$(this).css('background' , 'url(/static/image/mob_aut_back.png)');
		// }
	}
}
// $(window).resize(function(){
// 	// alert($( window ).width());
	
// })


// $(document).load(windowSize); // при загрузке
// $(document).resize(windowSize); // при изменении размеров
// // или "два-в-одном", вместо двух последних строк:
$(window).on('load resize', back_photo);