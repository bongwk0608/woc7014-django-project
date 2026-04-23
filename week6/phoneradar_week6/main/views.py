from django.shortcuts import render, get_object_or_404
from .models import Brand, PhoneModel

def index(request):
    brands = Brand.objects.all()
    return render(request, 'index.html', {'brands': brands})


def brand_models(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    models = PhoneModel.objects.filter(brand=brand)
    return render(request, 'models.html', {
        'brand': brand,
        'models': models
    })


def model_detail(request, model_id):
    model = get_object_or_404(PhoneModel, id=model_id)
    reviews = model.review_set.all()
    newslinks = model.newslink_set.all()

    return render(request, 'detail.html', {
        'model': model,
        'reviews': reviews,
        'newslinks': newslinks
    })