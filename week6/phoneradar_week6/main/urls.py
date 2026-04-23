from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brand/<int:brand_id>/', views.brand_models, name='brand_models'),
    path('model/<int:model_id>/', views.model_detail, name='model_detail'),
]