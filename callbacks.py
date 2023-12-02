import time
import random
import threading

from eventos import EventManager  

class RealTimeDataManager:
    def __init__(self):
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        while True:
            time.sleep(3)
            self.generate_real_time_data()
            # Notificar al EventManager que los datos han cambiado
            self.event_manager.notify("datos_actualizados", self.data)

    def generate_real_time_data(self):
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)

real_time_data_manager = RealTimeDataManager()

# Actualizaciones en tiempo real en segundo plano
update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
update_thread.start()

# Callback para imprimir los datos actualizados al stdout
def print_updated_data(data):
    print("Datos actualizados:", data)

# Suscribir el callback al EventManager para el evento "datos_actualizados"
real_time_data_manager.event_manager.subscribe("datos_actualizados", print_updated_data)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nPrograma terminado.")
