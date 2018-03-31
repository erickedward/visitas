from django import forms
from .models import Visitante
from .models import Departamento

class VisitaForm(forms.ModelForm):

	class Meta:
		model = Visitante
		fields = ('p_nombre', 's_nombre', 'p_apellido','s_apellido','cedula','direccion','telefono','dpto_visita')

class DepartamentoForm(forms.ModelForm):

	class Meta:
		model = Departamento
		fields = ('nombre_dpto','piso','descripcion')