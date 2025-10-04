from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'), # Movido para cima para melhor organização
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('cars/', CarsListView.as_view(), name='cars'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'), # Adicionada a barra final por consistência
]

# Esta linha é para arquivos de MÍDIA (fotos dos carros) e está CORRETA. Mantenha-a.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)