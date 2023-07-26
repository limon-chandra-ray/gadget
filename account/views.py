from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import UserRegisterForm,ClientProfileForm
from .models import ClientProfile
from order.models import Order,OrderItem,OrderAddress
# Create your views here.
def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if(password == repassword):
            add_success =User.objects.create_user(username=username,
                                                  email=email,
                                                  password=repassword,
                                                  is_staff = False,
                                                  is_superuser = True,is_admin=False)
            add_success.save()
            if add_success:
                return redirect('client:login_view')
        
    return redirect('client:signup_view')
def login_view(request):
    return render(request,'user/auth/login.html')
def login_request(request):
    if request.method == "POST":
        name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_authenticated:
                return redirect('client:home')
            else:
                return redirect('account:login_view')
        else:
            return redirect('account:login_view')
def log_out(request):
    logout(request)
    return redirect("client:home")
def user_order_list(request):
    order = Order.objects.exclude(order_status = 'INCOMPLETED').filter(user = request.user)
    order_items = []
    for o in order:
        order_items.append(o.orderitem_set.all())
    print(order_items)
    context={
        'orders':order,

    }
    return render(request,'user/profile/order.html',context)


def change_password(request):
    return render(request,'user/profile/change-password.html')
def change_password_edit(request):
    if request.method == 'POST':
        password  = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            user= User.objects.get(id = request.user.id)
            user.set_password(repassword)
            user.save()
            user_login = authenticate(request,username=user.username,password=repassword)
            if user_login is not None:
                login(request,user_login)
                if request.user.is_authenticated:
                    return redirect('client:profile')
        else:
            return redirect('account:change_password')
def user_address_view(request):
    client = ClientProfile.objects.get(user = request.user)
    context={
        'client':client
    }
    return render(request,'user/profile/address.html',context)

def user_address_save(request):
    if request.method == 'POST':
        client = ClientProfile.objects.get(user = request.user)
        client.address = request.POST['address']
        client.city = request.POST['city']
        client.post_code = request.POST['post_code']
        client.save()
        return redirect('account:user_address')

def edit_account_view(request):
    client = ClientProfile.objects.get(user = request.user)
    context ={
        'client':client
    }
    return render(request,'user/profile/edit-account.html',context)
def edit_account(request):
    
    if request.method == 'POST':
        user = User.objects.get(id = request.user.id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        client = ClientProfile.objects.filter(user=request.user).first()
        client.phone_number = request.POST['phone_number']
        client.save()
    return redirect('account:edit_account')

def star_point(request):
    return render(request,'user/profile/star-point.html')

def transaction(request):
    return render(request,'user/profile/transactions.html')