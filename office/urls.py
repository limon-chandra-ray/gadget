from django.urls import path
from . import views
app_name='office'
urlpatterns = [
    path('',views.home,name='home'),
    path('log-in',views.login_view,name='login'),
    path('login-request',views.login_request,name='login_request'),
    path('log-out',views.logout_request,name='logout'),
    path('category-list',views.category_list,name='category_list'),
    path('category-add',views.category_add,name='category_add'),
    path('category-delete-<int:id>',views.category_delete,name='category_delete'),
    path('sub-category-list',views.sub_category_list,name='sub_category_list'),
    path('sub-category-add',views.subcategory_add,name='subcategory_add'),
    path('sub-category-delete-<int:id>',views.subcategory_delete,name='subcategory_delete'),
    path('brand-list',views.brand_list,name='brand_list'),
    path('brand-add',views.brand_add,name='brand_add'),
    path('brand-delete-<int:id>',views.brand_delete,name='brand_delete'),
    path('product-list',views.product_list,name='product_list'),
    path('product-add',views.product_add,name='product_add'),
    path('user-list',views.user_list,name='user_list'),
    path('order-list',views.order_list,name='order_list'),
    path('order-status-change/<int:order_id>-<str:status>',views.order_status_change,name='order_status_change')
]