
#=============================PROJECT 3========================================
#==========================WEB PROGRAMMING========================
#=========================NAME: JONNATHAN FABRICIO CRESPO YAGUANA=============
#==========================DATE: DECEMBER 2019=================================


# Project 3

El presente trabajo contiene el codigo para el curso *CS50 Web Programming with Python and JavaScript* implementando el proyecto número 3 *Pizza* usando principalmente Django.

## Estructura de Archivos

According to the specifications of Django this repository contains one main directory for the whole *Pizza* Django Project as well as one directory for each of the two Django Apps: *Orders* and *Users*

Siguiendo las instrucciones del proyecto el repositorio contiene el proyecto en la ruta *Pizza* con las dos aplicaciones necesarias: *Orders* y *Users*

### Pizza

Cambios realizados en el proyecto

* *settings.py*: Como una caracteristica adicional se ha agregado la libreria  *Crispy Forms* para realizar *forms* de una manera mas dinamica.

* *urls.py*: Actualizacion de las rutas en las diferentes aplicaciones *Orders* and *Users*.

### Orders


La aplicación *Orders* contiene la implementación del Menu y el proceso de pedidos de usuarios. Contiene toda la informacion necesaria de la aplicacion a excepción del Inicio de sesión y Registro.

In the templates directory one can find the main layout template which is then extended by the templates for the Menu / Index page (index.html), the Shopping Cart page (cart.html), the Adding Item page (add.html) and the Order overview (orderlist.html).

Se han creado los siguientes modelos (la informacion de estos modelos se encuentra en el archivo *db.sql*)

* *MenuItem*: Contiene los items del menu como Small Regular Pizza y precio.
* *Topping*: Toppings que pueden ser añadidos a la pizza.
* *Extras*: Item que pueden ser añadidos al producto. Actualmente Extra Cheese para los Suvs y Onions. La relacion que se ha implementado es Many to May, porque cada item del menu puede tener varios extras.

* *OrderItem*: Item que el usuario a seleccionado dentro de una order. COtiene una ForeignKey para MenuItem tambien un campo Many to Many relationships con los toppings y extras añadidos.

* *Order*: Una order contiene todas los items que se han añadido a una orden de usuario. La ordern puede tener tres estados dependiendo de los usuarios del sistema (Open (Carrito de compras), Pending (En espera), Completed (Orden realizada),Canceled(Cancelación del usuario))



### Users

Para la parte *User* se integró el índice de la aplicación con el login y register, para mejorar los templates de *form* se ha usado *Crispy Forms* el cual es una opción disponible de Django. 

## Personal Touch / View and Cancel Orders

EL toque adicional que se ha implementado es que los usuarios pueden ver el estado de sus ordenes: Open, Completed y Canceled. Para esto se ha habilitado en el usuario la opcion de cancelar la ordern en el *carrito de compras*.

