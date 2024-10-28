# Futbol Admin DataBase

## 1. Requisitos del Sistema

- **Python**: 3.6 o superior
- **Flask**: 2.0 o superior
- **SQLite**: Incluido con Python, se usa como sistema de gestión de bases de datos
- **Bootstrap**: Para el diseño de la interfaz de usuario (cargado desde un CDN)

## 2. Instalación

### Clona el repositorio:

```
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### Crea un entorno virtual (opcional pero recomendado):

```
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```
### Configurar base de datos (app.py):

```
db_config = {
    'host': 'mysql',  # Nombre del servicio de MySQL en docker-compose.yml
    'user': 'root',
    'password': 'rootpassword',
    'database': 'futbol_app'
}
```


### Instala las dependencias:

```
pip install Flask
```

## 3. Uso de la Aplicación

**Ejecuta la aplicación**:

```
python app.py
```

**Accede a la aplicación**: Abre tu navegador web y ve a http://127.0.0.1:5000/.

**Inicio de sesión**: Los usuarios deben iniciar sesión para acceder a las funciones de gestión de la base de datos. Las credenciales deben ser configuradas en la aplicación.

**Gestión de datos**: Utiliza la interfaz para insertar, eliminar y visualizar datos de temporadas, jugadores y partidos.

## 4. Estructura del Proyecto
```
/tu_repositorio
│
├── app.py                # Archivo principal de la aplicación
├── templates/            # Carpeta que contiene las plantillas HTML
│   └── index.html        # Plantilla principal
│   └── login.html        # Plantilla login
```

## 5. Rutas y Funcionalidades

### Rutas Principales
- ```/```: Página principal con acceso a formularios de gestión de datos.
- ```/insertar_temporada```: Inserta una nueva temporada.
- ```/eliminar_temporada```: Elimina una temporada existente.
- ```/insertar_jugador```: Inserta un nuevo jugador.
- ```/eliminar_jugador```: Elimina un jugador existente.
- ```/insertar_partido```: Inserta un nuevo partido.
- ```/eliminar_partido```: Elimina un partido existente.
- ```/insertar_partidojugador```: Inserta la relación entre un partido y un jugador.
- ```/eliminar_partidojugador```: Elimina la relación entre un partido y un jugador.
- ```/logout```: Cierra la sesión del usuario.

### Mensajes Flash
La aplicación utiliza mensajes flash para proporcionar retroalimentación al usuario después de las operaciones de inserción y eliminación. Los mensajes pueden ser de éxito o de error.