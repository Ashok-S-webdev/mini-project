from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import User, Recipient, Donor, Organ
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    user = request.user
    if user.is_authenticated and user.is_donor:
        return redirect('donorhome')
    elif user.is_authenticated and user.is_recipient:
        return redirect('recipienthome')
    
    return render(request, 'organdonation/index.html')


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
        form_organs = request.POST.getlist('organ')
        def_organs = ['kidney', 'liver', 'lungs', 'pancreas', 'small_intestine', 'blood']
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
                for organ in form_organs:
                    if organ in def_organs:
                        organ = Organ.objects.get(name = organ)
                        donor.organs.add(organ)
                send_mail(
                    'Registration Successful',
                    '''Thank you for registering with us.
                    Congratulations! ''' + donor.first_name + " " + donor.last_name + '''. 
                    You are now a registered donor.
                    You can now login to your account and update your profile.
                    Thank you for your support.
                    Regards,
                    Organ Donation Team''',
                    'organdonation6@gmail.com',
                    [donor.email],
                    fail_silently=False,
                )
                messages.success(request, "Your account has been created successfully.")
                return redirect('login')

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

                send_mail(
                    'Registration Successful',
                    '''Thank you for registering with us, ''' + recipient.first_name + recipient.last_name + '''. You are now a registered recipient.
                    You can now login to your account and search for the available donors.
                    Thank you for your support.
                    Regards,
                    Organ Donation Team''',
                    'organdonation6@gmail.com',
                    [recipient.email],
                    fail_silently=False,
                )
                messages.success(request, "Your account has been created successfully.")
                return redirect('login')
                pass

        else:
            messages.success(request, "Password and Confirm Password doesn't match.")
            return redirect('rregister')
        
    else:
        return render(request, 'organdonation/rregister.html')

def userlogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, email=email, password = password)
        if user is not None:
            login(request, user)
            if user.is_donor:
                return redirect('donorhome')
            elif user.is_recipient:
                return redirect('recipientprofile')
            else:
                messages.success(request, 'Error logging in.')
                logout(request)
                return redirect('login')
        else:
            messages.success(request, 'Not valid Credentials!')
            return redirect('login')
    else:
        return render(request, 'organdonation/login.html', {})


def userlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out Successfully')
    return redirect('index')


@login_required(login_url='login')
def donorhome(request):
    current_user = request.user
    if current_user.is_authenticated and current_user.is_donor:
        organlist = (current_user.donor.organs.all())
        return render(request, 'organdonation/donorhome.html', {'user': current_user, 'organslist': organlist})
    

@login_required(login_url='login')
def recipientprofileview(request):
    current_user = request.user
    if current_user.is_authenticated and current_user.is_recipient:
        return render(request, 'organdonation/recipientprofile.html', {'user': current_user})



@login_required(login_url='login')
def recipientdonorsearch(request):
    current_user = request.user
    if current_user.is_authenticated and current_user.is_recipient:
        donorlist = (Donor.objects.all())
        print(donorlist)
        if request.method == 'GET':
            bg = request.GET.get('blood_group')
            organ = request.GET.get('organ')
            location = request.GET.get('location')
            if bg != '' and organ != '' and location != '':
                donorlist = donorlist.filter(blood_group = bg, organs__name = organ, district = location)
            elif bg != '' and organ != '':
                donorlist = donorlist.filter(blood_group = bg, organs__name = organ)
            elif bg != '' and location != '':
                donorlist = donorlist.filter(blood_group = bg, district = location)
            elif organ != '' and location != '':
                donorlist = donorlist.filter(organs__name = organ, district = location)
            elif bg != '':
                donorlist = donorlist.filter(blood_group = bg)
            elif organ != '':
                donorlist = donorlist.filter(organs__name = organ)
            elif location != '':
                donorlist = donorlist.filter(district = location)
                print(donorlist)
            
        return render(request, 'organdonation/recipientdonorsearch.html', {'user': current_user, 'donorslist': donorlist})
    

