
from .validationMassages import validation_message
from django.db import transaction
from .models import Customer

def validate_customer(params):
    customer_name = params.get("customer_name")
    customer_alias = params.get("customer_alias") 
    pan_number = params.get("pan_number") 
    gstn_number = params.get("gstn_number") 
    created = params.get("created") 
    modified = params.get("modified")

    # address = params.get("address")
    # state = params.get("state")
    # city = params.get("city")
    # pincode = params.get("pincode")

    # name = 
    # email = 
    # mobile_number1 = 
    # mobile_number2 = 

    if not customer_name:
        return False, "customer name is mandatory", None
    if not pan_number:
        return False, "pan number is mandatory", None
    if not gstn_number:
        return False, "gstn number is mandatory", None
    # if not address:
    #     return False, "address is mandatory", None
    # if not name:
    #     return False, "name is mandatory", None
    # if not mobile_number1:
    #     return False, "mobile_number1 is mandatory", None

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

