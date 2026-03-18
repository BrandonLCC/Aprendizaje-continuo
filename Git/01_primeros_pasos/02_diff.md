# Uso de diff

git-diff - Muestra los cambios entre commits, commit y árbol de trabajo, etc.

Digamos que al iniciar git lo primero que queremos hacer antes de subir los cambios con git add . es ver los cambios realizados y comparar los archivos modificados.

### Descripción

Muestra los cambios entre el árbol de trabajo y el índice o un árbol, los cambios entre el índice y un árbol, los cambios entre dos árboles, los cambios resultantes de una fusión, los cambios entre dos objetos blob o los cambios entre dos archivos en el disco.

blob: un objeto que contiene un archivo (no necesariamente binario)

### Uso de diff

- Ver cambios que hiciste pero aún NO agregas al staging area

```bash

git diff 

```

- Ver un archivo en especificio

```bash

# Primero vemos que archivos estan modificados

git status

# Ver los cambios de un directorio 

git diff nombre_achivo/

# Ver los cambios de un archivo

git diff nombre_archivo

```

## Ver los cambios subidos al stage area 

- Primer comando 


```bash 

git diff --staged

```
- ver el cambio de un archivo en especifico 

```bash 

git diff --staged nombre_archivo/

```


### Referencia 

- https://www.youtube.com/watch?v=9SJDhkpuh6w

- Documentacion de git + IA
https://git-scm.com/docs/git-diff 


