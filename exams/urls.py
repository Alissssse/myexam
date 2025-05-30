from django.urls import path
from . import views

urlpatterns = [
    path('akxam/', views.akxam_view, name='akxam'),
] 