from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.models import Planet
from .serializers import PlanetInfoSerializer, PlanetIdSerializer


# Planet and Silo Details Fragment
class PlanetInfoView(generics.ListAPIView):
    """
    Returns a list of silo details for the planet ID for the authenticated user
    """
    queryset = Planet.objects.all()
    serializer_class = PlanetInfoSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'


# List of player's planets for navigation drawer
class PlayerPlanetIdsView(generics.ListAPIView):
    """
    Returns a list of all planet IDs for the authenticated user
    """
    serializer_class = PlanetIdSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Planet.objects.filter(owner=user)

