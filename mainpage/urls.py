from django.urls import path
from . import views

urlpatterns = [
	path('', views.ViewCategory.as_view())
]