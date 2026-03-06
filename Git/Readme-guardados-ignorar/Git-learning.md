# Aprendiendo a dominar git 

## Comandos basicos de git 

```bash
# ==========================================
# CLONAR UN REPOSITORIO EXISTENTE
# ==========================================

# Clona un repositorio remoto en tu máquina local
git clone <url_del_repositorio>

# Ingresa a la carpeta del proyecto
cd <nombre_del_repositorio>


# ==========================================
# CREAR UN NUEVO REPOSITORIO DESDE CERO
# ==========================================

# Inicializa un nuevo repositorio Git en el proyecto actual
git init

# ==========================================
# CONFIGURAR USUARIO (solo una vez por equipo)
# ==========================================

# Configura tu nombre de usuario
git config --global user.name "Tu Nombre"

# Configura tu correo electrónico
git config --global user.email "tu@email.com"


# ==========================================
# FLUJO BÁSICO DE TRABAJO
# ==========================================

# Verifica el estado del repositorio
git status

# Agrega un archivo específico al staging
git add <archivo>

# Agrega todos los archivos modificados
git add .

# Crea un commit con un mensaje descriptivo
git commit -m "Descripción clara del cambio"

# Envía los cambios al repositorio remoto
git push origin main

```

## descartar cambios 

```bash

git restore --staged archivo.py


```

---

## Ramas  

- Contendio referido solamente a ramas, a continuacion de esta seccion, se hablara de uniones o entre otras cosas. 

### Creación de rama

```bash

# Al hacer el git add y git commit -m, el siguiente paso sera enfocado en la creación de ramas.

# Verifica las ramas disponibles o si se ha creado la rama.

git branch

# Al crear una rama, hay que hacer add . en algunos casos

git branch <nombre_rama>

# Nombres de ramas. Para las buenas practicas, utilizaremos estos prefijos y sus nombres.
# Siempre en minúsculas y separando con guiones:

git branch feature/sistema-pago-online

| Prefijo     | Cuándo usarlo                            | Ejemplo                         |
| ----------- | ---------------------------------------- | ------------------------------- |
| `feature/`  | Nueva funcionalidad                      | `feature/carrito-compras`       |
| `bugfix/`   | Corrección de errores                    | `bugfix/error-login`            |
| `hotfix/`   | Error crítico en producción              | `hotfix/pago-duplicado`         |
| `refactor/` | Mejora interna sin cambiar funcionalidad | `refactor/validaciones-modelo`  |
| `docs/`     | Documentación                            | `docs/readme-api`               |
| `test/`     | Agregar o mejorar tests                  | `test/modelos-usuario`          |
| `chore/`    | Tareas técnicas menores                  | `chore/actualizar-dependencias` |

# Opcion 2: Esta opcion nos cambia el punto de vista de como funciona git en otras ocaciónes.

git checkout -b nombre_rama

# Crea la rama y automáticamente te cambia a ella.

#Ejemplo:

git checkout -b feature-login


# Es equivalente a hacer:

git branch feature-login
git checkout feature-login


# Pero en un solo comando.

```
### Moverte de una rama a otra

```bash

# Visualizamos las ramas disponibles 

git branch

# Selecciónamos la rama que queremos entrar

git checkout <Nombre de la rama creada>

# O tambien



```

---

## Realizar marche de ramas (union de ramas)

En esta sección habran dos escenarios

1. Una union correcta de ramas

2. Cuando existe un conficto de ramas 


```bash

git 

```

--- 

## Mis Errores

### **Error clasico:** Un repositorio dentro de otro repositorio. (submodulo)

Cuando iniciamos un proyecto como principiantes, es común cometer el error de crear un repositorio dentro de otro repositorio sin intención.

Esto genera lo que Git interpreta como un submódulo, aunque realmente no queríamos crear uno.

---

**¿Por qué ocurre esto?**

- Ejecutamos git init en una carpeta padre.

- Luego ejecutamos git init nuevamente en una subcarpeta.

- O clonamos (git clone) un repositorio dentro de una carpeta que ya tenía un .git


```
Proyecto-FIFA-web/        ← Repo 1 (master, sin commits)
│
└── FIFA-web/             ← Repo 2 (main, con commits)
      ├── .git
      ├── README.md
      ├── LICENSE
      └── ...
```

**¿Cómo evitar este error?**

Regla profesional:

> Un proyecto = una carpeta raíz = un solo .git

# Referencias 

Como inicar git
https://www.youtube.com/watch?v=QYIT6k4JOfM

fusion merge de ramas
https://www.youtube.com/watch?v=Kq3AbJayY6Y
