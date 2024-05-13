from django.contrib import admin
from django.urls import include, path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'index.html'),
]