
from .validationMassages import validation_message
from django.db import transaction
from .models import Customer, Address, ContactPerson

def validate_customer(params):
    customer_name = params.get("customer_name")
    customer_alias = params.get("customer_alias") 
    pan_number = params.get("pan_number") 
    gstn_number = params.get("gstn_number") 
    created = params.get("created") 
    modified = params.get("modified")


    if not customer_name:
        return False, "customer name is mandatory", None
    if not pan_number:
        return False, "pan number is mandatory", None
    if not gstn_number:
        return False, "gstn number is mandatory", None

    kwargs = {
        "customer_name": customer_name,
        "customer_alias": customer_alias,
        "pan_number": pan_number,
        "gstn_number": gstn_number,
        "created": created,
        "modified": modified
    }
    return True, validation_message["105"], kwargs

def create_customer(data):
    try:
        with transaction.atomic():
            customer_obj = {}
            customer_obj["customer_name"] = data["customer_name"]
            customer_obj["customer_alias"] = data["customer_alias"]
            customer_obj["pan_number"] = data["pan_number"]
            customer_obj["gstn_number"] = data["gstn_number"]
            customer_obj["created"] = data["created"]
            customer_obj["modified"] = data["modified"]

            customer = Customer.objects.create(**customer_obj)
            customer_id = customer.id
            return customer_id, True
    except Exception as e:
        print (e)
        return None, False

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

def create_customer_address(data):
    try:
        with transaction.atomic():
            customer_address = Address.objects.create(**data)
            return True
    except Exception as e:
        print(e)
        return False

def validate_customer_contactPerson(data, customer_id):
    if not data.get("name") and not data.get("mobile_number1"):
        return False, "customer name and mob num is compulsary", None
    kwargs = {
        "customer": Customer.objects.get(id = customer_id),
        "name": data.get("name") ,
        "email": data.get("email"), 
        "mobile_number1": data.get("mobile_number1"), 
        "mobile_number2": data.get("mobile_number2") 
    }
    return True, "customer contact person created successfully", kwargs

def create_customer_contactPerson(data):
    try:
        with transaction.atomic():
            customer_contactPerson = ContactPerson.objects.create(**data)
            return True
    except Exception as e:
        print(e)
        return False
def create_object(model, data):
    try:
        with transaction.atomic():
            obj = model.objects.create(**data)
            return obj.id, True
    except Exception as e:
        print(e)
        return False