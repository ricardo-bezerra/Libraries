from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from book.api import viewsets as bookviewsets

from customer.api import viewsets as customerviewsets

from user.api import viewsets as userviewsets


route = routers.DefaultRouter()


route.register(r'book', bookviewsets.BookViewset, basename='Book')

route.register(r'customer', customerviewsets.CustomerViewset, basename='Customer')

route.register(r'user', userviewsets.UserViewset, basename='User')

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include(route.urls))

]
