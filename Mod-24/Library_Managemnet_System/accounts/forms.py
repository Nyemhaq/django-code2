
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserAccount, UserAddress

class UserRegistrationForm(UserCreationForm):
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'postal_code', 'city','country', 'address']
        
        
    def save(self, commit=True):
        our_user = super().save(commit=False) 
        if commit == True:
            our_user.save() 
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            city = self.cleaned_data.get('city')
            address = self.cleaned_data.get('address')
            
            UserAddress.objects.create(
                user = our_user,
                postal_code = postal_code,
                country = country,
                city = city,
                address = address
            )
            UserAccount.objects.create(
                user = our_user,
                account_no = 100000+ our_user.id
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })



class UserUpdateForm(forms.ModelForm):
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })


        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['address'].initial = user_address.address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user)
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_address.address = self.cleaned_data['address']
            user_address.city = self.cleaned_data['city']
            user_address.postal_code = self.cleaned_data['postal_code']
            user_address.country = self.cleaned_data['country']
            user_address.save()

        return user