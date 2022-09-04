# Proyecto desarrollo E-commerce CoderStore
![](https://media.discordapp.net/attachments/1004393238276362365/1005986351855964250/coderhouse-logo.png?width=473&height=473 )
## Integrantes
- Lucila Werner
- Lucas Badino
- Lucas Castiglioni
---
**Requisitos** 
- Django 4.0.6
- Python 3.10
- Django-crispy-forms 1.14.0
- Pillow 9.2.0
- Virtualenv 20.16.3 (opcional)

**repo github**
[GitHub](https://github.com/lucasbadino/trabajo_1)


**Tabla de Contenidos**

Para inicializar el proyecto deberas colocar en la consola el siguiente comando:
![](https://media.discordapp.net/attachments/1004393238276362365/1005977594602201238/Screen_Shot_2022-08-07_at_7.14.04_PM.png?width=1025&height=105)


Para acceder a la Web [CoderStore](url)<!--- Ver que lo de las url de los links solo funciona si subimos el repositorio a HEROKU o uno de esos -->

1. ***Inicio***

Al ingresar a la web se visualisaran los accesos directos a las categorias de productos que ofrecemos en el Store: 

   - 1.1 Panaderia.     
   - 1.2 Bebidas.
   - 1.3 Carnes.

2.  ***La Navbar*** 

    - *"Coderstore"*: es un aceso directo a la pagina de inicio.
    - *"Productos"*: es un acceso directo a la pagina de los distintos tipos de productos.
    - *"Stock"*: es un acceso directo al al gestor de productos donde se podran editar, eliminar o crear cualquier tipo de producto. Solo va a figurar si  estas registrado como admin>

    - 1. Cuando se acceda a productos, apareceran tres accesos directos para ir a carnes, o bebidas o panaderia. <!---CAMBIE LA LINEA -->

    - *"Creacion"*: es un aceso directo a la pagina de creacion de productos en la base de datos (solo para admin).
    - *"Buscar"*: encontraras cualquier producto que este en nuestra tienda.
    - *"Contacto"*: es un formulario para poder comunicarse con la empresa CoderStore.
    - *"Login"*: podras conectarte a la sesión.
    - 1. *"Perfil"*: encontraras un desplegable:
        - A. "Mas info": podras acceder y editar la información del usuario registrado.
        - B. "Logout": desconección de la sesión.
    - *"Singup"*: registro del nuevo usuario.
    - *"Carrito de compra(logo)"*: veras todos los productos añadidos al carrito. 
<!--- Ver que lo de las url de los links solo funciona si subimos el repositorio a HEROKU o uno de esos -->
3. ***Creacion de productos***
   Se puede accedere de dos maneras por cada categoria:
    - Ingresando a la siguiente url [Carnes](url) o en la pestaña creacion- <!--- borraria lo que sigue despues de creacion. -->  carnes que la empresa pueda agregar los productos relacionados a cortes de carnes.
    - Ingresando a la siguiente url [Bebidas](url) o en la pestaña creacion- bebidas que la empresa pueda agregar los productos relacionados a tipos de bebidas.<!--- borraria lo que sigue despues de creacion. --> 
    - Ingresando a la siguiente url [Panificacion](url) o en la pestaña creacion- babidas que la empresa pueda agregar los productos relacionados a tipos de panificados.<!--- borraria lo que sigue despues de creacion. --> 

        - ![](https://media.discordapp.net/attachments/1004393238276362365/1005986750956576888/Formulario.png)

    - En cada celda de creacion podras ingresar todos los datos requeridos y automaticamente se generara un codigo aleatorio (sku) de control de inventario. <!--Si lo subimos a heroku o lo que sea el sku va a quedar fijo o va ir variando cada vez q cargemos la pagina. No deberiamos agregar el valor unique=true?-->
    
    ***El Footer***
    - *"CoderStore"*: <!--Tiene informacion acerca-->acerca de la empresa.
    - *"Productos"*: Podras acceder a nuestras categorias de productos con sus redirecciones  
    - *"Links(About us)"*:  <!--Tiene informacion acerca-->Tiene informacion acerca de la pagina y de sus fundadores.
    - *"Contacto"*:  Tiene datos de la empresa.
    ---
***Listas de tareas***
- [x] Herencia Html
- [x] Repo en [Git Hub](https://github.com/lucasbadino/trabajo_1)
- [x] 3 Clases de productos 
- [x] Forms para agregar productos DB
- [x] Form busqueda DB
- [x] Readme.md
- [x] Carrito de compras
- [x] About us
- [x] Usuarios y sus permisos
- [x] Buscador
- [x] Formulario de contacto
- [x] Plantilla de stock
-[x] Subir a Heroku o el que usemos si es q lo hacemos-->