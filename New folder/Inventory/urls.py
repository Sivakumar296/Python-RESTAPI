from django.urls import path
from .views import *

urlpatterns=[
    path('products/',ProductView.as_view()),
    path('products/<int:id>/',Product_ViewById.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:id>/',CateoryGetById.as_view()),


    
]