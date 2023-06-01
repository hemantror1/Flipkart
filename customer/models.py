from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name=models.CharField(max_length=15,null=True,blank=True)
    last_name=models.CharField(max_length=15,null=True,blank=True)
    mobile=models.IntegerField(null=True,blank=True)
    adress=models.TextField(null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    city=models.CharField(max_length=20,null=True,blank=True)
    dob=models.DateField(max_length=15,null=True,blank=True)

    
    def __str__(self):
        return self.first_name

class CustomerAddress(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,related_name='customer_addresses')
    Street_name=models.CharField(max_length=15,null=True,blank=True)
    Street_number=models.IntegerField(null=True,blank=True)
    city=models.CharField(max_length=15,null=True,blank=True)
    state=models.CharField(max_length=20,null=True,blank=True)
    country=models.CharField(max_length=20,null=True,blank=True)
    pin_code=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.Street_name
    
class CustomerAdhar(models.Model):
    Customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
    adhar_number=models.IntegerField(null=True,blank=True)
    adhar_name=models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return str(self.adhar_name)

