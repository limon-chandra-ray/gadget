from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductReview,ProductQuestion
from product.models import Product
# Create your views here.
def product_rating(request,product_id):
    user = request.user
    rating = request.POST['rate']
    comment = request.POST['comment'] 
    product = Product.objects.get(id = product_id)
    add = ProductReview.objects.create(
        user=user,
        product = product,
        review_text = comment,
        review_number = rating

    )
    if add:
        return JsonResponse({'status':'success'})
    else:
        return JsonResponse({'status':'error'})
    
def product_question(request,product_id):
    if request.user.is_authenticated:

        user = request.user
        question = request.POST['question'] 
        product = Product.objects.get(id = product_id)
        add = ProductQuestion.objects.create(
            user = user,
            product = product,
            question = question
        )
        if add:
            return JsonResponse({'status':'success'})
        else:
            return JsonResponse({'status':'error'})