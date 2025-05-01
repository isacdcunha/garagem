from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import ModeloSerializer
from core.serializers.veiculo import VeiculoSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer