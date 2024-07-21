from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True, label="Nombre de Curso")
    comision = forms.IntegerField(required=True)

class ProfesorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)   
    profesion = forms.CharField(max_length=50, required=True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="contraseña" , widget= forms.PasswordInput)
    password2 = forms.CharField(label="contraseña A CONFIRMAR" , widget= forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
       
   # En entidades/forms.py

from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        widget=forms.TextInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'email', 'fecha_nacimiento']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['asistencia', 'faltas']

from django import forms
from .models import Profesor

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_contratacion']



from django import forms
from .models import AsistenciaProfesor

class AsistenciaProfesorForm(forms.ModelForm):
    class Meta:
        model = AsistenciaProfesor
        fields = ['profesor', 'fecha', 'presente']


class UserEditForm(UserChangeForm):

    email = forms.EmailField(required=True)

    first_name = forms.CharField(label="Nombre", max_length=50, required=True)

    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

 

    class Meta:

        model = User

        fields = ["email", "first_name", "last_name"]

# core/forms.py

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)