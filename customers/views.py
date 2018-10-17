from django.shortcuts import render
from django.http import JsonResponse
import json
from django.db import transaction
from .validationMassages import validation_message
from .helper_functions import  validate_customer, create_customer
from .models import Customer, Address, ContactPerson

def create_new_customer(request):
    if request.method == 'POST':
        try:
            params = json.loads(request.body)
            # if 'jsonObj' in params:
            print("params>>>>", params)
            # params = params.get('jsonObj')
            status, validation, data = validate_customer(params)
            print("after validate_customer>>", status, validation, data)
            if not status:
                return JsonResponse({
                    "validation": validation,
                        "status": status
                })
            customer_id, status = create_customer(data)
            if status:
                return JsonResponse({
                    "validation": "customer created successfully",
                    "status": True
                })
            return JsonResponse({
                "validation": "Failed",
                "status": False
            })

        except Exception as e:
            print(e)
            return JsonResponse({
                "validation": validation_message['101'],
                "status": False
            })
    else:
        return JsonResponse({
            "validation": validation_message['101'],
            "status": False
        })
