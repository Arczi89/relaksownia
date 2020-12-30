$(document).ready(function() {

    $('#customer-opinions').slick({
        arrows: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        adaptiveHeight: false,
        responsive: [
                        {
                          breakpoint: 1100,
                          settings: {
                            slidesToShow: 2,
                            slidesToScroll: 1
                          }
                        },
                        {
                          breakpoint: 768,
                          settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1,
                          }
                        },
                                                {
                          breakpoint: 320,
                          settings: {
                            slidesToShow: 1,
                            slidesToScroll: 1,
                            dots: false,
                          }
                        },
                      ]
    });

    console.log('ready!');
});