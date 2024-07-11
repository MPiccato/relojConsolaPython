import time
from datetime import datetime

try:
    while True:
        ahora = datetime.now().strftime("%H:%M:%S")
        print("\rHora actual: {}".format(ahora), end="")
        time.sleep(1)
except KeyboardInterrupt:
    print("Reloj Interrumpido por el usuario")