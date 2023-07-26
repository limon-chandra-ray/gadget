from itertools import count
from django.shortcuts import render,redirect
from product.models import Product,ProductImage,ProductBrand,Category
from order.models import Order,OrderItem,OrderAddress
from django.http import HttpResponseRedirect,JsonResponse
from django.db.models import Avg
from product_info.models import ProductQuestion,ProductReview
from account.forms import UserRegisterForm
from account.models import ClientProfile
import time
# Create your views here.
def profile(request):
    return render(request,'user/profile/profile.html')
def header_category(request):
    categories = Category.objects.all().values('name','id')
    return JsonResponse(list(categories),safe=False)

def home(request):
    products = Product.objects.all()
    brand = ProductBrand.objects.filter(status = True)
    category = Category.objects.filter(status=True)
    context ={
        'products':products,
        'brands':brand,
        'categories':category
    }
    return render(request,'user/home.html',context)
def login_view(request):
    return render(request,'user/auth/login.html')

def signup_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():

            form.save()
            return redirect('client:login_view')
        else:
            print(form.errors)
    else:
        form = UserRegisterForm()
        print('error')
    context = {
        'form':form
    }
    return render(request,'user/auth/registration.html',context)


def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    product_image = product.productimage_set.all()
    question = product.productquestion_set.all()
    review = product.productreview_set.all()
    avg_rating = review.aggregate(Avg('review_number'))
    min_price  = product.price - 3000
    max_price = product.price + 13000
    related_product = Product.objects.filter(price__range = (min_price,max_price)).exclude(id = product_id)
    context={
        'title':product.name,
        'product':product,
        'product_image':product_image,
        'questions':question,
        'reviews':review,
        'avg_rating':avg_rating['review_number__avg'],
        'related_product':related_product
    }
    return render(request,'user/product/product-details.html',context)


def card_product(request):
    if request.user.is_authenticated:
        user = request.user
        try:
            order = Order.objects.get(user= user,order_status="INCOMPLETED")
            order_item = order.orderitem_set.all()
            total_item = order.get_order_total_items
            total_amount = order.get_order_total_amount
        except:
            order_item=[]
            total_item = 0
            total_amount = 0
            
    else:
        order_item=[]
        total_item = 0
        total_amount = 0
    context={
        'items':order_item,
        'total_item':total_item,
        'total_amount':total_amount
    }
    return render(request,'user/order/card-product.html',context)

def checkout(request):
    if request.user.is_authenticated:
        user = request.user
        try:

            order = Order.objects.get(user= user,order_status="INCOMPLETED")
            order_item = order.orderitem_set.all()
            total_item = order.get_order_total_items
            total_amount = order.get_order_total_amount
            cleint = ClientProfile.objects.filter(user = request.user).first()
        except:
            order_item=[]
            total_item = 0
            total_amount = 0
            cleint = {}
    else:
        order_item=[]
        total_item = 0
        total_amount = 0
        cleint = {}
    context={
        'items':order_item,
        'total_item':total_item,
        'total_amount':total_amount,
        'client':cleint
    }
    return render(request,'user/order/checkout.html',context)

def product_add_card(request):
    if request.method == 'POST':
        quantity = request.POST['quantity']
        product_id = request.POST['product_id']
        user = request.user
        product = Product.objects.get(id=product_id)
        order,created = Order.objects.get_or_create(user=user,order_status='INCOMPLETED')
        orderItem,created = OrderItem.objects.get_or_create(order = order,product=product)
        orderItem.quantity = (orderItem.quantity + int(quantity))
        orderItem.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def card_item_update(request):
    item = request.POST['item']
    action = request.POST['action']
    orderitem,created = OrderItem.objects.get_or_create(id=int(item))
    if action == 'add':
        orderitem.quantity = orderitem.quantity + 1
    elif action == 'remove':
        orderitem.quantity = orderitem.quantity - 1
    orderitem.save()
    if orderitem.quantity <= 0:
        orderitem.delete()
    return JsonResponse({"status":'success'})

def order_complete(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        post_code = request.POST['post_code']
        order = Order.objects.get(user = request.user,order_status = 'INCOMPLETED' )
        order_product = order.orderitem_set.all()
        for i in order_product:
            product = Product.objects.get(id = i.product.id )
            product.quantity = product.quantity - i.quantity
            product.save()
        order.order_status = 'PENDING'
        tr_time = round(time.time()*1000)
        transaction = "#gadget" + str(order.id) + str(tr_time)
        order.transaction = transaction
        order.save()
        pick_up = OrderAddress.objects.create(
            user = request.user,
            order = order,
            full_name = first_name + " " +last_name,
            email = email,
            phone = phone_number,
            district = city,
            zip_code = post_code,
            address = address
        )
        pick_up.save()


        return redirect('account:user_order_list')
    
def category_product(request,category):
    product = Product.objects.filter(sub_category__category__id = category)
    context ={
        'products':product
    }
    return render(request,'user/product/category_product.html',context)