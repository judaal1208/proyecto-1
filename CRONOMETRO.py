import tkinter as tk
from datetime import datetime

class CronometroApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cronómetro")
        self.inicializar_gui()

        self.is_running = False
        self.inicio_tiempo = None

    def inicializar_gui(self):
        self.label_tiempo = tk.Label(self.master, text="Tiempo: 00:00:00", font=("Arial", 24))
        self.label_tiempo.pack(pady=10)

        self.btn_iniciar_detener = tk.Button(self.master, text="Iniciar", command=self.iniciar_detener_cronometro)
        self.btn_iniciar_detener.pack(pady=5)

        self.btn_reset = tk.Button(self.master, text="Reset", command=self.reset_cronometro)
        self.btn_reset.pack(pady=5)

    def iniciar_detener_cronometro(self):
        if not self.is_running:
            self.is_running = True
            if self.inicio_tiempo is None:
                self.inicio_tiempo = datetime.now()
            else:
                tiempo_actual = datetime.now()
                tiempo_pausa = tiempo_actual - self.tiempo_pausa
                self.inicio_tiempo = tiempo_actual - tiempo_pausa
            self.actualizar_cronometro()
            self.btn_iniciar_detener.config(text="Detener")
        else:
            self.is_running = False
            self.tiempo_pausa = datetime.now()
            self.btn_iniciar_detener.config(text="Continuar")

    def reset_cronometro(self):
        self.is_running = False
        self.inicio_tiempo = None
        self.label_tiempo.config(text="Tiempo: 00:00:00")
        self.btn_iniciar_detener.config(text="Iniciar")

    def actualizar_cronometro(self):
        if self.is_running:
            tiempo_actual = datetime.now()
            tiempo_transcurrido = tiempo_actual - self.inicio_tiempo
            tiempo_formateado = str(tiempo_transcurrido).split('.')[0]
            self.label_tiempo.config(text=f"Tiempo: {tiempo_formateado}")
            self.master.after(1000, self.actualizar_cronometro)

if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()
