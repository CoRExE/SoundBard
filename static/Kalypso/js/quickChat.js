$(document).ready(function() {
    $('#quick-chat').keyup(function(event) {
        if (event.keyCode === 13) {
            let message = $(this).val();
            $(this).after('<div class="spinner"></div>');  // Show spinner
            $.ajax({
                url: '/kalypso/quick-chat/',
                data: {
                    'message': message
                },
                dataType: 'json',
                success: function(data) {
                    console.log(data.response);
                    $('#chat-box').append('<div class="chat-message"><p>' + data.response + '</p></div>');
                    $('#quick-chat').val('');
                },
                complete: function() {
                    $('.spinner').remove();  // Remove spinner
                }
            });
        }
    });
});