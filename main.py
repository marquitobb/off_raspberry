import time
import os

def main():
    # Hora de apagado en formato HH:MM
    shutdown_time = "23:30"

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == shutdown_time:
            os.system("sudo shutdown now")
            break
        time.sleep(60)

if __name__ == '__main__':
    main()
