
from .validationMassages import validation_message
from django.db import transaction
from .models import Customer, Address, ContactPerson

def validate_customer(params):
    if not (params.get("customer_name") and params.get("pan_number") and params.get("gstn_number")):
        return False, "customer name, pan number, gstn number is mandatory", None

    kwargs = {
        "customer_name": params.get("customer_name"),
        "customer_alias": params.get("customer_alias"),
        "pan_number": params.get("pan_number"),
        "gstn_number": params.get("gstn_number"),
        "created": params.get("created"),
        "modified": params.get("modified")
    }
    return True, validation_message["105"], kwargs

def validate_customer_address(data, customer_id):
    # print("data in validate_customer_address", data)
    if not data.get("address"):
        return False, "customer address is mandatory", None
    
    kwargs = {
        "customer" : Customer.objects.get(id = customer_id),
        "address" : data.get("address"),
        "state" : data.get("state"),
        "city" : data.get("city"),
        "pincode" : data.get("pincode")
    }
    print("dictionary object: ", kwargs)
    return True, validation_message["105"], kwargs


def validate_customer_contactPerson(data, customer_id):
    if not (data.get("name") and data.get("mobile_number1")):
        return False, "customer name and mob num is compulsary", None
    kwargs = {
        "customer": Customer.objects.get(id = customer_id),
        "name": data.get("name") ,
        "email": data.get("email"), 
        "mobile_number1": data.get("mobile_number1"), 
        "mobile_number2": data.get("mobile_number2") 
    }
    return True, "customer contact person created successfully", kwargs


def create_object(model, data):
    try:
        with transaction.atomic():
            obj = model.objects.create(**data)
            return obj.id, True
    except Exception as e:
        print(e)
        return False