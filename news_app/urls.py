from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('detail_page/<int:id>/', views.detail_page, name='detail_page'),
]
