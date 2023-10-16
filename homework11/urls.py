from django.contrib import admin
from django.urls import path, include  # не забудьте импортировать include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HW11.urls')),  # подключение URL-адресов приложения
]
