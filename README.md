# Evaluacion Practica
Este documento tiene como objectivo documentar todo el proceso realizado para la creacion del menu de opciones en la evaluacion practica. Los contenidos son
1. Ramas creadas
2. Comandos Realizados
3. Opciones de menu en el proyecto
4. Informacion del integrante del grupo

### Ramas Creadas
- Individual: Esta rama fue creada para almacenar el archivo individuales.py que contiene la resolucion hecha en phyton de la funcion que calcula la representacion en bits de un caracter individual
- Multiple: Esta rama fue creada para almacenar el archivo multiples.py que contiene la resolucion hecha en phyton de la funcion que calcula la representacion en bytes de una palabra llena de caracteres
- Representation: Esta rama fue creada para almacenar el archivo ascii.py que contiene la resolucion hecha en phyton de la funcion que calcula la representacion del caracter en sistema ASCII de un byte ingresado

### Comandos Realizados
Se utilizo la interfaz Git Bash para poder crear desde un repositorio local las distintas branches y los archivos .py vacios, leugo se hicieron la transferencia a travez de pull requests hacia el repositorio remoto que es la pagina de GitHub
- git init: Comando para inicializar github desde la interfaz
- git clone: Para clonar el repositorio remoto (se usa en conjunto con el URL del repositorio remoto)
- cd 'Test': Test es el nombre del archivo de mi repositorio local donde guardo todos los cambios hechos
- git branch: Utilizado para crear las distintas ramas mencionadas anteriormente
- git checkout: Utilizado para cambiar directamente a las ramas recien creadas
- touch: para crear los distintos archivos .py que contendran las funciones del menu de opciones
- git add: para añadir dichos archivos vacios a las ramas
- git commit -m: para guardar los cambios realizados en las ramas en donde estamos creando e ingresando el archivo
- git push: para crear un pull request que meta los cambios realizados desde el repositorio local al repositorio remoto, se hace para cada una de las ramas

A partir de aqui se modificaron los archivos y se les definio su correspondiente codigo desde el repositorio remoto GitHub

### Opciones de menu en el proyecto:
El archivo principal que es el que se encuentra en la rama 'main' es el que contiene en forma de codigo todo el menu.
1.Se muestra en pantalla las opciones que posee el menu y que el usuario puede escoger:
  - (1) Representacion caracter individual
  - (2) Representacion palabra de caracteres
  - (3) Representacion ASCII de bytes
2.A continuacion se pregunta al usuario para que digite uno de los numeros que corresponde. SI dicho numero no corresponde, simplemente se imprimira en pantalla 'opcion incorrecta'
3. Dependiendo de la opcion valida ingresada, se ejecutara las siguientes opciones
  - Si la opcion es 1, entonces se pregunta al usuario que digite un caracter individual a convertir, luego se muestra en pantalla su representacion en bits
  - Si la opcion es 2, entonces se pregunta al usuario que digite una palanra, luego se muestra en pantalla la representacion en bytes
  - Si la opcion es 3, entonces se pregunta al usuario que digite un byte, luego se muestra en pantalla la representacion ASCII

### Informacion del integrante de grupo
Este trabajo fue hecho en solitario por el estudiante Santiago Restrepo Aguilar con usuario SantiaRA en github
