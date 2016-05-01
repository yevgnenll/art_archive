(function(){
    $(document).ready(function(){

        var delete_id = $('#delete_item').data('image-id');

        $('#delete_item').click(function(){
            $.ajax({
                url: "/api/images/" + delete_id,
                dataType: "json",
                method: "DELETE"

            }).success(function(result){

                console.log(result);
                $('.before_delete').css('display','none');
                $('.code').text("code: "+ result.code);
                $('.result').text(", result: "+  result.content.result);
            });
        });
    });
})();
