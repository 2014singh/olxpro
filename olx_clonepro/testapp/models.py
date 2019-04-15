from django.db import models


class UserRegistrationData(models.Model):
    user_name=models.CharField(max_length=30)
    user_mobile=models.BigIntegerField()
    user_email=models.EmailField(max_length=30)
    password1 = models.CharField(max_length=10)
    password2 = models.CharField(max_length=10)

    def __str__(self):
        return self.user_name

class UserSellingData(models.Model):
    rel_id = models.ForeignKey(UserRegistrationData)
    product_id = models.AutoField(primary_key=True)
    bike_name = models.CharField(max_length=30)
    bike_price = models.IntegerField()
    bike_old = models.IntegerField()
    bike_desc = models.CharField(max_length=300)
    bike_img = models.ImageField(upload_to='bikeimg/%Y/%m/%d/',max_length=200,blank=True)
    currdata = models.DateField(max_length=100)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.bike_name




