from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AsistenciaProfesor, Avatar, Estudiante
from .forms import AvatarForm, CursoForm, ProfesorForm, RegistroForm, UserEditForm
from django.contrib.auth.decorators import login_required 
from .forms import AsistenciaForm 
from .forms import RegistroForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render
from .models import Curso         
 User = get_user_model()
from django.shortcuts import render
from .models import AsistenciaProfesor, Avatar, Estudiante, Profesor

def profesores(request):
    profesores_list = Profesor.objects.all()
    return render(request, 'profesores_list.html', {'profesores': profesores_list})

def inicio(request):
    return render(request, "entidades/index.html")

def seguimiento(request):
    return render(request, 'entidades/seguimiento.html')

def home(request):
    contexto = {"inicio": Estudiante.objects.all()}
    return render(request, "entidades/home.html", contexto)


def acerca(request):
    return render(request, "entidades/acerca.html")

def profesores(request):
    profesores_list = Profesor.objects.all()
    return render(request, 'core/profesores.html', {'profesores': profesores_list})


# Cursos
@login_required
def cursos(request):
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

def cursoForm(request):
    if request.method == "POST":
        miForm = CursoForm(request.POST)
        if miForm.is_valid():
            curso_nombre = miForm.cleaned_data.get("nombre")
            curso_comision = miForm.cleaned_data.get("comision")
            curso = Curso(nombre=curso_nombre, comision=curso_comision)
            curso.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        miForm = CursoForm()

    return render(request, "entidades/cursoForm.html", {"form": miForm})

@login_required
def cursoUpdate(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    if request.method == "POST":
        miForm = CursoForm(request.POST, instance=curso)
        if miForm.is_valid():
            miForm.save()
            contexto = {"cursos": Curso.objects.all()}
            return render(request, "entidades/cursos.html", contexto)
    else:
        miForm = CursoForm(instance=curso)

    return render(request, "entidades/cursoForm.html", {"form": miForm})

@login_required
def cursoDelete(request, id_curso):
    curso = Curso.objects.get(id=id_curso)
    curso.delete()
    contexto = {"cursos": Curso.objects.all()}
    return render(request, "entidades/cursos.html", contexto)

# Profesores
@login_required
def profesores(request):
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)
from django.shortcuts import render, redirect
from .forms import ProfesorForm


def profesorForm(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            # Extraer los datos del formulario
            nombre = miForm.cleaned_data['nombre']
            apellido = miForm.cleaned_data['apellido']
            email = miForm.cleaned_data['email']
            telefono = miForm.cleaned_data['telefono']
            fecha_contratacion = miForm.cleaned_data['fecha_contratacion']
            
            # Crear y guardar una nueva instancia del modelo
            Profesor.objects.create(
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                fecha_contratacion=fecha_contratacion
            )
            
            # Redirigir a la página de listado de profesores
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm()
    
    return render(request, "entidades/profesorForm.html", {"form": miForm})

@login_required
def profesorUpdate(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST, instance=profesor)
        if miForm.is_valid():
            miForm.save()
            contexto = {"profesores": Profesor.objects.all()}
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm(instance=profesor)

    return render(request, "entidades/profesorForm.html", {"form": miForm})

@login_required
def profesorDelete(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all()}
    return render(request, "entidades/profesores.html", contexto)

# Estudiantes
class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante

class EstudianteCreate(LoginRequiredMixin, CreateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")

class EstudianteUpdate(LoginRequiredMixin, UpdateView):
    model = Estudiante
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("estudiantes")

class EstudianteDelete(LoginRequiredMixin, DeleteView):
    model = Estudiante
    success_url = reverse_lazy("estudiantes")

# Buscar información
def buscarCursos(request):
    return render(request, "entidades/buscar.html")

def encontrarCursos(request):
    if request.GET.get("buscar"):
        patron = request.GET.get("buscar")
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {'cursos': cursos}
    else:
        contexto = {'cursos': Curso.objects.all()}

    return render(request, "entidades/cursos.html", contexto)
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect("inicio")
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm})

# Seguimiento de estudiantes y asistencia

