from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from basic_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^basic_app/', include('basic_app.urls')),
    path('admin/', admin.site.urls),
]
