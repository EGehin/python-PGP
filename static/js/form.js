$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				message : $('#messageInput').val(),
				pgp : $('#pgpInput').val()
			},
			type : 'POST',
			url : '/process'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.message1).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});
