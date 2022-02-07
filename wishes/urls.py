from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='test'),
    path('addition/', views.addition, name="addition"),
]
