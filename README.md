# TRACE-CLINIC 360
## Plataforma de Gestión y Trazabilidad Clínica

---

# Descripción General

TRACE-CLINIC 360 es un sistema desarrollado en Python enfocado en el control y seguimiento de eventos clínicos y quirúrgicos dentro de entornos hospitalarios.

La aplicación permite administrar información relacionada con pacientes, procedimientos médicos, alertas clínicas y procesos hospitalarios, facilitando la organización y trazabilidad de cada evento registrado.

## Entre las principales funciones del sistema se encuentran:

- Registro de eventos clínicos
- Seguimiento de procedimientos médicos
- Consulta de información hospitalaria
- Gestión de alertas
- Visualización de líneas de tiempo
- Auditoría de acciones realizadas

El proyecto fue construido utilizando Python junto con la librería CustomTkinter para la interfaz gráfica y SQLite como sistema de almacenamiento de datos.

---

# Tecnologías Implementadas

- Python 3.11 o superior
- CustomTkinter
- SQLite
- Tkinter ttk

---

# Dependencias Requeridas

Antes de iniciar la aplicación es necesario instalar las siguientes librerías:

```bash
pip install customtkinter
pip install pillow
```

---

# Organización del Proyecto

```txt
TRACE-CLINIC-360/
│
├── database/
│   ├── conexion.py
│   └── models.py
│
├── ui/
│   ├── login.py
│   ├── dashboard.py
│   ├── registrar_evento.py
│   ├── consultar_eventos.py
│   ├── auditoria_view.py
│   ├── timeline.py
│   ├── alertas.py
│   └── reportes.py
│
├── layout.py
├── main.py
└── database.db
```

---

# Guía de Instalación y Ejecución

## Paso 1 — Instalar Python

Descargar Python desde el sitio oficial:

```txt
https://www.python.org/downloads/
```

Durante la instalación es importante activar la opción:

```txt
Add Python to PATH
```

---

## Paso 2 — Obtener el Proyecto

### Opción 1 — Descargar ZIP

Descargar el repositorio desde GitHub y descomprimir el archivo.

### Opción 2 — Clonar el Repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

---

## Paso 3 — Abrir el Proyecto

Abrir la carpeta principal utilizando alguno de los siguientes entornos:

- Visual Studio Code
- PyCharm
- Cursor
- Otro editor compatible con Python

---

## Paso 4 — Instalar Dependencias

Abrir una terminal dentro del proyecto y ejecutar:

```bash
pip install customtkinter
pip install pillow
```

---

# Paso 5 — Ejecutar la Aplicación

Ubicarse en la carpeta raíz del proyecto y ejecutar:

```bash
python main.py
```

---

## Paso 6 — Inicio de Sesión

Al iniciar el sistema utilizar las siguientes credenciales:

```txt
Usuario: user
Contraseña: 12345
```

---

# Características Principales

## Dashboard Clínico

El sistema cuenta con un panel principal que permite visualizar información estadística relacionada con:

- Total de eventos registrados
- Eventos críticos
- Eventos pendientes
- Prioridades urgentes
- Eventos registrados durante el día

---

## Registro de Eventos

Módulo encargado del almacenamiento de información clínica relacionada con:

- Pacientes
- Procedimientos
- Resultados
- Responsables
- Estados clínicos
- Prioridades

---

## Línea de Tiempo Clínica

Permite visualizar cronológicamente todos los eventos registrados dentro del sistema.

---

## Sistema de Alertas

Genera alertas automáticas para situaciones como:

- Eventos críticos
- Prioridades urgentes
- Procesos pendientes

---

## Auditoría

Facilita el seguimiento de actividades realizadas dentro de la plataforma, permitiendo mantener trazabilidad operativa.

---

# Base de Datos

TRACE-CLINIC 360 utiliza SQLite como motor de base de datos local.

La creación de la base de datos se realiza automáticamente al iniciar el sistema por primera vez.

---

# Posibles Mejoras Futuras

- Exportación de reportes PDF
- Exportación de archivos Excel
- Integración con inteligencia artificial
- Sistema multiusuario
- API REST
- Notificaciones en tiempo real
- Dashboard avanzado con gráficas

---

# Autores del Proyecto

- Any Carolina Marin Martinez
- Marileth Dayana Pereira Fontalvo
- Jesus David Bermudez Monsalve 
- Valeria Valle Alvarado
- Saray Johana Ruiz Perez 

---

# Conclusión

TRACE-CLINIC 360 representa una solución tecnológica orientada a mejorar la organización y trazabilidad de procesos clínicos y quirúrgicos mediante herramientas desarrolladas en Python.

El proyecto demuestra la aplicación práctica de tecnologías de software dentro del sector salud, permitiendo optimizar el seguimiento hospitalario y el control de eventos clínicos de manera estructurada y eficiente.
