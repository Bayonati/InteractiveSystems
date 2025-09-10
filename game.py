import os
import sys
from audio_manager import AudioManager

class Scene:
    def __init__(self, scene_id, text, sound_events=None):
        self.scene_id = scene_id
        self.text = text
        self.sound_events = sound_events if sound_events else []
        
    def display(self, audio_manager):
        """Muestra el texto y ejecuta los sonidos asociados"""
        print(f"\n{'-'*50}")
        print(f"\n{self.text}")
        
        # Ejecutar eventos de sonido si existen
        for sound_event in self.sound_events:
            sound_event.trigger(audio_manager)
            
        input("\n>>> Presione Enter para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

class SoundEvent:
    def __init__(self, sound_name, action="play", position=(0, 0, 0), volume=1.0):
        self.sound_name = sound_name
        self.action = action  # play, stop, set_position
        self.position = position
        self.volume = volume
        
    def trigger(self, audio_manager):
        if self.action == "play":
            audio_manager.play_sound(self.sound_name)
            audio_manager.set_position(self.sound_name, *self.position)
            audio_manager.set_volume(self.sound_name, self.volume)
        elif self.action == "stop":
            audio_manager.stop_sound(self.sound_name)

class Game:
    def __init__(self):
        self.audio_manager = AudioManager()
        self.scenes = {}
        self.current_scene = None
        self.load_scenes()
        
    def load_scenes(self):
        """Carga todas las escenas del juego con sus sonidos"""
        # Escena 1: Introducción
        self.scenes["intro"] = Scene(
            "intro", 
            "En el principio, no había nada. Solo existían las tres Diosas...",
            [SoundEvent("creation_ambience", "play", (0, 0, -10), 0.8)]
        )
        
        # Escena 2: Diosa Din
        self.scenes["din"] = Scene(
            "din",
            "Din, la Diosa del Poder, creó la tierra...",
            [
                SoundEvent("creation_ambience", "stop"),
                SoundEvent("earth_rumble", "play", (0, 0, -5), 1.0),
            ]
        )
        
        # Escena 3: Diosa Farore
        self.scenes["farore"] = Scene(
            "farore", 
            "Farore, la Diosa del Valor, creó a todos los seres vivientes...",
            [
                SoundEvent("earth_rumble", "stop"),
                SoundEvent("life_creation", "play", (0, 0, 0), 1.0),
                SoundEvent("birds_chirp", "play", (4, 0, 3), 0.7)  # Sonido a la derecha
            ]
        )

        # Escena 4: Diosa Nayru
        self.scenes["nayru"] = Scene(
            "nayru", 
            "Nayru, la Diosa de la Sabiduría, brindó el espíritu de justicia y consciencia a los seres vivientes...",
            [
                SoundEvent("life_creation", "stop"),
                SoundEvent("birds_chirp", "stop"),  
                SoundEvent("culture_village", "play", (0, 0, 0), 1.0)
            ]
        )

        # Escena 5: Trifuerza
        self.scenes["triforce"] = Scene(
            "triforce", 
            "Una vez que terminaron y pudieron observar la inmensidad de su creación, abandonaron la dimensión física, dejando atrás un vestigio de Luz Dorada, que luego daría paso a la creación del objeto más poderoso del universo entero... la grandiosa Trifuerza."\
            "\n\nDurante los años siguientes, muchos intentarían adueñarse de este preciado tesoro, dado que la leyenda dice que a quien tuviese la suerte de tocarlo se le concedería cualquier deseo.\nSin embargo, había una que otra trampa. Si dicha persona no poseía un balance entre las tres virtudes sagradas (Poder, Sabiduría y Valor), la Trifuerza se dividiría en tres, siendo el poderoso tocador capaz de recibir únicamente uno de los fragmentos, cualquiera que fuese el que resonara más con sus cualidades personales. Los otros dos fragmentos se le asignarían a otros dos seres vivientes, quienes poseyeran la mayor cantidad de las virtudes restantes."\
            "\n\nDurante siglos, fue a la diosa Hylia, una deidad diferente, a quien se le encomendó la ardúa tarea de proteger la Trifuerza. Pero desafortunadamente, el mundo a su alrededor se volvía cada vez más avaro y muchos comenzaron a levantarse, causando caos y tramando planes malvados para ser los adquisidores de la poderosa Luz Dorada.\nLa leyenda cuenta que hubo un punto en que Hylia se vio amenazada a tal extremo que tuvo que abandonar su divinidad para poder tocar la Trifuerza ella misma y desear su protección. Al hacerlo, reencarnó en quien se convertiría en un ancestro para un reino entero."\
            "\n\nLuego de haber derrotado a su rival más poderoso, junto a su leal caballero, quien empuñaba una versión mejorada de la espada con que ella misma había combatido incontables veces antes, parecía que el mundo por fin encontraría la paz de nuevo.\nAsí hubiese sido, sin embargo, si los últimos alientos de ese rival no hubiesen sido lo que fueron... una promesa, una maldición..."\
            "\n\nPrometió que su odio renacería una y otra vez, y que se aseguraría de que la tierra nunca floreciera bajo las benignas influencias de la diosa Hylia. Y entonces, el eterno ciclo de reencarnaciones comenzó.\nCada tantos milenios, la diosa reencarna de nuevo en una princesa del Reino que se construyó luego de la breve paz que se asentó en la tierra, su caballero, de igual forma reencarnaría en un caballero diferente, jurado a proteger a dicha princesa con su vida, y su rival, también reencarnaría en una ominosa figura, un hombre de poder sin precedentes, con un odio en su corazón solo comparable con aquel de sus encarnaciones pasadas..."\
            "\n\nEsta... es una de esas historias...",
            [
                SoundEvent("earth_rumble", "stop"),
                SoundEvent("life_creation", "play", (0, 0, 0), 1.0),
                SoundEvent("birds_chirp", "play", (4, 0, 3), 0.7)  # Sonido a la derecha
            ]
        )
        
        # ... agregar más escenas siguiendo el mismo patrón

    def new_game(self):
        """Inicia una nueva partida"""
        print("Comenzando Nueva Partida...")
        
        # Secuencia de escenas
        scene_order = ["intro", "din", "farore", "nayru", "intro2"]
        
        for scene_id in scene_order:
            if scene_id in self.scenes:
                self.scenes[scene_id].display(self.audio_manager)
                
    def main_menu(self):
        """Muestra el menú principal"""
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("-----------THE LEGEND OF ZELDA: OCARINA OF TIME-----------")
            print("-----MENÚ PRINCIPAL-----")
            print("1. Nueva Partida")
            print("2. Salir del juego")
            
            try:
                option = input("Seleccione una opción para continuar: ")
                
                if option == "1":
                    self.new_game()
                elif option == "2":
                    print("Saliendo del juego...")
                    self.audio_manager.cleanup()
                    break
                else:
                    print("Por favor ingrese una opción válida (1 o 2)")
                    input("Presione Enter para continuar...")
                    
            except ValueError:
                print("Error: Por favor ingrese un número válido")
                input("Presione Enter para continuar...")

# Punto de entrada del juego
if __name__ == "__main__":
    game = Game()
    game.main_menu()