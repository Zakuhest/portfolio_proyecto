# Proyecto: 
## PortfolioDev
#
# Tipo de proyecto: 
## Individual
#
# Hecho por:
## Cristian Diaz C.
#
# Funcionalidades:
## Formulario para crear un proyecto con los siguientes campos:

- Foto (que puede ser una URL)
- Título del proyecto
- Descripción del proyecto
- Tags: HTML, CSS, PYTHON, etc
- URL de github

## Formulario de autenticación y Registro de usuarios:
- Login (admin/users/guests)
- Registro de usuarios (users)

## Registro de IP que visitan el sitio:
- Almacenados en DB: Mysql

## Detalles de proyectos:
- Visualización de cada proyecto
- Paginación
- Filtro por Tags
- Edición de proyectos que le pertenezca a cada usuario.

## Formulario para envío de correo
- Solo usuarios registrados.

## Validación de urls según tipo de permisos.
- Permisos según users y guests.
#
# Instrucciones (Sin Railway):
(Autenticación/Login y Registro, utiliza lo dado por el mismo framework Django)
- Migrar tablas a DB 
- Cargar archivo JSON a DB, que contiene Tags
- (Opcional: Cargar archivo JSON Dumpsdata)
- Invitados (Guests) solo pueden visualizar el portfolio y proyectos de todos los usuarios.
- Para la url de la foto del proyecto, se recomienda utilizar la página: https://postimages.org/es/, para convertir la imagen a url de forma gratuita.
#
# Notas:
- Función de filtros es por página visualizada, no general.
- Deploy en Railway: https://portfolioproyecto-production.up.railway.app/portfolio/

- Los usuarios pueden compartir sus proyectos una vez registrados.

- Cada usuario puede visualizar sus proyectos y editarlos. Otros usuarios no tendrán acceso a la edición de proyectos que no le pertenezcan, mucho menos si son usuarios anónimos (guests)