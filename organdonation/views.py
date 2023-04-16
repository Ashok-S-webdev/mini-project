from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import User, Recipient, Donor


# Create your views here.

def index(request):
    users = User.objects.all()
    return render(request, 'organdonation/index.html', {users:users})


def dregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        mobile_num = request.POST['mobile_num']
        aadhaar = request.POST['aadhaar']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        addr_line = request.POST['addr_line']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        social_history = request.POST['social_history']
        medical_history = request.POST['medical_history']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.success(request, "This email is already registered with an account")
                return redirect('dregister')
            else:
                is_donor = True
                user = User.objects.create(username = first_name.lower()[0:4]+aadhaar[0:4],email = email, first_name=first_name, last_name=last_name, is_donor=is_donor)
                user.set_password(password1)
                user.save()
                donor = Donor.objects.create(user=user)
                donor.first_name = first_name
                donor.last_name = last_name
                donor.email = email
                donor.dob = dob
                donor.age = age
                donor.gender = gender
                donor.blood_group = blood_group
                donor.mobile = mobile_num
                donor.aadhaar = aadhaar
                donor.addr_line = addr_line
                donor.city = city
                donor.district = district
                donor.state = state
                donor.pincode = pincode
                donor.social_history = social_history
                donor.medical_history = medical_history
                donor.save()
                messages.success(request, "Your account has been created successfully.")
                return redirect('dlogin')

        else:
            messages.success(request, "Password and Confirm Password doesn't match.")
            return redirect('dregister')
    else:
        return render(request, 'organdonation/dregister.html')


def rregister(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        mobile_num = request.POST['mobile_num']
        aadhaar = request.POST['aadhaar']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        addr_line = request.POST['addr_line']
        city = request.POST['city']
        district = request.POST['district']
        state = request.POST['state']
        pincode = request.POST['pincode']
        organ_needed = request.POST['organ']
        medical_condition = request.POST['medical_condition']
        medical_history = request.POST['medical_history']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                person = User.objects.filter(email=email)
                for field in person:
                    temp_is_donor = field.is_donor
                    temp_is_recipient = field.is_recipient
                
                if temp_is_recipient == True:
                    pass
                messages.success(request, "This email is already registered with an account")
                return redirect('rregister')
            else:
                is_recipient = True
                user = User.objects.create(username = first_name.lower()[0:4]+aadhaar[0:4],email = email, first_name=first_name, last_name=last_name, is_recipient=is_recipient)
                user.set_password(password1)
                user.save()
                recipient = Recipient.objects.create(user=user)
                recipient.first_name = first_name
                recipient.last_name = last_name
                recipient.email = email
                recipient.dob = dob
                recipient.age = age
                recipient.gender = gender
                recipient.blood_group = blood_group
                recipient.mobile = mobile_num
                recipient.aadhaar = aadhaar
                recipient.addr_line = addr_line
                recipient.city = city
                recipient.district = district
                recipient.state = state
                recipient.pincode = pincode
                recipient.organ_needed = organ_needed
                recipient.medical_condition = medical_condition
                recipient.medical_history = medical_history
                recipient.save()
                messages.success(request, "Your account has been created successfully.")
                return redirect('rlogin')
                pass

        else:
            messages.success(request, "Password and Confirm Password doesn't match.")
            return redirect('rregister')
        
    else:
        return render(request, 'organdonation/rregister.html')

def dlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password = password)
        if user is not None and user.is_donor:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('donor_home')
        else:
            messages.success(request, 'Not valid Credentials!')
            return redirect('dlogin')
    else:
        return render(request, 'organdonation/dlogin.html', {})

def rlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password = password)
        if user is not None and user.is_recipient:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('recipient_home')
        else:
            messages.success(request, 'Not valid Credentials!')
            return redirect('rlogin')
    else:
        return render(request, 'organdonation/rlogin.html')


def dlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out Successfully')
    return redirect('index')

def rlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out Successfully')
    return redirect('index')


def donor_home(request):
    current_user = request.user
    return render(request, 'organdonation/dhome.html', {'user': current_user})

def recipient_home(request):
    current_user = request.user
    return render(request, 'organdonation/rhome.html', {'user': current_user})