from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny  # ajusta según tu auth
from .models import Cliente
from .serializers import ClienteSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    # Búsqueda y orden
    search_fields = ["nombres", "apellidos", "dni", "email", "telefono", "ciudad"]
    ordering_fields = ["id", "apellidos", "nombres", "creado_en"]
    ordering = ["apellidos", "nombres"]
