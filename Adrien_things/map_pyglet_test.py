import random as ran
import pyglet as py
import Carte as Carte
import matrix_manager as mm
from pyglet.window import key


window = py.window.Window()

dimension = (5, 5)
batch = py.graphics.Batch()
shapes = []


@window.event
def on_key_press(symbol, modifier):
    if symbol == key.A:
        print("A was pressed")
        a = input("choix ")
        if a == "1":
            tilemap = Carte.w_f_c_simplified(mm.create_matrix((60, 60),
                            {Carte.Plain: 3, Carte.Mountain: 1, Carte.Forest: 2, Carte.Desert: 2, Carte.Sea: 1, Carte.River: 2}),
                                          )
        
        else:
            tilemap = Carte.w_f_c_evolved(mm.create_matrix((500, 500),
                                                           {"baba": 2}),
                                                            50, [100, 6, Carte.Water], 15)
        print(tilemap)
        for i in range(len(tilemap)):
            for j in range(len(tilemap[1])):
                try:
                    tilemap[i][j].Color
                except AttributeError:
                    continue
                cell = py.shapes.Rectangle(x=50 + j*10,
                                           y=600 + i*(-10),
                                           width=10,
                                           height=10,
                                           color=tilemap[i][j].Color,
                                           batch=batch 
                                           )
                shapes.append(cell)
    if symbol == key.B:
        r = ran.choice(shapes)
        r.delete()


def matrice_creation(dimension_x, dimension_y):
    """Fonction créant une matrice"""
    matrice = []
    for i in range(dimension_x):
        matrice.append([])
        for y in range(dimension_y):
            pass
        
            
@window.event
def on_draw():
    window.clear()
    batch.draw()
        

if __name__ == "__main__":
    py.app.run()
    
