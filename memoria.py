#A00827133 Andrea Fernanda Molina Blandon
#A00829207 Isaac Alejandro Enriquez Trejo
from random import *
from turtle import *
from freegames import path

#Se crean la lista de signos a utilizar así como también se
#importa la imagen del carro que resulta de resolver el juego.
win_condition=0
car = path('car.gif')
tiles = list(['!','#','$','%','&','♂','♪','♫','=','▼','▲','?','¶',
              '♀','¬','@','○','↓','↑','~','+','►','§','↔','<','>',
              '☻','♥','☺','♦','♣','♠']) * 2
state = {'mark': None}
hide = [True] * 64

#Esta función dibuja los cuadrados blanco con borde negro
#en los que hay que darle clic para voltearlos.
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

#Esta función convierte coordenadas al número de casilla
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

#Esta función convierte la cuenta de casillas a las coordenadas.
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

#Esta función sirve para que cuando se haga
#click en una casilla la compare con la anterior.
#También esconde las casillas en caso de no ser la correcta.
def tap(x, y):
    global win_condition
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
        #Este contador aumenta cada vez que una pareja correcta sea elegida
        win_condition+=1
        
#Esta función dibuja la imagen y las
#casillas, asi como el texto en ellas.
def draw():
    global win_condition
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    #Este ciclo lo que hace es que esconde las 64 casillas
    #para que si vean cuadros blancos y no el automovil.
    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    #Esta condición pone el simbolo cuando se le da click
    #a una casilla, por default viene en Arial tamaño 30.
    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
     
    #Esta condición desplega un signo de victoria si
    #todas las casillas se han volteado correctamente.
    #Si se quiere sólo probar la función reemplazar el 32 por 1.
    if win_condition == 32:
        up()
        goto(0,0)
        down()
        write("GANASTE!", align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

shuffle(tiles) #Se ponen en orden aleatorio las casillas
setup(420, 420, 370, 0)
addshape(car) #Se añade la imagen del automovil
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()