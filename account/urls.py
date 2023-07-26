from django.urls import path
app_name = 'account'
from . import views
urlpatterns = [
    path('log-in',views.login_view,name='login_view'),
    path('login-sent',views.login_request,name='login_request'),
    path('user-add',views.registration,name='registration'),
    path('log-out',views.log_out,name='log_out'),
    path('orders',views.user_order_list,name='user_order_list'),
    path('change-password',views.change_password,name='change_password'),
    path('change-password-save',views.change_password_edit,name='change_password_save'),
    path('user-address',views.user_address_view,name='user_address'),
    path('user-address-save',views.user_address_save,name='user_address_save'),
    path('edit',views.edit_account_view,name='edit_account'),
    path('edit-account-save',views.edit_account,name='edit_account_save'),
    path('star-point',views.star_point,name='star_point'),
    path('transaction',views.transaction,name='transaction'),
]
