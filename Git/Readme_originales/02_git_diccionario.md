
# MANUAL COMPLETO PROFESIONAL DE GIT

Este documento contiene:

- Manual base de Git
- Comandos avanzados
- Todas las variantes importantes
- Diferencias entre comandos similares
- Buenas prácticas
- Advertencias críticas
- Casos de uso reales

No sigue un flujo lineal.
Es un documento de referencia total.

## SECCION 1 - FUNDAMENTOS

### 1- INICIALIZAR REPOSITORIO
------------------------------------------------------------

- Crear repositorio:
```bash

git init

Clonar repositorio existente:

git clone <url>

Clonar en carpeta específica:

git clone <url> nombre_carpeta
```
------------------------------------------------------------
2) CONFIGURACION DE USUARIO
------------------------------------------------------------

```bash
Configurar global:

git config --global user.name "Tu Nombre"
git config --global user.email "correo@email.com"

Configurar solo proyecto actual:

git config user.name "Otro Nombre"
git config user.email "otro@email.com"

Ver configuración:

git config --list
git config --global --list

Editar configuración manual:

git config --global -e
```



## Ver información del repositorio

```bash
# Verifica el estado del repositorio
git status

# Ver diferencias antes de hacer commit
git diff

# Ver historial completo
git log

# Historial resumido
git log --oneline

# Ver gráfico visual de ramas
git log --graph --oneline --all

# Ver detalles de un commit específico
git show <id_commit>
```

------------------------------------------------------------
3) ESTADOS EN GIT
------------------------------------------------------------

```bash
Working Directory
Staging Area
Repository

Flujo básico:
Modificar -> Add -> Commit -> Push
```
------------------------------------------------------------
4) GIT ADD
------------------------------------------------------------

```bash
Agregar archivo específico:

git add archivo.txt

Agregar múltiples:

git add archivo1.txt archivo2.txt

Agregar carpeta:

git add carpeta/

Agregar todo:

git add .

Agregar por extensión:

git add *.txt
git add *.md

Modo interactivo profesional:

git add -p
```


------------------------------------------------------------
5) DESHACER GIT ADD
------------------------------------------------------------
``` bash
git restore --staged archivo.txt

Alternativa clásica:

git reset archivo.txt
```
------------------------------------------------------------
6) COMMITS
------------------------------------------------------------

Crear commit:
```bash
git commit -m "Mensaje claro"

Agregar y hacer commit:

git commit -a -m "Mensaje"

Modificar último commit:

git commit --amend

Cambiar mensaje:

git commit --amend -m "Nuevo mensaje"
```

------------------------------------------------------------
7) DESHACER COMMITS
------------------------------------------------------------


Revertir commit (seguro):
```bash
git revert <id_commit>

Reset suave:

git reset --soft <id_commit>

Reset mixto:

git reset --mixed <id_commit>

Reset duro (borra todo):

git reset --hard <id_commit>

Nunca usar --hard en ramas compartidas.
```
------------------------------------------------------------
8) RAMAS
------------------------------------------------------------

- Ver ramas locales:

```bash
git branch

Ver todas:

git branch -a
```
- Crear rama:

```bash
git branch nombre_rama

Crear y cambiar:

git checkout -b nombre_rama

Forma moderna:

git switch -c nombre_rama
```
- Cambiar rama:

```bash
git checkout nombre_rama
git switch nombre_rama
```

- Eliminar rama:

```bash
git branch -d nombre_rama

Forzar eliminación:

git branch -D nombre_rama
```

- Eliminar rama remota:

```bash
git push origin --delete nombre_rama
```
------------------------------------------------------------
9) MERGE
------------------------------------------------------------

- Fusionar rama:
```bash
git merge nombre_rama

Abortar conflicto:

git merge --abort
```
------------------------------------------------------------
10) REMOTO
------------------------------------------------------------

- Agregar remoto:

```bash
git remote add origin <url>
```
- Ver remotos:

```bash
git remote -v
```
- Subir cambios:

```bash 
git push origin main
```

- Establecer upstream:

```bash
git push -u origin main
```
Actualizar:
```bash
git pull origin main
```

Diferencia:
pull = fetch + merge
fetch = solo descarga

------------------------------------------------------------

### 11- STASH

**ESCENARIO TÍPICO:** Estás trabajando en main (o cualquier rama) y:

- Tienes cambios sin terminar

- Necesitas hacer git pull

- cambiar de rama

- hacer hotfix urgente

Nota: También se conoce como área temporal o staging area (preparación) al espacio intermedio antes de un commit, pero para "guardar y ocultar" cambios temporalmente, el comando específico es git stash.

Guardar cambios temporales:

```bash
# Primero ver el estado del proyecto
git status

#Solo archivos rastreados:
git stash
#o Incluir archivos no rastreados:
git stash -u

git stash push -m "cambio temporal antes de pull"
```
Guardar con mensaje:

```bash
git stash save "mensaje"
```

-Ver lista:

```bash
git stash list
```
- Aplicar y eliminar:

```bash
git stash pop
```

- Aplicar sin eliminar:
```bash
git stash apply
```

## SECCION 2 - AVANZADO

### 12- REBASE
------------------------------------------------------------

Rebase básico:

git rebase main

Rebase interactivo:

git rebase -i HEAD~3

Opciones en interactivo:

pick
reword
edit
squash
fixup
drop

Continuar tras conflicto:

git rebase --continue

Abortar:

git rebase --abort

Nunca hacer rebase en ramas públicas.

------------------------------------------------------------
13) CHERRY-PICK
------------------------------------------------------------

Aplicar commit específico:

git cherry-pick <id_commit>

Continuar:

git cherry-pick --continue

Abortar:

git cherry-pick --abort

------------------------------------------------------------
14) REFLOG
------------------------------------------------------------

Ver historial interno:

git reflog

Recuperar commit:

git reset --hard HEAD@{3}

Reflog permite recuperar:
- commits borrados
- ramas eliminadas
- errores de reset

------------------------------------------------------------
15) BISECT
------------------------------------------------------------

Iniciar:

git bisect start

Marcar actual como malo:

git bisect bad

Marcar commit bueno:

git bisect good <id>

Finalizar:

git bisect reset

------------------------------------------------------------
16) TAGS
------------------------------------------------------------

Crear tag simple:

git tag v1.0

Tag anotado:

git tag -a v1.0 -m "Versión estable"

Ver tags:

git tag

Enviar tags:

git push origin --tags

============================================================
SECCION 3 - BUENAS PRACTICAS PROFESIONALES
============================================================

No reutilizar ramas antiguas.
Eliminar ramas tras merge.
No hacer commits gigantes.
Escribir mensajes claros.
No usar reset --hard en equipo.
Hacer pull antes de comenzar trabajo.
Usar ramas por funcionalidad.
Usar rebase solo en ramas locales.
Usar revert en ramas públicas.