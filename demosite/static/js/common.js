$(document).ready(function() {

    $('#customer-opinions').slick({
        arrows: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        adaptiveHeight: false,
    });

    console.log('ready!');
});