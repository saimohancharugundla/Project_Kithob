from django.urls import path
from Kitmain import views

urlpatterns = [
    path('',views.home,name='home'),
    path('products',views.products,name='products'),
    path('sell/',views.sell,name='sell'),
    
]
