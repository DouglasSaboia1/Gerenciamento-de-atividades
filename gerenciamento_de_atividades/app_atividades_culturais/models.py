from django.db import models

class EventoCultural(models.Model):
    TIPO_EVENTO_CHOICES = [
        ('show', 'Show'),
        ('teatro', 'Apresentação Teatral'),
        ('orquestra', 'Orquestra'),
        ('musical', 'Musical'),
        ('humor', 'Show de Humor'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50, choices=TIPO_EVENTO_CHOICES)
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    local = models.CharField(max_length=100)
    horario = models.TimeField()
    cidade = models.CharField(max_length=100)
    quantidade_vagas = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.titulo
