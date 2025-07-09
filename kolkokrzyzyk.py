

import turtle
import random

ninja = turtle.Turtle()
turtle.bgcolor("#C0D9D9")
ninja.speed(10)

# symbole
pierwiastek = 2 ** 0.5

def kolko(x,y,t):
    t.penup()
    t.goto(x, y - 25)
    t.pendown()
    t.circle(25,360)

def krzyzyk(x,y,t):
    t.setheading(0)
    t.penup()
    t.goto(x + 25, y - 25)
    t.left(135)
    t.pendown()
    t.forward(50 * pierwiastek)

    t.penup()
    t.goto(x - 25 ,y - 25)
    t.right(90)
    t.pendown()
    t.forward(50 * pierwiastek)
    t.setheading(0)

# linie
ninja.penup()
ninja.goto(-300,100)
ninja.pendown()
ninja.forward(600)

ninja.penup()
ninja.goto(-300,-100)
ninja.pendown()
ninja.forward(600)

ninja.penup()
ninja.goto(-100,300)
ninja.pendown()
ninja.right(90)
ninja.forward(600)
ninja.left(90)

ninja.penup()
ninja.goto(100,300)
ninja.pendown()
ninja.right(90)
ninja.forward(600)
ninja.left(90)

# tekst
ninja.penup()
ninja.goto(-400,325)
ninja.pendown()
ninja.write("Wybierz symbol :)", align="center", font=("Times New Roman", 20, "normal"))

# przyciski
ninja.color("black", "#ffcc00")
ninja.penup()
ninja.goto(-550,300)
ninja.pendown()
ninja.begin_fill()
ninja.forward(100)
for i in range(3):
    ninja.right(90)
    ninja.forward(100)
ninja.end_fill()
kolko(-475,275,ninja)
ninja.right(90)

ninja.penup()
ninja.goto(-400,300)
ninja.pendown()
ninja.begin_fill()
ninja.forward(100)
for i in range(3):
    ninja.right(90)
    ninja.forward(100)
ninja.end_fill()
krzyzyk(-350,250,ninja)

# po kliknieciu
symbol = None
ilosc = 0
akcja = 0
blok = 1
srodki = [[-200,200], [0,200], [200,200], [-200,0], [0,0], [200,0], [-200,-200], [0,-200], [200,-200]]
wolne = [[-200,200], [0,200], [200,200], [-200,0], [0,0], [200,0], [-200,-200], [0,-200], [200,-200]]
uzytkownik = []
zwyciestwa = [[1,4,7], [2,5,8], [3,6,9], [1,2,3], [4,5,6], [7,8,9], [1,5,9], [3,5,7]]
flaga = 0

def rysunek(a,b):
    global ilosc   
    if symbol == "o" and ilosc < 5:
        kolko(a, b, ninja)
        ilosc += 1
    elif symbol == "x" and ilosc < 5:
        krzyzyk(a, b, ninja)
        ilosc += 1

def przeciwnik(el):
    if symbol == "x":
        kolko(el[0], el[1], ninja)    
    elif symbol == "o":
        krzyzyk(el[0], el[1], ninja)

def klik(x, y):
    global symbol
    global wolne
    global akcja
    global blok
    global uzytkownik
    global flaga
    global srodki

    if -550 <= x <= -450 and 200 <= y <= 300:
        symbol = "o"
        blok = 0
    if -400 <= x <= -300 and 200 <= y <= 300:
        symbol = "x"
        blok = 0

    if blok == 0 and flaga == 0:
        # 1
        if -300 <= x <= -100 and 100 <= y <= 300 and wolne[0] != 0:
            rysunek(-200, 200)
            wolne[0] = 0
            akcja = 1
            uzytkownik += [1]
        # 2
        elif -100 <= x <= 100 and 100 <= y <= 300 and wolne[1] != 0:
            rysunek(0,200)
            wolne[1] = 0
            akcja = 1
            uzytkownik += [2]
        # 3
        elif 100 <= x <= 300 and 100 <= y <= 300 and wolne[2] != 0:
            rysunek(200,200)
            wolne[2] = 0
            akcja = 1
            uzytkownik += [3]
        # 4
        elif -300 <= x <= -100 and -100 <= y <= 100 and wolne[3] != 0:
            rysunek(-200,0)
            wolne[3] = 0
            akcja = 1
            uzytkownik += [4]
        # 5
        elif -100 <= x <= 100 and -100 <= y <= 100 and wolne[4] != 0:
            rysunek(0,0)
            wolne[4] = 0
            akcja = 1
            uzytkownik += [5]
        # 6
        elif 100 <= x <= 300 and -100 <= y <= 100 and wolne[5] != 0:
            rysunek(200,0)
            wolne[5] = 0
            akcja = 1
            uzytkownik += [6]
        # 7
        elif -300 <= x <= -100 and -300 <= y <= -100 and wolne[6] != 0:
            rysunek(-200,-200)
            wolne[6] = 0
            akcja = 1
            uzytkownik += [7]
        # 8
        elif -100 <= x <= 100 and -300 <= y <= -100 and wolne[7] != 0:
            rysunek(0,-200)
            wolne[7] = 0
            akcja = 1
            uzytkownik += [8]
        # 9
        elif 100 <= x <= 300 and -300 <= y <= -100 and wolne[8] != 0:
            rysunek(200,-200)
            wolne[8] = 0
            akcja = 1
            uzytkownik += [9]

        for i in range(len(zwyciestwa)):
            kombinacja = zwyciestwa[i]
            wynik = all(liczba in uzytkownik for liczba in kombinacja)

            if wynik == True:
                wygrana = kombinacja
                numer = wygrana[0]
                wspolrzedne = srodki[numer - 1]
                ninja.penup()
                ninja.goto(wspolrzedne)
                ninja.pendown()
                for j in range(1, len(wygrana)):
                    numer = wygrana[j]
                    wspolrzedne = srodki[numer - 1]
                    ninja.goto(wspolrzedne)
                ninja.penup()
                ninja.goto(0,325)
                ninja.pendown()
                ninja.write("Wygrałeś", align="center", font=("Times New Roman", 20, "normal"))
                flaga = 1
                break

        # komputer
        dostepne = [pole for pole in wolne if pole != 0]
        losowe_pole = random.choice(dostepne)

        if akcja == 1 and flaga == 0:
            przeciwnik(losowe_pole)
            index = wolne.index(losowe_pole)
            wolne[index] = 0
            akcja = 0

turtle.onscreenclick(klik)
turtle.done()