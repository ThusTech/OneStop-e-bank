$(function(){
    $('.login').click(function(){
        const email = $("#email").val();
        const password = $("#password").val();

        data = {
            'email':email,
            'password':password
        }

        $.ajax({
        //     url:,
            type:  'POST',
            contentType: 'application/json',
            data: JSON.stringify({ data: data}),
        //     success:,
        //     error:,
        })
    })
})  