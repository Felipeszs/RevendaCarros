from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarCreateView, CarDetailView, CarUptadeView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('cars/', CarsListView.as_view(), name='cars'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update', CarUptadeView.as_view(), name='car_uptade'),
    path('car/<int:pk>/delete', CarDeleteView.as_view(), name='car_delete'),
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),
    path('', CarsListView.as_view(), name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)