

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

# zmienne i funkcje
symbol = None
ilosc = 0
akcja = 0
blok = 1
srodki = [[-200,200], [0,200], [200,200], [-200,0], [0,0], [200,0], [-200,-200], [0,-200], [200,-200]]
wolne = [[-200,200], [0,200], [200,200], [-200,0], [0,0], [200,0], [-200,-200], [0,-200], [200,-200]]
wolne_numery = [1,2,3,4,5,6,7,8,9]
uzytkownik = []
komputer = []
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

# po kliknięciu
def klik(x, y):
    flaga_teraz = 0
    flaga_teraz2 = 0
    global symbol
    global wolne
    global wolne_numery
    global akcja
    global blok
    global uzytkownik
    global komputer
    global flaga
    global srodki

    if -550 <= x <= -450 and 200 <= y <= 300:
        symbol = "o"
        blok = 0
    if -400 <= x <= -300 and 200 <= y <= 300:
        symbol = "x"
        blok = 0

    # ruch użytkownika
    if blok == 0 and flaga == 0:
        # 1
        if -300 <= x <= -100 and 100 <= y <= 300 and wolne[0] != 0:
            rysunek(-200, 200)
            wolne[0] = 0
            wolne_numery[0] = 0
            akcja = 1
            uzytkownik += [1]
        # 2
        elif -100 <= x <= 100 and 100 <= y <= 300 and wolne[1] != 0:
            rysunek(0,200)
            wolne[1] = 0
            wolne_numery[1] = 0
            akcja = 1
            uzytkownik += [2]
        # 3
        elif 100 <= x <= 300 and 100 <= y <= 300 and wolne[2] != 0:
            rysunek(200,200)
            wolne[2] = 0
            wolne_numery[2] = 0
            akcja = 1
            uzytkownik += [3]
        # 4
        elif -300 <= x <= -100 and -100 <= y <= 100 and wolne[3] != 0:
            rysunek(-200,0)
            wolne[3] = 0
            wolne_numery[3] = 0
            akcja = 1
            uzytkownik += [4]
        # 5
        elif -100 <= x <= 100 and -100 <= y <= 100 and wolne[4] != 0:
            rysunek(0,0)
            wolne[4] = 0
            wolne_numery[4] = 0
            akcja = 1
            uzytkownik += [5]
        # 6
        elif 100 <= x <= 300 and -100 <= y <= 100 and wolne[5] != 0:
            rysunek(200,0)
            wolne[5] = 0
            wolne_numery[5] = 0
            akcja = 1
            uzytkownik += [6]
        # 7
        elif -300 <= x <= -100 and -300 <= y <= -100 and wolne[6] != 0:
            rysunek(-200,-200)
            wolne[6] = 0
            wolne_numery[6] = 0
            akcja = 1
            uzytkownik += [7]
        # 8
        elif -100 <= x <= 100 and -300 <= y <= -100 and wolne[7] != 0:
            rysunek(0,-200)
            wolne[7] = 0
            wolne_numery[7] = 0
            akcja = 1
            uzytkownik += [8]
        # 9
        elif 100 <= x <= 300 and -300 <= y <= -100 and wolne[8] != 0:
            rysunek(200,-200)
            wolne[8] = 0
            wolne_numery[8] = 0
            akcja = 1
            uzytkownik += [9]

        # sprawdzenie wygranej użytkownika
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

        # ruch komputera
        if flaga == 0:
            for j in range(len(zwyciestwa)):
                opcja = zwyciestwa[j]
                zajete_komputer = 0 
                zajete_uzytkownik = 0
                wolne_teraz = 0
                for k in range(len(opcja)):
                    if opcja[k] in komputer:
                        zajete_komputer += 1
                    elif opcja[k] in uzytkownik:
                        zajete_uzytkownik += 1
                    elif opcja[k] in wolne_numery:
                        wolne_teraz += 1
                        nr = opcja[k]
                if zajete_komputer == 2 and wolne_teraz == 1:
                    wybrane = wolne[nr - 1]
                    przeciwnik(wybrane)
                    index = wolne.index(wybrane)
                    wolne[index] = 0
                    wolne_numery[index] = 0
                    komputer += [nr]
                    flaga_teraz = 1
                    akcja = 0
                    break

            if flaga_teraz == 0:
                for m in range(len(zwyciestwa)):
                    opcja2 = zwyciestwa[m]
                    zajete_komputer2 = 0 
                    zajete_uzytkownik2 = 0
                    wolne_teraz2 = 0
                    for n in range(len(opcja2)):
                        if opcja2[n] in uzytkownik:
                            zajete_uzytkownik2 += 1
                        elif opcja2[n] in komputer:
                            zajete_komputer2 += 1
                        elif opcja2[n] in wolne_numery:
                            wolne_teraz2 +=1
                            nr2 = opcja2[n]
                    if zajete_uzytkownik2 == 2 and wolne_teraz2 == 1:
                        wybrane2 = wolne[nr2 - 1]
                        przeciwnik(wybrane2)
                        index = wolne.index(wybrane2)
                        wolne[index] = 0
                        wolne_numery[index] = 0
                        komputer += [nr2]
                        flaga_teraz2 = 1
                        akcja = 0
                        break

            if flaga_teraz2 == 0:
                dostepne = [pole for pole in wolne if pole != 0]
                if akcja == 1 and flaga == 0 and dostepne:
                    losowe_pole = random.choice(dostepne)
                    index = wolne.index(losowe_pole)
                    nr3 = wolne_numery[index]
                    przeciwnik(losowe_pole)
                    wolne[index] = 0
                    wolne_numery[index] = 0
                    komputer += [nr3]
                    akcja = 0

        # sprawdzwenie wygranej komputera
        for i in range(len(zwyciestwa)):
            kombinacja2 = zwyciestwa[i]
            wynik2 = all(liczba in komputer for liczba in kombinacja2)

            if wynik2 == True:
                wygrana2 = kombinacja2
                numer2 = wygrana2[0]
                wspolrzedne2 = srodki[numer2 - 1]
                ninja.penup()
                ninja.goto(wspolrzedne2)
                ninja.pendown()
                for j in range(1, len(wygrana2)):
                    numer2 = wygrana2[j]
                    wspolrzedne2 = srodki[numer2 - 1]
                    ninja.goto(wspolrzedne2)
                ninja.penup()
                ninja.goto(0,325)
                ninja.pendown()
                ninja.write("Wygrałem", align="center", font=("Times New Roman", 20, "normal"))
                flaga = 1
                break

        # sprawdzenie remisu
        if len(komputer) + len(uzytkownik) == 9 and flaga == 0:
            ninja.penup()
            ninja.goto(0,325)
            ninja.pendown()
            ninja.write("Remis", align="center", font=("Times New Roman", 20, "normal"))
            flaga = 1

turtle.onscreenclick(klik)
turtle.done()