from django import forms
from usuarios.models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = "__all__"