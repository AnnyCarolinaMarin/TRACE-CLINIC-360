from database.conexion import conectar

# Credenciales por defecto para el usuario administrador
DEFAULT_ADMIN_NOMBRE = "Administrador"
DEFAULT_ADMIN_USUARIO = "user"
DEFAULT_ADMIN_PASSWORD = "12345"
DEFAULT_ADMIN_ROL = "Administrador"

def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    # =========================
    # TABLA EVENTOS
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS eventos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente TEXT NOT NULL,
        tipo_evento TEXT NOT NULL,
        descripcion TEXT,
        responsable TEXT,
        area TEXT,
        fecha TEXT,
        resultado TEXT,
        estado TEXT,
        prioridad TEXT
    )
    """)

    # =========================
    # TABLA USUARIOS
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        usuario TEXT UNIQUE,
        password TEXT,
        rol TEXT
    )
    """)

    # =========================
    # TABLA AUDITORIA
    # =========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS auditoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        accion TEXT,
        fecha TEXT
    )
    """)

    # =========================
    # CREAR ADMIN POR DEFECTO
    # =========================

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = 'admin'
    """)

    admin = cursor.fetchone()

    if not admin:

        cursor.execute("""
        INSERT INTO usuarios(
            nombre,
            usuario,
            password,
            rol
        )
        VALUES (?, ?, ?, ?)
        """, (
            DEFAULT_ADMIN_NOMBRE,
            DEFAULT_ADMIN_USUARIO,
            DEFAULT_ADMIN_PASSWORD,
            DEFAULT_ADMIN_ROL
        ))

    conexion.commit()
    conexion.close()