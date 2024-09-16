from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import SignupForm, LoginForm
from .models import UserDetails
from .serializers import UserDetailsSerializer
import json

# Create your views here.

def hello_world(request):
    return HttpResponse("Hello, world!")

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful. Please log in.")
            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'Loginify/signup.html', {'form': form})

def login_view(request):
    if request.session.get('username'):
        return JsonResponse({'success': True,'message':f"Username: {request.session.get('username')} is already logged in."})
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = UserDetails.objects.get(email=email, password=password)
                request.session.set_expiry(5)
                request.session['username'] = user.username
                return redirect('success')  
            except UserDetails.DoesNotExist:
                return JsonResponse({'success': False,"message":"Invalid credentials"})
    else:
        form = LoginForm()
    return render(request, 'Loginify/login.html', {'form': form})
    
def success_view(request):
    return render(request, 'Loginify/success.html')

@csrf_exempt
def get_all_data(request):
    if request.method == 'GET':
        try:
            all_users=UserDetails.objects.all() 
            serializer_data=UserDetailsSerializer(all_users,many=True)
            return JsonResponse(serializer_data.data, safe=False)
        except Exception as e:
            return JsonResponse({"error":str(e)})

@csrf_exempt
def single_user_data(request, email):
    if request.method == 'GET':
        try:
            user_data=UserDetails.objects.get(email=email)
            serializer_data=UserDetailsSerializer(user_data)
            return JsonResponse(serializer_data.data, safe=False)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
    
    if request.method == 'PUT':
        try:
            user_data=UserDetails.objects.get(email=email)
            input_data=json.loads(request.body)
            serializer_data=UserDetailsSerializer(user_data,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data Updated Successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        
    if request.method == 'PATCH':
        try:
            user_data=UserDetails.objects.get(email=email)
            input_data=json.loads(request.body)
            serializer_data=UserDetailsSerializer(user_data,data=input_data,partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({"message":"Data Updated Successfully"},status=200)
            else:
                return JsonResponse(serializer_data.errors,status=400)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)
        
    if request.method == 'DELETE':
        try:
            user_data=UserDetails.objects.get(email=email)
            user_data.delete()
            return JsonResponse({"message":"Data deleted Successfully"},status=204)
        except UserDetails.DoesNotExist:
            return JsonResponse({"error":"User not found"},status=404)