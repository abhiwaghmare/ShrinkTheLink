from django.contrib import admin
from django.urls import path
from shortner.views import index,go

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('<str:pk>',go,name='go')
]
