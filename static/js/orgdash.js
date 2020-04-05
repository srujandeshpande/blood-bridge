$(function(){

  $('#newAlert').submit(function(e){
      e.preventDefault();
      email = $('#email_div').data('email');
      data = $('#newAlert').serialize();
      data['email'] = email;
      $.ajax({
          url:'/add_new_alert',
          type:'post',
          data:data,
          success:function(){
              $('#newAlertSuccess').removeAttr('hidden');
              $('#newAlertForm')[0].reset();
          },
          error:function(){
              $('#newAlertFailure').removeAttr('hidden');
          }
      });
  });


});
