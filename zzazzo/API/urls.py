from django.urls import path
from . import views

urlpatterns = [
    path('', views.paymentListView.as_view()),
    path('user/<pk>/', views.userDetailApiView.as_view()),
]
