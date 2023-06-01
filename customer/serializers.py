from rest_framework import serializers
from customer.models import *

class GetCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
                                                 
class GetAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAddress
        fields = "__all__"

class CustomerDetailsAddressSerializer(serializers.ModelSerializer):
    customer_addresses=GetAddressSerializer(many=True)
    
    class Meta:
        model = Customer
        fields = ('first_name','last_name','mobile','adress','age','country','city','dob')