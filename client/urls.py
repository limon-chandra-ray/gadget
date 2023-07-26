from django.urls import path
from . import views
app_name ='client'
urlpatterns = [
    path('profile',views.profile,name='profile'),
    path('all-category',views.header_category,name='header_category'),
    path('',views.home,name='home'),
    path('log-in',views.login_view,name='login_view'),
    path('sign-up',views.signup_view,name='signup_view'),
    path('product-details-<int:product_id>',views.product_detail,name='product_detail'),
    path('card-product',views.card_product,name='card_product'),
    path('checkout',views.checkout,name='checkout'),
    path('order-complete',views.order_complete,name='order_complete'),
    path('product-add-card',views.product_add_card,name='product_add_card'),
    path('card-item-update',views.card_item_update,name='card_item_update'),
    path('product-<int:category>',views.category_product,name='category_product'),
]
