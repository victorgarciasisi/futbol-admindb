# app.py
from flask import Flask, request, render_template, redirect, url_for, flash, session
from functools import wraps
import mysql.connector

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para manejar sesiones

# Configuración de la base de datos
db_config = {
    'host': 'mysql',  # Nombre del servicio de MySQL en docker-compose.yml
    'user': 'root',
    'password': 'rootpassword',
    'database': 'futbol_app'
}

# Credenciales fijas
USERNAME = 'admin'
PASSWORD = 'admin1234'

# Decorador para verificar si el usuario ha iniciado sesión
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            flash('Por favor, inicia sesión para acceder a esta página.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Ruta de inicio de sesión
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'admin1234':
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash('Usuario o contraseña incorrectos', 'error')  # Agregar mensaje de error
    return render_template('login.html')

# Ruta de cierre de sesión
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('Has cerrado sesión.', 'success')
    return redirect(url_for('login'))

# Ruta principal
@app.route('/')
@login_required
def index():
    return render_template('index.html')

### CRUD para la tabla jugador

# Insertar jugador
@app.route('/insertar_jugador', methods=['POST'])
@login_required
def insertar_jugador():
    idjugador = request.form['idjugador']
    apodo = request.form['apodo']
    nombre = request.form['nombre']
    fechanacimiento = request.form['fechanacimiento']
    demarcacion = request.form['demarcacion']
    ciudad = request.form.get('ciudad')
    pais = request.form.get('pais')
    alturapeso = request.form.get('alturapeso')
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
    INSERT INTO jugador (idjugador, apodo, nombre, fechanacimiento, demarcacion, ciudad, pais, alturapeso, foto)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (idjugador, apodo, nombre, fechanacimiento, demarcacion, ciudad, pais, alturapeso, "232401.jpg"))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Jugador insertado exitosamente', 'success')
    return redirect(url_for('index'))

# Eliminar jugador
@app.route('/eliminar_jugador', methods=['POST'])
@login_required
def eliminar_jugador():
    jugador_id = request.form['idjugador']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "DELETE FROM jugador WHERE idjugador = %s"
    cursor.execute(query, (jugador_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Jugador eliminado exitosamente', 'success')
    return redirect(url_for('index'))

### CRUD para la tabla partido

# Insertar partido
@app.route('/insertar_partido', methods=['POST'])
@login_required
def insertar_partido():
    idpartido = request.form['idpartido']
    jornada = request.form['jornada']
    resultado = request.form['resultado']
    rival = request.form['rival']
    golesfavor = request.form['golesfavor']
    golescontra = request.form['golescontra']
    idtemporada = request.form['idtemporada']
    ganado = request.form['ganado']
    empatado = request.form['empatado']
    perdido = request.form['perdido']
    fecha = request.form['fecha']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
    INSERT INTO partido (idpartido, jornada, resultado, rival, golesfavor, golescontra, idtemporada, ganado, empatado, perdido, fecha)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (idpartido, jornada, resultado, rival, golesfavor, golescontra, idtemporada, ganado, empatado, perdido, fecha))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Partido insertado exitosamente', 'success')
    return redirect(url_for('index'))

# Eliminar partido
@app.route('/eliminar_partido', methods=['POST'])
@login_required
def eliminar_partido():
    partido_id = request.form['idpartido']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "DELETE FROM partido WHERE idpartido = %s"
    cursor.execute(query, (partido_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Partido eliminado exitosamente', 'success')
    return redirect(url_for('index'))

### CRUD para la tabla partidojugador

# Insertar partidojugador
@app.route('/insertar_partidojugador', methods=['POST'])
@login_required
def insertar_partidojugador():
    idpartidojugador = request.form['idpartidojugador']
    idpartido = request.form['idpartido']
    idjugador = request.form['idjugador']
    partido = request.form.get('partido')
    titular = request.form.get('titular')
    suplente = request.form.get('suplente')
    minutos = request.form.get('minutos')
    roja = request.form.get('roja')
    amarilla = request.form.get('amarilla')
    gol = request.form.get('gol')
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
    INSERT INTO partidojugador (idpartidojugador, idpartido, idjugador, partido, titular, suplente, minutos, roja, amarilla, gol)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (idpartidojugador, idpartido, idjugador, partido, titular, suplente, minutos, roja, amarilla, gol))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Registro de partido-jugador insertado exitosamente', 'success')
    return redirect(url_for('index'))

# Eliminar partidojugador
@app.route('/eliminar_partidojugador', methods=['POST'])
@login_required
def eliminar_partidojugador():
    partidojugador_id = request.form['idpartidojugador']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "DELETE FROM partidojugador WHERE idpartidojugador = %s"
    cursor.execute(query, (partidojugador_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Registro de partido-jugador eliminado exitosamente', 'success')
    return redirect(url_for('index'))

### CRUD para la tabla temporada

# Insertar temporada
@app.route('/insertar_temporada', methods=['POST'])
@login_required
def insertar_temporada():
    idtemporada = request.form['idtemporada']
    temporada = request.form['temporada']
    division = request.form['division']
    posicion = request.form['posicion']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    sql = "INSERT INTO temporada (idtemporada, temporada, division, posicion) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (idtemporada, temporada, division, posicion))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Temporada insertada exitosamente', 'success')
    return redirect(url_for('index'))

# Eliminar temporada
@app.route('/eliminar_temporada', methods=['POST'])
@login_required
def eliminar_temporada():
    temporada_id = request.form['idtemporada']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "DELETE FROM temporada WHERE idtemporada = %s"
    cursor.execute(query, (temporada_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Temporada eliminada exitosamente', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8083, debug=True)
