/**
 * Created by garfild on 1/31/16.
 */
$(document).ready(function () {
    $('.comment_form').submit(function () {
        $.ajax({
            data: $(this).serialize(),
            type: $(this).attr('method'), // GET or POST
            url: $(this).attr('action'), // the file to call
            success: function (response) { // on success..
                window.location.reload();
            }
        });
        return false;
    });
});