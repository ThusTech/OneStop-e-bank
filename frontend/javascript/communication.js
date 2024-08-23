$(function(){
    $('#login').click(function(){
        const email = $("#email").val();
        const password = $("#password").val();

        data = {
            'email':email,
            'password':password
        }

        $.ajax({
            url:"http://localhost:8080/auth/login",
            type:  'POST',
            data: data,
            dataType: 'json',
            xhrFields:{
                withCredentials: true,
            },
            success: function(data){
                // alert(data)
            },
            error: function(error){
                // alert(error)
            }
        })
    })
})  