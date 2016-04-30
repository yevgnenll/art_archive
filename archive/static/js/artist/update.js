(function(){
    $(document).ready(function(){
        artist_id = $('#update_btn').data('artist-id');

        $('#update_btn').click(function(){
		    $.ajax({
                url: "/api/artists/" + artist_id,
                dataType: "json",
                method: "PUT",
                data: {
                    "name": $('#name').val(),
                    "birth_year": $('#birth_year').val(),
                    "death_year": $('#death_year').val(),
                    "country": $('#country').val(),
                    "genre": $('#genre').val(),
                    }
                }).success(function(result){
                  console.log(result);
                  $('.code').text("code: "+ result.code);
                  $('.result').text(", result: "+  result.result);
                });
            });

        });
})();
