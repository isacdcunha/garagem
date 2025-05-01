from django.db import models

from core.models.acessorio import Acessorio
from core.models.cor import Cor
from core.models.modelo import Modelo

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos')
    acessorio = models.ManyToManyField(Acessorio, related_name='veiculos')

    def __str__(self):
        return f"({self.id}) {self.modelo} {self.cor} {self.ano}"