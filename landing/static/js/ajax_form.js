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


$(document).ready(function(){
  $('*[data-show="show_event"]').click(function(){
    var url = $(this).data('url');
    var id  = $(this).data('id_event');
    $.ajax({
            type: "GET",
            url: url,
            dataType: "json",
            data:{
                'id':id,
            },
            success: function(data)
            {
              console.log(data.event.id);
              var theme = data.event.theme;
              var full_name  = data.event.lector.name + " " + data.event.lector.surname;
              var where  = data.event.where;
              var when  = data.event.when;
              var description  = data.event.description;
              when  = when.split('+')[0];
              var position = data.event.lector.position;
             $('#register_event').attr('data-event_id' , data.event.id);
             $('.title_pop h1').text(theme);
             $('.title_pop span#full-name').text(full_name);
             $('.title_pop span#position').text(position);
             $('span#where').text(where);
             $('span#when').text(when);
             $('span#lector').text(full_name);
             $('p#description').text(description);
            }
  })
})
})


$(document).ready(function(){
  $('#register_event').submit(function(e){
    e.preventDefault();
    var url = $(this).attr('action');
    var name = $('#id_name_client').val();
    var phone = $('#id_phone_client').val();
    var id_event  = $(this).attr('data-event_id');
    
  function reload(){
        $('.modal-open').css('overflow' , 'auto');
        $('body').css('overflow-x' , 'hidden');
        $('body').css('padding-right' , '0');
        $('#register_event input#id_name_client').val('');
        $('#register_event input#id_phone_client').val('');
 
    }
    $.ajax({
      type: "POST",
      url: url,
      dataType: "json",
      data:{
              'name':name,
              'phone':phone,
              'id_event':id_event,
            },
      success: function(data)
      {
        console.log(data);
        
       $('#events_modal').hide(500);
        $('#thanks-register-event').toggle(500);
        reload();
        console.log(data);
      }

    })
  })
})
