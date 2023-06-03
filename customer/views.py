from django.shortcuts import render
from customer.models import *
from customer.serializers import *
# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class GetCustomerView(APIView):
    def get(self,request):
        instance=Customer.objects.all()
        serializer = GetCustomerSerializer(instance,many=True)
        return Response(serializer.data)
    def  post(self,request):
      params=request.data
      print("data",params)
      serl=GetCustomerSerializer(data=params)
      serl.is_valid(raise_exception=True)
      serl.save()
      return Response({"Message":"Save Sucessfully"})
class GetAddressView(APIView):
 
   def get(self,request):
       instance=Customer.objects.all()
       serializer = GetCustomerSerializer(instance,many=True)
       return Response(serializer.data)
   
class GetCustomerDetailsAddressView(APIView):
   
   def get(self,request,pk):
       instance=Customer.objects.filter(id=pk)
       serializer=CustomerDetailsAddressSerializer(instance,many=True)
       return Response(serializer.data)