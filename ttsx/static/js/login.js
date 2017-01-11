$(function () {
        var error_name = false;
	    var error_password = false;
function check_user_name(){

	    $('.form_input>.user_error').hide()
		var len = $('.name_input').val().length;
		if(len<5||len>20)
		{
			$('.name_input').next().html('请输入5-20个字符的用户名')
			$('.name_input').next().show();
			error_name = true;
		}
		else
		{
			$('.name_input').next().hide();
			error_name = false;
		}
	}

function check_pwd(){
		var len = $('.pass_input').val().length;
		if(len<8||len>20)
		{
			$('.pass_input').next().html('密码最少8位，最长20位')
			$('.pass_input').next().show();
			error_password = true;
		}
		else
		{
			$('.pass_input').next().hide();
			error_password = false;
		}
	}

$('form').submit(function() {
		check_user_name();
		check_pwd();
	    event.preventDefault();

		if(error_name == false && error_password == false)
		{
			$.post("", { username: $('.name_input').val(), pwd: $('.pass_input').val()}, function(data){
				if(data.login){
					data.come ?window.location.href = data.come:window.location.href = '/'
				}else {
					 $('.form_input>.user_error').show()
				}
              });
		}
		else
		{
			return false;
		}

	});





});