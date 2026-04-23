from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, DaraxtViewSet
from rest_framework.routers import DefaultRouter

r = DefaultRouter()
r.register("category", CategoryViewSet)
r.register("product", ProductViewSet)
r.register("daraxt", DaraxtViewSet)




urlpatterns = [
    path("", include(r.urls)),
]
