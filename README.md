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
- Almacenados en DB.

## Detalles de proyectos:
- Visualización de cada proyecto
- Paginación
- Filtro por Tags
- Edición de proyectos

## Formulario para envío de correo
- Solo usuarios registrados

## Validación de urls según tipo de permisos.
- Permisos de admin, users y guests
#
# Instrucciones:
(Autenticación/Login y Registro, utiliza lo dado por el mismo framework Django)
- Migrar tablas a DB
- Cargar archivo JSON a DB, que contiene Tags
- Crear superuser
- (Opcional: Cargar archivo JSON Dumpsdata)
- Usuarios solo pueden visualizar portfolio y proyectos, y enviar correos al admin
- Invitados (Guests) solo pueden visualizar el portfolio y proyectos
- Administrador (admin/superuser) tiene acceso a todas las funcionalidades, incluyendo añadir y editar proyectos.
- Para la url de la foto del proyecto, se puede utilizar la página: https://postimages.org/es/, para convertir la imagen a url de forma gratuita.
#
# Notas:
- Deploy en Railway: https://portfolioproyecto-production.up.railway.app/portfolio/

- Cuenta de Administrador:

Usuario: admin

Contraseña: root

- Las siguientes cuentas registradas solo tendrán permisos de usuario.