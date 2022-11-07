from pynput import keyboard


class Actions:
    def on_use(key):
        if key == keyboard.Key.esc:
            return False  # stop listener
        try:
            k = key.char  # single-char keys
        except Exception as e:
            k = key.name  # other keys
            print(e)
        if k in ['1', '2', 'left', 'right']:  # keys of interest
            # self.keys.append(k)  # store it in global-like variable
            print('Key pressed: ' + k)
            return True  # keep listening;

    listener = keyboard.Listener(on_press=on_use)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys


def main():
    action_obj = Actions

