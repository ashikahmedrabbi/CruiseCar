
from django.urls import path
from . import views

urlpatterns = [
    
    path('details/<int:id>/', views.DetailCarView.as_view(), name='detail_car_view'),
    path('buy_now/<int:car_id>/', views.buy_now, name='buy_now'),
    
]
