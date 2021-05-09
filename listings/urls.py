from django.urls import path
from . import views

urlpatterns = [
    path('',views.listings,name='listings'),
    path('<int:pk>/',views.listing,name='listing'),
    path('search/',views.search,name='search'),
    path('cse/textbooks/',views.CSETEXTBOOKS,name='cse_tb'),
    path('cse/notebooks/',views.CSENOTEBOOKS,name='cse_nb'),
    path('cse/complete_materials/',views.CSECM,name='cse_cm'),

]
