from django.urls import path
from .api import PlanetInfoView

urlpatterns = [
    # Your other URL patterns here
    path('api/planet-info/', PlanetInfoView.as_view(), name='planet-info'),
]
