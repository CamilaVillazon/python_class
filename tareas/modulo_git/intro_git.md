-------------
``git init`` inicializar repositorio
``ls -la`` para archivos ocultos
``git status`` para ver los archivos que están commited. ver estado de preparacion
``git commit -m`` para agregar mensaje e identificar versiones
``git add`` para añadir a preparación (staging area).
``git commit -a`` define el commit y añade una descripción más amplia.
``git commit --ammend -m "mensaje"`` para modificar el mensaje del commit.
``git diff``te muestra los cambios realizados. Con ``--staged`` ves los cambios guardados (solo cuando se hace commit). `head` te muestra solo el cambio
``git log`` muestra los commits que lleva con el identificador (de 40 caracteres). con ``--oneline`` se ven los mensajes que se han añadido de forma resumida. Con `-N` indica el número de commits que queremos obtener
``git status -u`` para ver el estatus que se añadieron al repositorio pero tadavia no estan controlados (todavia no tiene un add).
