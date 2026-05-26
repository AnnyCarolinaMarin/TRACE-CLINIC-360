import customtkinter as ctk
from database.conexion import conectar


def obtener_alertas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            paciente,
            tipo_evento,
            estado,
            prioridad,
            fecha
        FROM eventos
        WHERE estado = 'Crítico'
        OR prioridad = 'Urgente'
        OR estado = 'Pendiente'
        ORDER BY fecha DESC
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def crear_alerta(parent, alerta):

    paciente, evento, estado, prioridad, fecha = alerta

    # =====================================
    # COLORES DINAMICOS
    # =====================================

    bg_color = "#FFFFFF"
    border_color = "#CBD5E1"
    icono = "🔵"

    if prioridad == "Urgente":

        bg_color = "#FEE2E2"
        border_color = "#DC2626"
        icono = "🔴"

    elif estado == "Crítico":

        bg_color = "#FECACA"
        border_color = "#B91C1C"
        icono = "⚠"

    elif estado == "Pendiente":

        bg_color = "#FEF3C7"
        border_color = "#D97706"
        icono = "🟡"

    # =====================================
    # CARD
    # =====================================

    card = ctk.CTkFrame(
        parent,
        fg_color=bg_color,
        corner_radius=20,
        border_width=1,
        border_color=border_color
    )

    card.pack(
        fill="x",
        padx=20,
        pady=10
    )

    # =====================================
    # TITULO
    # =====================================

    titulo = ctk.CTkLabel(
        card,
        text=f"{icono} {evento}",
        font=("Arial", 22, "bold"),
        text_color="#0F172A"
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=(15, 10)
    )

    # =====================================
    # DETALLES
    # =====================================

    detalle = ctk.CTkLabel(
        card,
        text=f"""
            Paciente: {paciente}
            Estado: {estado}
            Prioridad: {prioridad}
            Fecha: {fecha}
            """,
        justify="left",
        font=("Arial", 15),
        text_color="#334155"
    )

    detalle.pack(
        anchor="w",
        padx=20,
        pady=(0, 20)
    )

def pantalla_alertas(parent):

    frame = ctk.CTkScrollableFrame(
        parent,
        fg_color="#F1F5F9"
    )

    titulo = ctk.CTkLabel(
        frame,
        text="Panel de Alertas Clínicas",
        font=("Arial", 30, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=20
    )

    alertas = obtener_alertas()

    if not alertas:

        vacio = ctk.CTkLabel(
            frame,
            text="No existen alertas activas",
            font=("Arial", 20)
        )

        vacio.pack(pady=50)

    else:

        for alerta in alertas:
            crear_alerta(frame, alerta)

    return frame