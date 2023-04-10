from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm,bookingdetailsform,contactdetailsform,restdetailsform
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from restapp.models import bookingdetails,contactdetails,restdetails

# Create your views here.

def index(request):
    contform = contactdetailsform()
    if request.method =='POST':
        contform = contactdetailsform(request.POST)
        if contform.is_valid():
            contform.save()
            messages.success(request,'Confirmed Your Request')
            return redirect('index')
    else:
        contform = contactdetailsform()

    return render(request,'index.html',{'contform':contform})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'Account is created')
                return redirect('index')
            except:
                pass

    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def Login(request):
    #  if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']

    #     user = authenticate(username=username, password=password)

    #     if user is not None:
    #         if user.is_staff == True:
    #             return redirect('ownerhome')
    #         else:
    #             form =login(request,user)
    #             messages.success(request,f'welcome {username} !!')
    #             return redirect('userhome')
    #     else:
    #         messages.info(request, 'invalid username and password')
    #         return redirect('login')
       
    #  else:
    #     return render(request,'Login.html')
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None:
            if user.is_staff == True:
                return redirect('ownerhome')
            else:
                form = login(request,user)
                messages.success(request,f'welcome {username} !!')
                return redirect('userhome') 
        else:
            messages.info(request,'account done not exit plz sign in')
            
    form = AuthenticationForm()
    return render(request,'Login.html',{'form':form})


@login_required()
def userhome(request):
    form1 = bookingdetailsform()
    if request.method == 'POST':
        form1 = bookingdetailsform(request.POST)
        if form1.is_valid:
            try:
                profile = form1.save(commit=False)
                profile.user = request.user
                profile.save()
                # form1.save()
                messages.success(request,'Your booking is pending!!!  Check your Email or SMS for conformation')
                return redirect('userhome')
            except:
                pass
    else:
        form1 = bookingdetailsform()


    return render(request,'userhome.html',{'form1':form1})


def ownerhome(request):
    return render(request,'ownerhome.html')

def bookingstatus(request):

    booking = bookingdetails.objects.all()
    
    return render(request,'bookingstatus.html',{'booking':booking})

def bookingstatus_for_user(request):

    cont1 = restdetails.objects.all()

    return render(request,'bookingstatus-user.html',{'cont1':cont1})


def contact(request):

    cont = contactdetails.objects.all()

    return render(request,'contact.html',{'cont':cont})

def delete(request,id):
    booking = bookingdetails.objects.get(id=id)
    booking.delete()
    return redirect('/bookingstatus')

def delete1(request,id):
    cont = contactdetails.objects.get(id=id)
    cont.delete()
    return redirect('/contact')

def Details(request):
    contform = restdetailsform()
    if request.method =='POST':
        contform = restdetailsform(request.POST)
        if contform.is_valid():
            contform.save()
            messages.success(request,'Confirmed Your Request')
            return redirect('Details')
    else:
        contform = restdetailsform()
    return render(request,'Details.html',{'contform' : contform})

def Addrestdetails(request):

    cont1 = restdetails.objects.all()

    return render(request,'Addrestdetails.html',{'cont1':cont1})

def delete2(request,id):
    cont = restdetails.objects.get(id=id)
    cont.delete()
    return redirect('/Addrestdetails')


def edit(request,id):

    rest = restdetails.objects.get(id=id)

    return render(request,'editdetails.html',{'rest':rest})

def update(request,id):
    rest = restdetails.objects.get(id=id)
    if request.method == 'POST':
        special = request.POST['special']
        opentime = request.POST['opentime']
        closetime = request.POST['closetime']
        print("-------------------------------------", special, opentime, closetime)
        rest.special = special
        rest.opentime = opentime
        rest.closetime = closetime
        rest.save()
        return redirect("Addrestdetails")

    return render(request,"editdetails.html",{'rest':rest})



