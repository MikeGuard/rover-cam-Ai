import math
def angolo_freccia(x_attendibile, height : int, width) -> tuple:
    if x_attendibile != 0:
     spostamento_freccia = (x_attendibile)
     angolo_frec = int(math.degrees(math.atan(int(spostamento_freccia)/int((height / 10)*4)))) 
    else:
        angolo_frec = 0
    return angolo_frec


def freccia_on_screen(x_attendibile, width : int, height : int) -> tuple:
    centro_angolo = x_attendibile
    spostamento_freccia_x_a = centro_angolo / 5 + (width / 10 * 8.5)
    spostamento_freccia_x_b = (width / 10) * 8.5
    altezza_freccia = (height / 10) * 2
    posizione_freccia_y_b = (height / 10) * 7
    posizione_freccia_y_a = altezza_freccia + posizione_freccia_y_b
    return spostamento_freccia_x_a, spostamento_freccia_x_b, posizione_freccia_y_a, posizione_freccia_y_b






    