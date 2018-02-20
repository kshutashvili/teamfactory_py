(function () {

   function getCookie(name) {
       var cookieValue = null;
       if (document.cookie && document.cookie !== '') {
           var cookies = document.cookie.split(';');
           for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
               // Does this cookie string begin with the name we want?
               if (cookie.substring(0, name.length + 1) === name + '=') {
                   cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                   break;
               }
           }
       }
       return cookieValue;
   }

   var csrftoken = getCookie('csrftoken');

   function csrfSafeMethod(method) {
       // these HTTP methods do not require CSRF protection
       return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method)
       );
   }

   $.ajaxSetup({
       beforeSend: function beforeSend(xhr, settings) {
           if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
               xhr.setRequestHeader("X-CSRFToken", csrftoken);
           }
       }
   });
})();


$(document).ready(function(){
	$('#form_registration').submit(function(e){
		e.preventDefault();
		url = $('#form_registration').attr('action');
		name = $('#form_registration input#id_name').val();
		phone = String($('#form_registration input#id_phone').val());
		course_id = $('#form_registration select#id_course').val();
	$('#learn_modal').css('display','none');
	$('.modal-backdrop.in').css('opacity','0');
		$.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            data:{
                'name':name,
                'phone':phone,
                'course_id':course_id,
            },
            success: function(data){
               		console.log(data.new_number_seats);
                		
                
             }
            });
       });
	});