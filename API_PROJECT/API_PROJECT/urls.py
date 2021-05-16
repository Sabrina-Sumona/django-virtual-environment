from django.contrib import admin
from django.urls import path
from API_EXAMPLE import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index')
]
