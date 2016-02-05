/**
 * Created by garfild on 1/31/16.
 */
$(document).ready(function () {
    $('.comment_form,.rate_form').submit(function () {
        console.log("salam");
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function (response) { // on success..
                $(document).ajaxStop(function () {
                    location.reload(true);
                });
            }
        });
        return false;
    });


});