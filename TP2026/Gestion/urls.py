from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.dashboard_admin, name='dashboard_admin'),
]