from django.shortcuts import render, get_object_or_404, redirect
from .models import Curso, Estudiante, Profesor
from .forms import EstudianteForm, AsistenciaForm

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'entidades/listar_estudiantes.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'entidades/agregar_estudiante.html', {'form': form, 'view_title': 'Agregar Estudiante'})

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'entidades/agregar_estudiante.html', {'form': form, 'view_title': 'Editar Estudiante'})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('listar_estudiantes')
    return render(request, 'entidades/eliminar_estudiante.html', {'estudiante': estudiante})

def registrar_asistencia(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = AsistenciaForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('listar_estudiantes')
    else:
        form = AsistenciaForm(instance=estudiante)
    return render(request, 'entidades/registrar_asistencia.html', {'form': form, 'estudiante': estudiante})

from django.shortcuts import render, redirect
from .forms import AsistenciaProfesorForm




from django.shortcuts import render, redirect
from .forms import AsistenciaProfesorForm

def registrar_asistencia_profesores(request):
    if request.method == 'POST':
        form = AsistenciaProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profesores')
    else:
        form = AsistenciaProfesorForm()
    return render(request, 'entidades/asistencia_profesores.html', {'form': form})
# core/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Profesor, AsistenciaProfesor
from .forms import AsistenciaProfesorForm

def listar_profesores(request):
    profesores = Profesor.objects.all()
    asistencia_data = []

    for profesor in profesores:
        asistencias = AsistenciaProfesor.objects.filter(profesor=profesor, presente=True).count()
        faltas = AsistenciaProfesor.objects.filter(profesor=profesor, presente=False).count()
        asistencia_data.append({
            'profesor': profesor,
            'asistencias': asistencias,
            'faltas': faltas,
        })

    contexto = {
        'asistencia_data': asistencia_data,
    }
    return render(request, 'entidades/profesores.html', contexto)
# En views.py


#edicion del perfil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserEditForm

@login_required
# ____ Edición de Perfil / Avatar

 

@login_required
# ____ Edición de Perfil / Avatar

 

@login_required

def editProfile(request):

    usuario = request.user

    if request.method == "POST":

        miForm = UserEditForm(request.POST)

        if miForm.is_valid():

            user = User.objects.get(username=usuario)

            user.email = miForm.cleaned_data.get("email")

            user.first_name = miForm.cleaned_data.get("first_name")

            user.last_name = miForm.cleaned_data.get("last_name")

            user.save()

            return redirect(reverse_lazy("home"))

    else:

        miForm = UserEditForm(instance=usuario)

    return render(request, "entidades/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "entidades/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "entidades/agregarAvatar.html", {"form": miForm})    

# views.py

from django.shortcuts import render

def some_view(request):
    from .models import Estudiante, Avatar  # Delayed import
    estudiantes = Estudiante.objects.all()
    # Other view logic
# entidades/views.py
def profesorForm(request):
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profe_nombre = miForm.cleaned_data.get("nombre")
            profe_apellido = miForm.cleaned_data.get("apellido")
            profe_email = miForm.cleaned_data.get("email")
            profe_profesion = miForm.cleaned_data.get("profesion")

            profesor = Profesor(nombre=profe_nombre, 
                          apellido=profe_apellido,
                          email=profe_email,
                          profesion=profe_profesion)
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm()
    
    return render(request, "entidades/profesorForm.html", {"form": miForm})
def profesorUpdate(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    if request.method == "POST":
        miForm = ProfesorForm(request.POST)
        if miForm.is_valid():
            profesor.nombre = miForm.cleaned_data.get("nombre")
            profesor.apellido = miForm.cleaned_data.get("apellido")
            profesor.email = miForm.cleaned_data.get("email")
            profesor.profesion = miForm.cleaned_data.get("profesion")
            profesor.save()
            contexto = {"profesores": Profesor.objects.all() }
            return render(request, "entidades/profesores.html", contexto)
    else:
        miForm = ProfesorForm(initial={"nombre": profesor.nombre,
                                       "apellido": profesor.apellido,
                                       "email": profesor.email,
                                       "profesion": profesor.profesion})
    
    return render(request, "entidades/profesorForm.html", {"form": miForm})

def profesorDelete(request, id_profesor):
    profesor = Profesor.objects.get(id=id_profesor)
    profesor.delete()
    contexto = {"profesores": Profesor.objects.all() }
    return render(request, "entidades/profesores.html", contexto)     



from entidades.models import Curso


cursos_sin_comision = Curso.objects.filter(comision__isnull=True)

for curso in cursos_sin_comision:
    curso.comision = 0  
    curso.save()
