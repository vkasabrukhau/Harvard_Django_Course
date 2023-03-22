from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("steve", views.steve, name="steve"),
    path("bill", views.bill, name="bill"),
    path('<str:name>', views.greet, name="greet")
]