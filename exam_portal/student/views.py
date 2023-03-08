from django.shortcuts import render
from student.models import user_data
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user_data



def signup(request):
    if request.method == 'POST':
        # get form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        studying_year = request.POST.get('studying_year')
        dob = request.POST.get('dob')
        new = user_data(email=email, password=password, confirm_password=confirm_password,age=age, gender=gender, studying_year=studying_year, DateofBirth=dob)
        new.save()
        # TODO: validate form data and save user to database
        return render(request, 'login.html')
    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        # get form data
        email = request.POST.get('email')
        password = request.POST.get('password')
        # TODO: validate user credentials and show appropriate message
        return render(request, 'profile.html')
    return render(request, 'login.html')
def profile(request):
    # TODO: get user details from database and pass them to the template
    email = "example@email.com"
    age = 20
    gender = "Male"
    return render(request, 'profile.html', {'email': email, 'age': age, 'gender': gender})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # login user and redirect to profile page
            login(request, user)
            return redirect('profile')
        else:
            # display error message
            error_message = 'Invalid email or password.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@api_view(['post'])
def adduser(request):
    print("\nrequest:",request,"\nrequest.method:",request.method,"\nrequest.data:",request.data)
    print("\n email:",request.data["email"])
    m=user_data(email=request.data["email"],password=request.data["password"],confirm_password=request.data["confirm_password"],age=request.data["age"],gender=request.data["gender"],studying_year=request.data["studying_year"],DateofBirth=request.data["dob"])
    m.save()
    return render(request, 'login.html')

