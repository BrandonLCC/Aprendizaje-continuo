# Uso de rebase con git

## Escenario

Antes de empezar, asumir que pueden existir diferentes escenarios y problemas para aplicar un solo comando.

- En este caso, cuando utilizamos una rama llamada `bugfix/unsupervised-pipeline` esta contiene **13 cambios hacia atras**, esto quiere decir que tiene 13 cambios (commits) no aplicados a la rama main. 

- Tambien, esta rama contiene **2 cambios hacia adelante**, osea que esta rama se mantiene desactualizada?

Desde nuestro entorno local nosotros pensariamos que al hacer `push` para subir los cambios y luego merge en el github fusionamos la  rama con sus cambios al `main`  mantendriamos actualizado el proyecto desde el remoto. 

Pero, **¿Por qué se mantendria una rama desactualizada?**

![Instalación de Node.js](./img\escenario-rebase\1-img-cambios-adelante-atras.png)

**Vista localmente** 

Desde nuestro proyecto o **entorno local** nosotros hacemos el flujo normal, desde git status, git add . hasta un git push.

¿desde aqui todo bien? hacemos el pull request desde el github para aceptar los cambios y hacer merge. 

Desde nuestra visualización notaremos que los cambios estan todo ok, pero nos falta algo, una mala practica...

### Rama 1 `main`

- Rama main o rama principal que contiene todos los cambios y cambios de ramas fusionadas

- **Commit totales:** 103 

![rama-principal](.//img/escenario-rebase/2-img-rama-main-.png)

### Rama 2: `bugfix/unsupervised-pipeline`

- rama que contiene cambios que no se han fusionado con la rama `main`

- rama que contiene 13 cambios hacia atras porque ... 
y 2 cambios que no...

- **Commit totales:** 113 (Si tiene **muchos** cambios faltantes que en main Puede ser un problema) no es problema en x circunstancias.

![rama-2](.//img/escenario-rebase/3.1-img-rama-unsupervised-part-2.png)


## ¿Por qué ocurre? 

Significa simplemente que las dos ramas evolucionaron en paralelo.


En algún momento tenías algo así:

```
A---B---C  main
         \
          D---E---F  feature
```

Hasta ahí todo bien.

Pero después alguien (o tú mismo) agregó commits en main:

```
A---B---C---G---H   main
         \
          D---E---F---I---J---K...   feature
```

Entonces ahora Git compara:

Tu rama feature

tiene 13 commits que main no tiene

main

tiene 2 commits que tu rama no tiene

Por eso GitHub dice:

ahead 13
behind 2


Cuándo ocurre más seguido

Pasa mucho cuando:

1️⃣ Creas una rama

git checkout -b feature

2️⃣ Trabajas varios commits

commit
commit
commit

3️⃣ Mientras tanto alguien hace push a main.

## Solución 

Es normal cuando:

trabajas en una rama feature

mientras tanto main sigue recibiendo cambios


----

Cómo se arregla

Hay dos estrategias.

1️. Merge (más simple)
```bash
git checkout feature
git merge main
```

Resultado:

```
A---B---C---G---H
         \      \
          D---E---F---I---J---M
```

2️. Rebase (más limpio)

```bash
git checkout feature
git rebase main
```

Resultado:
```
A---B---C---G---H---D'---E'---F'---I'---J'
```

Tu trabajo queda encima del main actualizado.

En equipos profesionales

La mayoría de equipos usan:

- rebase antes del merge

para mantener el historial limpio.

## **Uso de rebase**

```bash
# Opción 1 (común)
#  Traer cambios de main a tu rama

git checkout main
git merge feature

# Opción 2 (flujo moderno)
# Integrar tu rama a main

git checkout feature
git rebase main
```
### Antes de 

- Primero actualizar el proyecto local siempre y luego ubicarnos a la rama en la que queremos subir los cambios a main

```bash
# Primero te aseguras de que main esté actualizado.
git checkout main
# Opcion 1: pull actualiza y fusiona todos los cambios
git pull 

# Opcion 2: no mezcla los codigos directamente

git fetch

# Luego vuelves a tu rama de trabajo:

git checkout bugfix/pipeline-unsupervised
```

### Paso 1 - Inició con rebase

```bash
# significa: “Reaplica mis commits encima del main.
git rebase main
```

### Paso 2 - Git detecta conflictos

- Esto es asi, se detecta el archivo que tiene conflicto entre las ramas

```bash
CONFLICT (content): Merge conflict in README.md
error: could not apply 6ef7ce7
```

![rama-principal](.//img/escenario-rebase/5-img-error-rebase-a-main.png)

- Cuando estamos en la rama nos aparecera en al lado del nombre de la rama un texto que dice "REBASE 1/7". Esto significa que hay 7 commits que tenemos que verificar y soluciónar en caso de conflictos.

![rama-principal](.//img/escenario-rebase/4.rebase-1-de-7.png)

### PASO 3 - Ver archivos con conflicto

- Ver el estado del conflicto

```bash
git status

# Respuesta del status: Eso indica que ese archivo tiene conflicto.
both modified: README.md
```

### PASO 4 - Abrir el archivo y resolver conflicto
- Agregar conflicto como resuelto 
```bash
<<<<<<< HEAD
contenido que viene desde main
=======
contenido de tu commit
>>>>>>> 6ef7ce7
```
### PASO 5 - Marcar conflicto como resuelto
```bash
git add README.md
```
### PASO 6 - Continuar el rebase (soluciónar los otros commits)

```bash
# al pasar el siguiente rebase pasara a 2/7 y asi ..
git rebase --continue
```
En la siguiente imagen, luego del `git rebase --continue` se puede:

1. Salir par continuar con los cambios
```bash
Esc <-- Presiona el boton de escape
:wq <-- escribe en la terminal esto
Enter <-- Presiona el boton de Enter
```
2. Entrar en modo editor con "i" para editar algun mensaje y luego salir.

![rama-principal](.//img/escenario-rebase/6-rebase--continue.png)


### PASO 7 — Terminar el rebase

Cuando Git termine todos los commits verás algo como:
```bash

Successfully rebased and updated refs/heads/bugfix/pipeline-unsupervised
```
### PASO 8 — Subir los cambios

Como el rebase reescribe el historial, debes hacer:

```bash
git push --force-with-lease
```
## Pasos finales

- Resolver el pull request y hacer merge desde github

- Volver a hacer git rebase en caso de que falten cambios por subir.

### Otros comandos 

Comandos universales que debes recordar (sirven SIEMPRE)
Ver estado del rebase
git status
Continuar rebase
git rebase --continue
Saltar un commit problemático
git rebase --skip
Cancelar todo el rebase
git rebase --abort

y vuelves al estado anterior.

Flujo profesional típico

Muchos equipos trabajan así:

git checkout feature-rama
git fetch origin
git rebase origin/main
# resolver conflictos
git push --force-with-lease
Algo importante que hiciste bien

Hiciste exactamente el flujo correcto:

git checkout main
git pull
git checkout bugfix/pipeline-unsupervised
git rebase main

Eso es lo que hacen los ingenieros normalmente.

El conflicto simplemente significa:

alguien cambió el README en main y tú también.



### consejos 

Consejo profesional:
Cuando trabajas en feature branches (como pipelines o Django), el flujo más usado es:

git fetch
git rebase origin/main

y después push.

