# backend-portfolio

## Descripción del proyecto

Este es el backend de un portafolio personal desarrollado con Django. Proporciona funcionalidades para manejar información como **about**, **proyectos**, **redes sociales**, **herramientas** y más.

---

## Instalación

### Requisitos previos

- **Python** 3.x
- **pip** (administrador de paquetes de Python)
- **virtualenv** (para entornos virtuales)

### Configuración del entorno

#### Windows

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate

# Instalar las dependencias
pip install -r requirements.txt
```

#### Linux/MacOS

```bash
# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar las dependencias
pip install -r requirements.txt
```

---

### Configuración del archivo `.env`

1. Crea un archivo `.env` en la raíz del proyecto.
2. Agrega las siguientes variables de entorno (modifica según sea necesario):

```env
SECRET_KEY='your_secret_key'
DEBUG=True
```

> **Nota:** Cambia `your_secret_key` por una clave generada segura. Puedes usar un generador como el siguiente:
>
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

---

### Migraciones de la base de datos

Aplica las migraciones para configurar la base de datos:

```bash
# Crear y aplicar las migraciones para cada módulo
python manage.py makemigrations about projects social tools projectsTools porfolio

# Aplicar todas las migraciones al proyecto
python manage.py migrate
```

---

### Iniciar el servidor de desarrollo

Ejecuta el servidor de desarrollo en localhost:

```bash
python manage.py runserver
```

Por defecto, el servidor estará disponible en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Estructura del proyecto

```plaintext
backend-portfolio/
├── about/           # Módulo para la sección "Acerca de"
├── porfolio/        # Configuración principal de Django
├── projects/        # Módulo para proyectos
├── projectsTools/   # Relación entre proyectos y herramientas
├── social/          # Módulo para redes sociales
├── tools/           # Módulo para herramientas
├── venv/            # Entorno virtual (ignorado por Git)
├── .env             # Archivo de configuración (ignorado por Git)
├── .gitignore       # Archivos/Carpetas ignorados por Git
├── db.sqlite3       # Base de datos SQLite (no para producción)
├── manage.py        # Archivo principal de gestión
├── README.md        # Este archivo
└── requirements.txt # Dependencias del proyecto
```

---

## Notas adicionales

- **Producción:** Para entornos de producción, asegúrate de desactivar `DEBUG` y utilizar una base de datos más robusta, como PostgreSQL.
- **Dependencias adicionales:** Si necesitas instalar dependencias adicionales, agrégalas al archivo `requirements.txt`.
