import time
from threading import Thread, Lock
import threading

mutex = Lock()

def filososEsperando():
    tenedoresDisponibles = 3
    tenedoresOcupados = 0
    hilo = threading.current_thread().getName()

    while True:
        print(f'Filoso {hilo} esperando turno...')
        time.sleep(2)
        mutex.acquire()

        if tenedoresDisponibles > 0:
            print(f'Filosofo {hilo} toma 2 tenedores')
            time.sleep(1)
            tenedoresDisponibles = tenedoresDisponibles - 1
            tenedoresOcupados = tenedoresDisponibles

        try:
            if tenedoresOcupados == 2:
                print(f'Filoso {hilo} está comiendo')
                time.sleep(3)
                tenedoresDisponibles = 3
        finally:
            print(f'Filosofo {hilo} terminó de comer')
            time.sleep(2)
            mutex.release()
            break

def main():
    filosofo1 = Thread(name='1', target=filososEsperando, args=())
    filosofo2 = Thread(name='2', target=filososEsperando, args=())
    filosofo3 = Thread(name='3', target=filososEsperando, args=())
    filosofo4 = Thread(name='4', target=filososEsperando, args=())
    filosofo5 = Thread(name='5', target=filososEsperando, args=())

    filosofo1.start()
    filosofo2.start()
    filosofo3.start()
    filosofo4.start()
    filosofo5.start()

main()