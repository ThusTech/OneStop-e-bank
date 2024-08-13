$(function(){
    $('.login').click(function(){
        const email = $("#email").val();
        const password = $("#password").val();

        data = {
            'email':email,
            'password':password
        }

        $.ajax({
            url:"http://127.0.0.1:8080/login",
            type:  'POST',
            contentType: 'application/json',
            data: JSON.stringify({ data: data}),
        //     success:,
        //     error:,
        })
    })
})  