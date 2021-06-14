from django.contrib import admin
from django.urls import path, include

from .views import HelloworldClass, helloworldfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HelloworldClass.as_view()),# class based viewの場合は、as_view()でオブジェクト化しなければならない。
    path('', include('helloworldapp.urls')),
]
