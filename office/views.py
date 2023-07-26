from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from account.models import ClientProfile
from order.models import Order
from django.forms import formset_factory
from product.models import Category,ProductBrand,SubCategory,Product,ProductImage

from .forms import ProductBrandFrom,CategoryFrom,SubCategoryFrom,ProductFrom,ProductImageFrom
from django.db.models import Count
# Create your views here.

def order_list(request):
    order = Order.objects.all().order_by('id').reverse()
    context={
        'orders':order
    }
    return render(request,'eadmin/order/order-list.html',context)

def user_list(request):
    user = ClientProfile.objects.all()
    context={
        'users':user
    }
    return render(request,'eadmin/user/list.html',context)


@login_required(redirect_field_name='office:login')
def home(request):
    product = Product.objects.count()
    users = User.objects.exclude(is_staff =False,is_superuser=False).count()
    category = Category.objects.count()
    brand = ProductBrand.objects.count()
    order = Order.objects.count()
    pending = Order.objects.filter(order_status ='PENDING').count()
    processing = Order.objects.filter(order_status ='PROCESSING').count()
    completed = Order.objects.filter(order_status ='COMPLETED').count()
    context = {
        'products':product,
        'users':users,
        'category':category,
        'brand':brand,
        'order':order,
        'pending':pending,
        'processing':processing,
        'completed':completed
    }
    return render(request,'eadmin/dashboard/index.html',context)

def login_view(request):
    return render(request,'admin/login.html')
def login_request(request):
    if request.method == "POST":
        name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_authenticated:
                return redirect('office:home')
            else:
                return redirect('office:login')
        else:
            return redirect('office:login')
# def registration(request):
#     return render(request,'admin/registration.html')

def logout_request(request):
    logout(request)
    return redirect('office:login')

# category
def category_list(request):
    category = Category.objects.all()
    context={
        'categorys':category
    }
    return render(request,'eadmin/category/list.html',context)

def category_add(request):
    form = CategoryFrom()
    if request.method == 'POST':
        form = CategoryFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form  = CategoryFrom()
    context={
        'form':form
    }
    return render(request,'eadmin/category/add.html',context)
def category_delete(request,id):
    delete = Category.objects.filter(id=id).delete()
    if delete:
        return redirect('office:category_list')
# sub category
def sub_category_list(request):
    sub_category = SubCategory.objects.all()
    context={
        'subCategorys':sub_category
    }
    return render(request,'eadmin/sub-category/list.html',context)
def subcategory_add(request):
    form = SubCategoryFrom()
    if request.method == 'POST':
        form = SubCategoryFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form  = SubCategoryFrom()
    context={
        'form':form
    }
    return render(request,'eadmin/sub-category/add.html',context)
def subcategory_delete(request,id):
    sub_category = SubCategory.objects.filter(id=id).delete()
    if sub_category:
        return redirect('office:sub_category_list')
# brand
def brand_list(request):
    brand = ProductBrand.objects.all()
    context={
        'brands':brand
    }
    return render(request,'eadmin/brand/list.html',context)
def brand_add(request):
    form = ProductBrandFrom()
    if request.method == 'POST':
        form = ProductBrandFrom(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form  = ProductBrandFrom()
    context={
        'form':form
    }
    return render(request,'eadmin/brand/add.html',context)
def brand_delete(request,id):
    brand = ProductBrand.objects.filter(id = id).delete()
    if brand:
        return redirect('office:brand_list')

# product
def product_list(request):
    product = Product.objects.all().order_by('id').reverse()
    context = {
        'products':product
    }
    return render(request,'eadmin/product/list.html',context)

def product_add(request):
    p_form =ProductFrom()
    image_form = formset_factory(ProductImageFrom,extra=4)
    image_form_set = image_form()
    if request.method == 'POST':
        p_form = ProductFrom(request.POST, request.FILES)
        image_form_set = image_form(request.POST,request.FILES)
        if p_form.is_valid() and image_form_set.is_valid():
            instance_product = p_form.save()
            for image in image_form_set:
                p_image = image.save(commit=False)
                p_image.product = instance_product
                p_image.save()
            print('some')
        else:
            print('some wrong')
    else:
        p_form =ProductFrom()
    
        image_form_set = image_form()
    context={
        'p_form':p_form,
        'i_forms':image_form_set
    }
    return render(request,'eadmin/product/add.html',context)


def order_status_change(request,order_id,status):
    order_update = Order.objects.get(id = order_id)
    if status == 'completed':
        order_update.order_status = 'COMPLETED'
    elif status == 'hold':
        order_update.order_status = 'HOLD'
    elif status == 'processing':
        order_update.order_status = 'PROCESSING'
    order_update.save()
    return redirect('office:order_list')