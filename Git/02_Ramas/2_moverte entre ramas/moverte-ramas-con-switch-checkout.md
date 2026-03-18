mover los cambios del stage a otra rama

Brandon, si quieres mover los cambios que ya están en el staging area a otra rama, depende del estado en que estén.

Te explico los casos más comunes 👇

🔹 Caso 1: Solo están en stage (hiciste git add, pero NO git commit)

En este caso es fácil:

git switch nombre-nueva-rama

Git se lleva contigo los cambios (tanto los staged como los unstaged) a la nueva rama automáticamente.

Si la rama no existe:

git switch -c nombre-nueva-rama

Listo. Tus cambios siguen ahí, pero ahora en la otra rama.

🔹 Caso 2: Ya hiciste commit en la rama equivocada

Aquí hay dos opciones.

✅ Opción A (más limpia): mover el commit

1️⃣ Crea la nueva rama desde donde estás:

git branch nueva-rama

2️⃣ Vuelve la rama actual al estado anterior:

git reset --soft HEAD~1

Eso:

Quita el commit

Pero deja los cambios en stage

3️⃣ Cambias a la nueva rama:

git switch nueva-rama

4️⃣ Y haces el commit ahí:

git commit -m "mensaje"
⚠️ Si ya hiciste push

Si ya lo subiste al remoto, cambia la estrategia porque reescribes historial. Ahí dime y lo vemos con más cuidado.

🔥 Extra (por si estás en medio de un rebase como antes)

Si estás en algo como:

(no branch, rebasing feature/...)

Primero termina el rebase:

git rebase --continue

Y después haces el movimiento.

Si quieres, dime exactamente qué te muestra:

git status
git branch

y te digo el comando exacto para tu caso 👌