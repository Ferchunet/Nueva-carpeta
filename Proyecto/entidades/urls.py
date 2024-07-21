from django.urls import path
from django.contrib.auth.views import LogoutView
from entidades import views

urlpatterns = [
    # Páginas principales
    path('', views.home, name="home"),
    path('home/', views.inicio, name="inicio"),
    path('acerca/', views.acerca, name="acerca"),

    # Cursos
    path('cursos/', views.cursos, name="cursos"),
    path('cursoForm/', views.cursoForm, name="cursoForm"),
    path('cursoUpdate/<int:id_curso>/', views.cursoUpdate, name="cursoUpdate"),
    path('cursoDelete/<int:id_curso>/', views.cursoDelete, name="cursoDelete"),

    # Profesores
    path('profesores/', views.listar_profesores, name='listar_profesores'),
   path('profesores/', views.profesores, name='profesores'),  # URL para la vista de profesores
    path('profesorUpdate/<int:id_profesor>/', views.profesorUpdate, name="profesorUpdate"),
    path('profesorDelete/<int:id_profesor>/', views.profesorDelete, name="profesorDelete"),
    path('profesores/asistencia/', views.registrar_asistencia_profesores, name='registrar_asistencia_profesores'),

    # Estudiantes
    path('estudiantes/', views.listar_estudiantes, name='listar_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('estudiantes/asistencia/<int:pk>/', views.registrar_asistencia, name='registrar_asistencia'),

    # Buscar
    path('buscarCursos/', views.buscarCursos, name="buscarCursos"),
    path('encontrarCursos/', views.encontrarCursos, name="encontrarCursos"),

    # Autenticación
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', views.register, name="registro"),

    # Edición de Perfil / Avatar
    path('perfil/', views.editProfile, name="perfil"),
    path('<int:pk>/password/', views.CambiarClave.as_view(), name="cambiarClave"),
    path('agregar_avatar/', views.agregarAvatar, name="agregar_avatar"),
]


