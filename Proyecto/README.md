# Gestión Musical

**Gestión Musical** es una aplicación web desarrollada en Django para la administración de una escuela musical. El sistema incluye funcionalidades para gestionar usuarios, profesores, estudiantes, cursos y más.

## Índice

1. [Instalación](#instalación)
2. [Configuración](#configuración)
3. [Uso](#uso)
4. [Rutas](#rutas)
5. [Pruebas](#pruebas)
6. [Contribuciones](#contribuciones)
7. [Licencia](#licencia)

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```

2. **Instalar las dependencias:**

    Navega al directorio del proyecto y crea un entorno virtual:

    ```bash
    cd nombre_del_proyecto
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

    Luego, instala las dependencias desde `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configurar la base de datos:**

    Asegúrate de tener configurada la base de datos en el archivo `settings.py`. Luego, realiza las migraciones necesarias:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Crear un superusuario (opcional):**

    ```bash
    python manage.py createsuperuser
    ```

5. **Ejecutar el servidor:**

    ```bash
    python manage.py runserver
    ```

## Configuración

El archivo de configuración `settings.py` incluye configuraciones básicas para la base de datos, archivos estáticos y plantillas. Asegúrate de ajustar estos valores según tus necesidades.

## Uso

- **Página principal:** `http://localhost:8000/`
- **Página de inicio:** `http://localhost:8000/home/`
- **Acerca de:** `http://localhost:8000/acerca/`

## Rutas

### Cursos
- **Lista de cursos:** `http://localhost:8000/cursos/`
- **Formulario de curso:** `http://localhost:8000/cursoForm/`
- **Actualizar curso:** `http://localhost:8000/cursoUpdate/<id_curso>/`
- **Eliminar curso:** `http://localhost:8000/cursoDelete/<id_curso>/`

### Profesores
- **Lista de profesores:** `http://localhost:8000/profesores/`
- **Actualizar profesor:** `http://localhost:8000/profesorUpdate/<id_profesor>/`
- **Eliminar profesor:** `http://localhost:8000/profesorDelete/<id_profesor>/`
- **Registrar asistencia de profesores:** `http://localhost:8000/profesores/asistencia/`

### Estudiantes
- **Lista de estudiantes:** `http://localhost:8000/estudiantes/`
- **Agregar estudiante:** `http://localhost:8000/estudiantes/agregar/`
- **Editar estudiante:** `http://localhost:8000/estudiantes/editar/<pk>/`
- **Eliminar estudiante:** `http://localhost:8000/estudiantes/eliminar/<pk>/`
- **Registrar asistencia de estudiantes:** `http://localhost:8000/estudiantes/asistencia/<pk>/`

### Buscar
- **Buscar cursos:** `http://localhost:8000/buscarCursos/`

### Autenticación
- **Iniciar sesión:** `http://localhost:8000/login/`
- **Cerrar sesión:** `http://localhost:8000/logout/`
- **Registro:** `http://localhost:8000/registro/`

### Edición de Perfil / Avatar
- **Perfil:** `http://localhost:8000/perfil/`
- **Cambiar contraseña:** `http://localhost:8000/<pk>/password/`
- **Agregar avatar:** `http://localhost:8000/agregar_avatar/`

## Pruebas

Los casos de prueba se encuentran en el directorio `tests` dentro de cada aplicación. Para ejecutar las pruebas, usa:

```bash
python manage.py test
