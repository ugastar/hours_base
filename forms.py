#Forms.py é quem faz as validações de integridades de dados#
from django import forms
from .models import Solicitar1
import datetime


class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class SolicitarForm(forms.ModelForm):
    class Meta:
        model = Solicitar1
        fields = '__all__'
        widgets = {
                    'startdate': DateTimeInput(), 'autofocus': True,
                    'endate': DateTimeInput(),
                    'justificate': forms.Textarea(attrs={'placeholder': 'Informe a justificativa.'}),
                  }





