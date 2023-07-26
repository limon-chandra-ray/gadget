from django.urls import path
from . import views
app_name = 'product_info'

urlpatterns = [
    path('product-rating/<int:product_id>',views.product_rating,name='product_rating'),
    path('product-question/<int:product_id>',views.product_question,name='product_question')
]
