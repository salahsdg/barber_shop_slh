from appointments import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.book_appointment, name='book'),
    path('success/', views.success, name='success'),
]
