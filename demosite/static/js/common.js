$(document).ready(function() {

    $(window).scroll(function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#back-to-top').click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 400);
        return false;
    });

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
    $('[data-toggle="tooltip"]').tooltip()

    function onIsVatClicked() {
        let isVat = document.getElementById("id_is_vat").checked;

        ["company_name", "nip"].forEach((item) => {
            showField(item, isVat);
            clearField(item);
            clearErrors(item, isVat);
        });
    }

    function onDeliveryKindChanged() {
        let isInpost = document.getElementById("id_delivery_kind").value == "INPOST";

        ["inpost_code", "delivery_place"].forEach((item) => {
            showField(item, isInpost);
            clearField(item);
            clearErrors(item, isInpost);
        });

        ["street", "postcode", "city"].forEach((item) => {
            showField(item, !isInpost);
            clearField(item);
            clearErrors(item, !isInpost);
        });
    }

    function clearField(field) {
        if(document.getElementById("id_"+field)) {
            document.getElementById("id_"+field).value = "";
        }
    }

    function clearErrors(field, show) {
        if(document.getElementById("error_"+field)) {
            document.getElementById("error_"+field).style.display = show ? 'block' : 'none';
        }
    }

    function showField(field, show) {
        if(document.getElementById("form_"+field)) {
            document.getElementById("form_"+field).style.display = show ? 'block' : 'none';
        }
    }


    document.getElementById("id_is_vat").onclick = onIsVatClicked;
    document.getElementById("id_delivery_kind").onclick = onDeliveryKindChanged;

    onIsVatClicked();
    onDeliveryKindChanged();

    console.log('ready!');
});