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

    function reload(){
        $('.modal-open').css('overflow' , 'auto');
        $('body').css('overflow-x' , 'hidden');
        $('body').css('padding-right' , '0');
        $('#form_registration input#id_name').val('');
        $('#form_registration input#id_phone').val('');
        $('#form_registration select#id_course').val('');   
    }
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
              number = String(data.new_number_seats);
              if (number.length == 1)
              {
                $('#course_id_' + data.course_id + '.btn_course button:nth-child(2)').css('display' , 'none');
                $('#course_id_' + data.course_id + '.btn_course button:first-child').text(number[0]);
              }
              else{
                 $('#course_id_' + data.course_id + '.btn_course button:first-child').text(number[0]);
                 $('#course_id_' + data.course_id + '.btn_course button:nth-child(2)').text(number[1]);
              }
              if(number == '0')
              {
                $('#course_id_' + data.course_id + '.btn_course').css('display' , 'none');
                $('#none-seats-' + data.course_id).addClass('zero-number');
                $('a#id_' + data.course_id).css('display' , 'none');
              }
              reload();
             $('#thanks_register').toggle('slow');
             },
             error: function(data_error){
                    $('#error').toggle('slow');
                    $('#error_close').click(function(){
                        $('#error').hide(500);
                    
                    });
                   reload();
              }
            });
       });
	});