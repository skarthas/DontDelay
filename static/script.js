$(function(){
	$('button').click(function(){
		var fnum = $('#txtflnum').val();
		var fdate = $('#txtfldate').val();
        var fac = $('#txtflac').val();
        var fdept = $('#txtfldept').val();
        var fori = $('#txtflor').val();
        var fdest = $('#txtfldest').val();
		$.ajax({
			url: '/FindDelay',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});