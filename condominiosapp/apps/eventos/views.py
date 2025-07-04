from .models import Evento
from rest_framework import viewsets
from .serializer import EventoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'local', 'data', 'morador']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
