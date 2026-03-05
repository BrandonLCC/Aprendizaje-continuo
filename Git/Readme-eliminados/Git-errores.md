
## Mis Errores

### **Error clasico:** Un repositorio dentro de otro repositorio. (submodulo)

Cuando iniciamos un proyecto como principiantes, es común cometer el error de crear un repositorio dentro de otro repositorio sin intención.

Esto genera lo que Git interpreta como un submódulo, aunque realmente no queríamos crear uno.

**Inicio del error:** Creación del proyecto al intentar hacer un commit. Se hace .git en la carpeta padre cuando ya exisitia un .git en la carpeta del repositorio clonada. 

**Soluciones:** 

1. Eliminar la carpeta padre creada localmente `Proyecto-FIFA-web/` y mantener la carpeta del proyecto 

2. Solo hacer git init en la carpeta del proyecto clonado, no en la carpeta creada localmente y mantenerla ahi.

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

