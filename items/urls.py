from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'weather', views.WeatherDataViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('dashboard/', views.dashboard, name='dashboard'),
]
