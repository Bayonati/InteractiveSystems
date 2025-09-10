from openal import oalOpen, oalQuit, Listener

class AudioManager:
    def __init__(self):
        self.sounds = {}
        # Configurar el oyente (jugador)
        self.listener = Listener()
        self.listener.position = (0, 0, 0)  # Posición inicial del jugador

    def load_sound(self, name, filepath):
        try:
            sound = oalOpen(filepath)
            if sound:
                self.sounds[name] = sound
            else:
                print(f"Error al cargar: {filepath}")
        except Exception as e:
            print(f"Error cargando {filepath}: {e}")

    def play_sound(self, name):
        if name in self.sounds:
            self.sounds[name].play()
        else:
            print(f"Sonido '{name}' no encontrado")

    def set_position(self, name, x, y, z):
        if name in self.sounds:
            self.sounds[name].set_position((x, y, z))

    def set_volume(self, name, volume):
        if name in self.sounds:
            self.sounds[name].gain = volume

    def stop_sound(self, name):
        if name in self.sounds:
            self.sounds[name].stop()

    def cleanup(self):
        for sound in self.sounds.values():
            sound.destroy()
        oalQuit()