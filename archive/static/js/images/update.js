(function(){
    $(document).ready(function(){

        var image_id = $('#update_btn').data('image-id');

        $('#update_btn').click(function(){
		    $.ajax({
                url: "/api/images/" + image_id,
                dataType: "json",
                method: "PUT",
                data: {
                    'artist_id': $('#artist_id').val(),
                    'title': $('#title').val(),
                    'image_url': $('#image_url').val(),
                    'year': $('#year').val(),
                    'description': $('#description').val()
                    }
                }).success(function(result){
                  console.log(result);
                  $('.form_update').css('display','none');
                  $('.code').text("code: "+ result.code);
                  $('.result').text(", result: "+  result.result);
                });
            });

        });
})();
