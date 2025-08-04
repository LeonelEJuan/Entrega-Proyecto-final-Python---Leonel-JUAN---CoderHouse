# Entrega-Proyecto-final-Python---Leonel-JUAN---CoderHouse
Proyecto: Plataforma/Blog web de reclutamiento "Innova Talent" 

 Objetivo del proyecto
Crear una aplicación web que permita a CEOs o empresas:

Registrarse e iniciar sesión.

Acceder a un panel de control personalizado.

Enviar formularios solicitando perfiles IT.

Crear y gestionar publicaciones estilo blog.

Visualizar solicitudes recibidas desde el panel de administración.

Al mismo tiempo, mantener una estética moderna y una navegación clara, con un landing page inicial que inspire confianza y profesionalismo.

Tecnologías utilizadas
Lenguaje: Python 3.x

Framework: Django

Base de datos: SQLite (por defecto)

Frontend: HTML, CSS embebido, plantillas Django

Entorno de desarrollo: Visual Studio Code

Autenticación: Sistema de usuarios de Django

Hosting local: runserver en entorno virtual

 Estructura principal de la app
blog_project/ – Proyecto principal (configuración)

core/ – App que contiene vistas, modelos, formularios y templates

templates/core/ – HTMLs con la UI (base, login, registro, dashboard, blog, etc.)

 Pasos clave del desarrollo
1. Configuración inicial
Crear entorno virtual y activarlo.

Instalar Django con pip install django.

Crear proyecto blog_project y app core.

Configurar settings.py (app instalada, templates, base de datos, autenticación).

2. Autenticación
Se usaron las vistas genéricas de Django (LoginView, LogoutView) para manejo de sesiones.

Se creó un modelo de CEO personalizado con campos adicionales como empresa y cargo.

3. Panel del usuario
Vista protegida (@login_required) que muestra datos del usuario logueado.

Se accede desde el menú desplegable de usuario.

4. Blog
Modelo Page con título, contenido, autor y fecha.

Formularios y vistas para crear, editar, eliminar y ver publicaciones.

Se muestra lista de posts en la página principal o en un botón llamado “Blog”.

5. Formulario de reclutamiento
Formulario para que el CEO solicite perfiles IT.

Se guarda con relación al usuario y se puede visualizar desde el panel de admin o desde una URL protegida.

6. Frontend y diseño
Se diseñó un base.html con estilo moderno (header, nav, dropdown de usuario, y footer).

Todas las vistas extienden esta base.

Se agregó un botón en el pie de página que enlaza a un sitio externo de contacto (sites.google.com/...).

7. Vista de formularios recibidos
Vista protegida para ver todas las solicitudes de reclutamiento recibidas.

Útil para uso interno del equipo de recursos humanos o administración.

 Características destacadas
 Diseño responsive simple, sin necesidad de librerías externas.

Se protege todo lo sensible con @login_required.

 Diferencia entre usuarios normales y superusuarios para ver el panel de admin.

 Posibilidad de exportar, revisar y analizar las solicitudes entrantes.
