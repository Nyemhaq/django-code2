from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


class UserAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_no = models.IntegerField(unique=True, null=False) 
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    
    def __str__(self):
        return str(self.account_no)
    
    def save(self, *args, **kwargs):
        if not self.account_no:
            unique = False
            while not unique:
                account_no = get_random_string(length=6, allowed_chars='1234567890')
                if not UserAccount.objects.filter(account_no=account_no).exists():
                    unique = True
            self.account_no = account_no
        super().save(*args, **kwargs)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length= 100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.user.email)
    
def set_user_address(self, address, city, postal_code, country):
    address_obj, created = UserAddress.objects.get_or_create(user=self)
    address_obj.address = address
    address_obj.city = city
    address_obj.postal_code = postal_code
    address_obj.country = country
    address_obj.save()

User.set_user_address = set_user_address

def set_user_address_view(request, user_id):
    user = User.objects.get(id=user_id)


    