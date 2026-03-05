# Desasher cambios 

Digamos que hemos iniciado nuevamente unos cambios al proyecto. Por lo que simularemos agregar nuevos cambios, hacer nuevos commits, nuevas ramas y eliminar cambios y evitar conflictos. 

Con el tiempo se actualizara este readme.md para agregar la mayor cantidad de codigos de git. 

No olvidar la reflexion, la idea no es saber mas comandos, sino la logica.

## Flujo de comandos esperados 

### Crear un nuevo repositorio desde cero

```bash
# Inicializa un nuevo repositorio Git
git init
```
---

## Flujo básico de trabajo

```bash
# Verifica el estado del repositorio
git status

# Ver diferencias entre archivos modificados y el último commit
git diff

# Agrega un archivo específico
git add <archivo>

# Agrega todos los archivos modificados
git add .

# Crear un commit
git commit -m "Descripción clara del cambio"

# Enviar cambios al repositorio remoto
git push origin main
```

---

## Comparar cambios

```bash
# Ver diferencias antes de hacer add
git diff

# Ver diferencias después de hacer add (en staging)
git diff --staged
```

---

## Eliminar archivos

```bash
# Eliminar un archivo del proyecto y del repositorio
git rm <archivo>

# Eliminar un archivo solo del repositorio pero mantenerlo local
git rm --cached <archivo>
```

---

## Deshacer cambios

```bash
# Quitar un archivo del staging (deshacer git add)
git reset <archivo>

# Deshacer el último commit manteniendo los cambios
git reset --soft HEAD~1

# Deshacer el último commit eliminando cambios
git reset --hard HEAD~1
```

⚠️ Advertencia:  
`--hard` elimina cambios permanentemente.

---

## Guardar cambios temporalmente (Stash)

El stash permite guardar cambios sin hacer commit.

```bash
# Guardar cambios temporales
git stash

# Ver lista de cambios guardados
git stash list

# Recuperar el último stash
git stash pop

# Recuperar un stash específico
git stash apply stash@{0}

# Eliminar un stash específico
git stash drop stash@{0}
```

El stash es útil cuando necesitas cambiar de rama pero tienes cambios sin confirmar.