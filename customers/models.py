from django.db import models


class Customer(models.Model):
    customer_name = models.CharField(max_length = 20)
    customer_alias = models.CharField(max_length = 20, null = True, blank = True)
    pan_number = models.CharField(max_length = 25)
    gstn_number = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add = True, editable = False)
    modified = models.DateTimeField(auto_now = True, editable = False)

    def __str__(self):
        return self.customer_name

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    address = models.TextField()
    state = models.CharField(max_length = 25, null = True, blank = True)
    city = models.CharField(max_length = 25, null = True, blank = True)
    pincode = models.CharField(max_length = 25, null = True, blank = True)
    is_active = models.BooleanField(default = True)
    
    def __str__(self):
        return self.customer.customer_name

class ContactPerson(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length = 25)
    email = models.EmailField(null = True, blank = True)
    mobile_number1 = models.CharField(max_length = 10)
    mobile_number2 = models.CharField(max_length = 10, null = True, blank = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

