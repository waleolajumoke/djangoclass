from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact),
    path('create', views.create),
    path('delete/<int:id>', views.delete),
    path('update/<int:id>', views.update),
]