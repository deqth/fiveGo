$(function () {
    var error_name = false;
    var error_address = false;
    var error_zipcode = false;
    var error_tel = false;
    var oBtn = document.getElementById('info_submit');


    $('#uname').blur(function () {
        check_uname()
    });

    $('#address').blur(function () {
        check_address()
    });

    $('#zipcode').blur(function () {
       check_zipcode()
    });

    $('#tel').blur(function () {
        check_tel()
    });
    $('#info_submit').click(function () {
        checkform()
    })


    function check_uname() {
        var len = $('#uname').val().length;
        if(len<2 ||len>20){
            $('#uname').next().html('<em  style="color:red;">请输入正确的收件人姓名</em>')
            $('#uname').next().show();
            error_name = true;
        }
        else{
            $('#uname').next().hide()
            error_name = false;
        }

    };

    function check_address() {
        var len = $('#address').val().length
        if (len<10||len>50){
            $('#address').next().html('<em  style="color:red;">请输入正确的收货地址</em>')
            $('#address').next().show()
            error_address = true;
        }
        else{
            $('#address').next().hide()
            error_address = false;
        }
    };

    function check_zipcode() {
        var re = /^[0-9]{6}/;
        if (re.test($('#zipcode').val())){
            $('#zipcode').next().hide()
            error_zipcode = false
        }
        else{
            $('#zipcode').next().html('<em  style="color:red;">请输入正确的邮编例如（130021）</em>')
            $('#zipcode').next().show()
            error_zipcode = true
        }
    };

    function check_tel() {
        var re = /^[0-9]{11}/;
        if (re.test($('#tel').val())){
            $('#tel').next().hide()
            error_zipcode = false
        }
        else{
            $('#tel').next().html('<em  style="color:red;">请输入正确的电话号码</em>')
            $('#tel').next().show()
            error_zipcode = true
        }
    };

     function checkform() {
        if (error_name==true || error_address==true || error_zipcode==true || error_tel==true ) {
            alert("收货信息错误请重新填写");
            return false;
        }
        else{
            return true;
        }
    }

});