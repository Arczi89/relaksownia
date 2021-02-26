from promo.models import DeliveryKind


def get_initialized_form_data():
    return {
        "email": "",
        "contact_name": "",
        "company_name": "",
        "street": "",
        "postcode": "",
        "city": "",
        "phone": "",
        "inpost_code": "",
        "delivery_place": "",
        "is_vat": False,
        "is_company": False,
        "nip": "",
        "permission": False
    }


def retrieve_incorrect_form_data_courier_to_person():
    form = get_initialized_form_data()
    form['is_vat'] = False
    form['delivery_kind'] = DeliveryKind.get_value("COURIER")
    return form


def retrieve_incorrect_form_data_inpost_to_person():
    form = get_initialized_form_data()
    form['is_vat'] = False
    form['delivery_kind'] = DeliveryKind.get_value("INPOST")
    return form


def retrieve_incorrect_form_data_courier_to_company():
    form = get_initialized_form_data()
    form['is_vat'] = True
    form['delivery_kind'] = DeliveryKind.get_value("COURIER")
    return form


def retrieve_incorrect_form_data_inpost_to_company():
    form = get_initialized_form_data()
    form['is_vat'] = True
    form['delivery_kind'] = DeliveryKind.get_value("INPOST")
    return form


def retrieve_correct_form_data():
    return {
        "email": "a@a.pl",
        "contact_name": "John Kowalsky",
        "postcode": "",
        "street": "",
        "city": "",
        "phone": "0123456789",
        "inpost_code": "GLI06A",
        "delivery_place": "",
        "is_vat": False,
        "delivery_kind": DeliveryKind.get_value("INPOST"),
        "nip": "",
        "permission": True
    }
