 eso esta bien? hacer merge en una rama para traer cambios de otra y tambien asi con main?

Sí, eso está bien 👍 Es una práctica normal en Git.

Lo importante es entender para qué estás haciendo el merge, porque hay dos situaciones comunes.

1️⃣ Actualizar tu rama con lo último de main (muy común)

Estás trabajando en una rama, por ejemplo:

feature/login

Pero main avanzó con nuevos cambios. Entonces actualizas tu rama:

git checkout feature/login
git merge main

📌 Resultado:
Tu rama trae los cambios nuevos de main para evitar conflictos después.

Esto se hace mucho antes de hacer un Pull Request.

2️⃣ Pasar tu trabajo a main

Cuando tu trabajo ya está listo.

git checkout main
git merge feature/login
git push

📌 Resultado:
main ahora tiene los cambios de tu rama.

Esto también es lo que hace GitHub automáticamente cuando aceptas un Pull Request.

Flujo típico profesional

1️⃣ Crear rama

git checkout -b feature/login

2️⃣ Trabajar y hacer commits

3️⃣ Actualizar tu rama con main

git merge main

4️⃣ Subir la rama

git push origin feature/login

5️⃣ Crear Pull Request

6️⃣ Merge a main

✅ Conclusión:
Sí, es correcto hacer merge en una rama para traer cambios de otra.

merge main → actualizar tu rama

merge rama en main → integrar cambios finales

💡 Tip importante:
Muchos equipos prefieren esto:

git pull origin main --rebase

en vez de merge, porque deja el historial más limpio.