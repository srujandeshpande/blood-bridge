$(function(){

  $('#newAlert').submit(function(e){
      e.preventDefault();
      $.ajax({
          url:'/add_new_alert',
          type:'post',
          data:$('#newAlert').serialize(),
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
