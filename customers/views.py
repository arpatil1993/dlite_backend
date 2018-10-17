from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db import transaction
from .validationMassages import validation_message
from .helper_functions import  *
from .models import Customer, Address, ContactPerson

def responseOnStatus(status, validation=None):
    if not status:
        response = {
            status: status,
            validation: validation,
        }
        # response.setdefault(validation, None)
        return response, False
    return None, True

def create_new_customer(request):
    if request.method == 'POST':
        try:
            params = json.loads(request.body)
            status, validation, data = validate_customer(params)
            if not status:
                return JsonResponse({"validation": validation, "status": status})
            customer_id, status = create_object(Customer, data)
            if not status:
                return JsonResponse({"validation": validation, "status": status})
            status, validation, data = validate_customer_address(params, customer_id)
            if not status:
                return JsonResponse({"validation": validation, "status": status})
            address_id, status = create_object(Address, data)
            if not status:
                return JsonResponse({"validation": validation, "status": status})
            status, validation, data = validate_customer_contactPerson(params,customer_id)
            contactPerson_id, status = create_object(ContactPerson, data)
            if not status:
                return JsonResponse({"validation": validation, "status": status})
            responseOnStatus(status,validation)
            return JsonResponse({
                    "validation": "customer contact person created sucessfully",
                    "status": True
                })
        except Exception as e:
            print(e)
            return JsonResponse({
                "validation": "failed with exception",
                "status": False
            })
    else:
        return JsonResponse({
            "validation": "It is not a post request",
            "status": False
        })
