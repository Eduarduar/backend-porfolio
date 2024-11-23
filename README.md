# backend-porfolio

## Instalación

### Requisitos previos

- Python 3.x
- pip
- virtualenv

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

### Configuración del archivo .env

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```env
SECRET_KEY='your_secret_key'
DEBUG=True
```

### Migraciones de la base de datos

```bash
# Aplicar las migraciones
python manage.py makemigrations porfolio
python manage.py makemigrations about
python manage.py makemigrations projects
python manage.py makemigrations social
python manage.py makemigrations tools
python manage.py makemigrations projectsTools
python manage.py makemigrations

python manage.py migrate
```

### Iniciar el servidor de desarrollo

```bash
# Iniciar el servidor
python manage.py runserver
```

## Estructura del proyecto

```plaintext
backend-porfolio/
├── about/
├── porfolio/
├── projects/
├── projectsTools/
├── social/
├── tools/
├── venv/
├── .env
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```
