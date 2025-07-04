from .models import AreaComum
from rest_framework import viewsets
from .serializer import AreaComumSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class AreaComumViewSet(viewsets.ModelViewSet):
    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'capacidade', 'condominio']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
