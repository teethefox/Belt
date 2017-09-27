from django.shortcuts import render, redirect
from models import *
import bcrypt
from django.db import connection, transaction
from django.contrib import messages
cursor = connection.cursor()


cursor = connection.cursor()
# Create your views here.
def index(request):
    User.objects.all()
    Destination.objects.all()
    context={
        "users":User.objects.all(),
        "destinations":Destination.objects.all()
    }
    return render(request,'index.html')
def register(request):
    errors = User.objects.validate_reg(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
        
        return redirect('/')
    else:
        hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user=User.objects.create(firstname=request.POST['firstname'], lastname=request.POST['lastname'],email=request.POST['email'], password=hash1)
        request.session['user_id']=user.id

        return redirect('/success')
def login(request):
    users = User.objects.filter(email=request.POST['email']) 
    errors = User.objects.validate_log(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
 
       

        
        return redirect('/') 
    
    if len(users) > 0:
        context = {
            'users': User.objects.filter(email=request.POST['email'])
        }

        for user in users:
            password = user.password
    user.id=user.id
    request.session['user_id'] = user.id

    return redirect('/success')
def success(request):
    User.objects.all()
    Destination.objects.all()
    a=Destination.objects.filter(id=User.objects.filter(id=request.session['user_id']))
    context={
        "user":User.objects.get(id=request.session['user_id']),
        "otherdestinations":Destination.objects.all().exclude(user_destinations=request.session['user_id']),
        "otherusers":User.objects.exclude(id=request.session['user_id']),
        "destinations":Destination.objects.filter(id=request.session['user_id'])
    }
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    return render(request,'success.html',context)
def logout(request):
    request.session.clear()
    return redirect('/')
def add(request):
    
    return render(request, 'add.html')
def submit(request):
    errors = User.objects.validate_add(request.POST)
    if len(errors):
        for field, message in errors.iteritems():
            messages.error(request, message, extra_tags=field)
 
       

        
        return redirect('/add') 
    Destination.objects.create(destination=request.POST['destination'], start=request.POST['start'], end=request.POST['end'], description=request.POST['description'])
    # All created destinations go into "other destinations" instead of "your destinations"
    return redirect('/success')
def show(request, id):
    Destination.objects.all()
    a=Destination.objects.get(id=id)
    User.objects.all()
    # b=Destination.objects.get(id=id).user_destinations
    

    context={
        "user":User.objects.get(id=request.session['user_id']),
       
        "destination": Destination.objects.get(id=id)
    #    "destinations": User.objects.get(id=b)
       
    }
    return render(request, 'show.html', context)
def join(request, id):
    # Destination.id=request.session['user_id']
    context={
    "user":User.objects.get(id=request.session['user_id']),
    "otherdestinations":Destination.objects.all().exclude(id=request.session['user_id']),
    "otherusers":User.objects.exclude(id=request.session['user_id']),
    "destinations":Destination.objects.filter(id=request.session['user_id'])
    }

    return redirect('/success', context)