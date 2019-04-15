from django.shortcuts import render,redirect
from .forms import UserRegistrationForm,UserLoginForm
from .models import UserSellingData,UserRegistrationData
from django.http.response import HttpResponse
from django.contrib import messages
import re

def home_view(request):
    ads = UserSellingData.objects.all()
    my_dict = {'data':ads}
    return render(request,'home.html',my_dict)


import datetime
currdate = datetime.datetime.now()


# print(email)


def selling_view(request):
    count = 0
    if request.method == 'POST':
        bike_name = request.POST.get('bike_name')
        bike_price = request.POST.get('bike_price')
        bike_old = request.POST.get('bike_old')
        bike_disc = request.POST.get('bike_disc')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        bike_picture = request.FILES['bike_picture']
        id = request.COOKIES.get('id')
        print(id,'inside post get method')
        print(bike_name,bike_price,bike_old,bike_disc,mobile,address,bike_picture,id)

        data = UserSellingData(
            bike_name=bike_name,
            bike_price=bike_price,
            bike_old=bike_old,
            bike_desc=bike_disc,
            bike_img=bike_picture,
            currdata=currdate,
            mobile=mobile,
            address=address,
            rel_id_id= int(id),
        )
        print('before save()')
        data.save()

        ads = UserSellingData.objects.all()
        my_dict = {'data': ads}
        print(count)
        return render(request, 'home.html', my_dict)
    else:
        msg = 'Pls fills all the details'
        return render(request,'adpost.html',{'msg':msg})


def registration_view(request):
    if request.method == 'POST':
        rform = UserRegistrationForm(request.POST)
        if rform.is_valid():
            user_name = request.POST.get('user_name')
            user_mobile = request.POST.get('user_mobile')
            user_email = request.POST.get('user_email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')


            check = True
            if len(user_name)<5:
                rform = UserRegistrationForm()
                my_dict = {'rform':rform}
                messages.success(request,'User name length must be greater than 5')
                return render(request,'registration.html',my_dict)

            if (password1 and user_name) in UserRegistrationData.objects.all():
                rform = UserRegistrationForm()
                my_dict = {'rform':rform}
                messages.error(request,'Username already exist')
                return render(request,'registration.html',my_dict)

            if password1 != password2:
                messages.error(request,'Both password must be match')
                rform = UserRegistrationForm()
                return render(request,'registration.html',{'rform':rform})

            if len(str(password1)) >=8:
                match = re.fullmatch('[0-9a-zA-Z]*',str(password1))
                if match != None:
                    pass


                else:
                    rform = UserRegistrationForm()
                    messages.error(request,"Don't use special character")
                    return render(request,'registration.html',{'rform':rform})



            if len(str(password1)) <8:
                rform = UserRegistrationForm()
                messages.error(request, "Password length must be 8 character")
                return render(request, 'registration.html', {'rform': rform})

            if (len(str(user_mobile)) < 10):
                messages.error(request, 'Please enter a valid number')
                rform = UserRegistrationForm()
                return render(request, 'registration.html', {'rform': rform})


            if len(str(user_mobile)) == 10:
                match = re.fullmatch('[6-9][0-9]{9}',user_mobile)
                if match != None:
                    pass
                else:
                    messages.error(request, "Please enter a valid number")
                    rform = UserRegistrationForm()
                    return render(request, 'registration.html', {'rform': rform})

            if len(str(user_mobile)) > 10:
                messages.error(request, "Please enter a valid number")
                rform = UserRegistrationForm()
                return render(request, 'registration.html', {'rform': rform})



            data = UserRegistrationData(
                user_name=user_name,
                user_mobile=user_mobile,
                user_email=user_email,
                password1=password1,
                password2=password2,
            )

            data.save()
            msg = 'Enter Your Login Details..'
            lform = UserLoginForm()
            my_dict = {'lform':lform,'msg':msg}
            return redirect('/login/')
            # return render(request,'login.html',my_dict)
        msg = 'Pls Enter Details correctly'
        rform = UserRegistrationForm()
        my_dict = {'msg':msg,'rform':rform}
        messages.success(request, 'Please fill the form Correctly')
        return render(request,'registration.html',my_dict)


    else:
        msg='Fill all the details'
        rform = UserRegistrationForm()
        my_dict={'msg':msg,'rform':rform}
        return render(request, 'registration.html', my_dict)


def login_view(request):
    if request.method == 'POST':
        lform = UserLoginForm(request.POST)
        if lform.is_valid():
            user_email = request.POST.get('user_email')
            password1 = request.POST.get('password1')
            # request.COOKIES['email'] = user_email
            # temp = UserRegistrationData.objects.get(user_email=user_email)
            # get_id = temp.id
            #

            user_data = UserRegistrationData.objects.filter(user_email=user_email,password1=password1)
            print(user_data,"login")
            get_id = user_data[0].id
            print(get_id,"set")
            #request.COOKIES['id'] = get_id
            data = UserSellingData.objects.filter(rel_id_id=get_id)


            if user_data!=None:
                print('above return')
                msg = "Please Provide bike information"
                my_dict = {'data':data,'msg':msg}
                response = render(request,'adpost.html',my_dict)
                response.set_cookie('id',get_id)
                return response

        else:
            msg = 'Pls Enter a valid detail...'
            lform = UserLoginForm()
            my_dict = {'msg': msg, 'lform': lform}
            return render(request, 'login.html', my_dict)
    else:
        msg = 'Please Enter your details'
        lform = UserLoginForm()
        my_dict = {'lform': lform, 'msg': msg}
        return render(request, 'login.html', my_dict)


def product_desc(request):
    id_no1 = request.GET.get('id')
    id_no=int(id_no1)
    id = UserSellingData.objects.filter(product_id=id_no)
    return render(request, 'fullprodetail.html', {'id_no': id})




