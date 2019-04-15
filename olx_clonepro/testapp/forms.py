from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    user_name = forms.CharField(
        label='Enter Name',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Name'
            }
        )
    )
    user_mobile = forms.CharField(
        label='Mobile Number',
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Mobile No.'
            }
        )
    )
    user_email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Email'
            }
        )
    )
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'form-control',
                'placeholder' : 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Re-Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Re-Enter Password'
            }
        )
    )

    # def clean_password1(self):
    #     inpname = self.cleaned_data.get('password1')
    #     if len(inpname)<8:
    #         print('inside if valid before forms.ValidationError')
    #         raise forms.ValidationError('Length of name must be more than 8')
    #     print('inside if valid before forms.ValidationError')
    #     return inpname

    # def clean(self):
    #     data = super().clean()
    #     psw1 = data['password1']
    #     psw2 = data['password2']
    #     if psw1!=psw2:
    #         raise forms.ValidationError('Both password must be match')







#
# class UserSellingForm(forms.Form):
#
#     bike_name = forms.CharField(
#         label='Bike Name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'placeholder': 'BikeName'
#             }
#         )
#     )
#     bike_price = forms.IntegerField(
#         label='Bike Price',
#         widget=forms.NumberInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'BikePrice'
#             }
#         )
#     )
#     bike_old = forms.IntegerField(
#         label='Bike Model',
#         widget=forms.NumberInput(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'How Old'
#             }
#         )
#     )
#     bike_desc = forms.CharField(
#         label='Enter Description',
#         widget=forms.Textarea(
#             attrs={
#                 'class' : 'form-control',
#                 'placeholder' : 'Description'
#             }
#         )
#     )
#     bike_img = forms.ImageField(
#         label='Upload Image',
#         widget=forms.FileInput()
#
#     )





class UserLoginForm(forms.Form):
    user_email = forms.EmailField(
        label='Enter Email',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Email'
            }
        )
    )
    password1 = forms.CharField(
        label='Enter Password',
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Password'
            }
        )
    )

    # def clean(self):
    #     cleaned_data=super().clean()
    #     password1=cleaned_data['']







