# Conflictos

- Accept Current Change: acepta los cambios de la rama actual (HEAD).

- Accept Incoming Change: acepta los cambios de la otra rama (por ejemplo, main).

### **Tipos de conflictos**

### Conflictos que pueden resolverse automáticamente **(Git decide).**


### Conflictos que requieren intervención manual.

### Solución manual de conflictos

**¿Por qué solución manual?**

Se utiliza cuando ninguna de las opciones automáticas de Git es suficiente para resolver el conflicto.

**Esto ocurre porque:**

- En la rama principal se modifica la variable result.

- En la rama actual se cambia el mensaje de console.log.

**Por lo tanto, se necesita combinar ambos cambios para lograr una fusión correcta.**

**Ejemplo**

```bash 
<<<<<<< HEAD (Current Change)

const calculation = data + 10;
console.log("This is the result:", calculation);
=======

const result = data + 10;
console.log("Result is:", result);

>>>>>>> main (Incoming Change)
```
En este caso, la solución debe realizarse manualmente, editando el código para integrar ambos cambios de forma coherente.

### **Referencia**

https://www.youtube.com/watch?v=DloR0BOGNU0