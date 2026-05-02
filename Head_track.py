from panda3d.core import loadPrcFileData


loadPrcFileData("", "win-size 1500 800")


from ursina import Ursina, Entity, Sky, color, application
from ursina.window import instance as window
from ursina.prefabs.first_person_controller import FirstPersonController




def main():


   app = Ursina(title="Head Tracking World", borderless=False, development_mode=True)


   window.color = color.rgb(135, 206, 235)


   Sky(texture="sky_default")


   ground = Entity(
       model="plane",
       color=color.rgb(45, 160, 65),
       texture="grass",
       texture_scale=(64, 64),
       scale=(200, 1, 200),
       position=(0, 0, 0),
       collider="box",
   )


   player = FirstPersonController()
   player.position = (0, 2, 0)


   player.cursor.enabled = False


   class QuitOnKey(Entity):
       def input(self, key):
           if key in ("q", "escape"):
               application.quit()
   QuitOnKey()


   app.run()




if __name__ == "__main__":
   main()