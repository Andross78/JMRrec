from django.contrib import admin
from django.urls import path
from jmr import views

urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.IndexView.as_view(), name='index'),
      path('shortener/<str:key>', views.redirectView.as_view(), name='shortener'),
]