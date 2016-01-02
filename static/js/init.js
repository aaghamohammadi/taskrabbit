$(document).ready(function () {
    $('.button-collapse').sideNav();
    $('.parallax').parallax();

    $('.dropdown-button').dropdown({
        inDuration: 300,
        outDuration: 225,
        constrain_width: false,
        hover: true,
        gutter: -25,
        belowOrigin: true,
        alignment: 'left'
    });
    $('.modal-trigger').leanModal();
});



