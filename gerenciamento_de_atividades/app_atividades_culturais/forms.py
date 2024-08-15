from django import forms
from .models import EventoCultural

class EventoCulturalForm(forms.ModelForm):
    class Meta:
        model = EventoCultural
        fields = [
            'titulo',
            'tipo',
            'data_inicio',
            'data_fim',
            'valor',
            'local',
            'horario',
            'cidade',
            'quantidade_vagas',
        ]
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-field'})
    )

    
    valor = forms.DecimalField(
        widget=forms.NumberInput(attrs={'placeholder': 'Ex: 50.00'}),
        label='Valor (Deixe em branco se for gratuito)',
        required=False,
        decimal_places=2,
        max_digits=10,
    )
    
    quantidade_vagas = forms.IntegerField(
        label='Quantidade de Vagas (Deixe em branco se ilimitadas)',
        required=False
    )

