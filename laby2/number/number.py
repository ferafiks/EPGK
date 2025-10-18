# Importowanie
import tkinter as tk
from tkinter import *
import random

# Tworzenie okna o rozdzielczości 750x750 i tytule "Guess the number 2"
win = tk.Tk()
win.geometry("750x750")
win.title("Guess the number 2")

# Tworzenie wartości które będą wyświetlane w oknie
hint = StringVar()
score = IntVar()
final_score= IntVar()
guess= IntVar()

# Losowanie liczby
num=random.randint(1,50)

# Ustawianie początkowych wartości
hint.set("Guess a number between 1 to 50")
score.set(5)
final_score.set(score.get())

def fun():
    # Zczytywanie wpisanej liczby
    x=guess.get()
    # Ustawianie tury
    final_score.set(score.get())

    # Sprawdzanie liczby, jeżeli jeszcze nie przegraliśmy
    if score.get() > 0:
        # Jeżeli zgadywana liczba jest poza zakresem 0-50
        if x > 50 or x < 0:
            hint.set("You just lost 1 Chance")
            score.set(score.get()-1)
            final_score.set(score.get())

        # Jeżeli zgadywana liczba została trafiona
        elif num==x:
            hint.set("Congratulation YOU WON!!!")
            score.set(score.get()-1)
            final_score.set(score.get())

        # Jeżeli zgadywana liczba jest mniejsza
        elif num > x:
            hint.set("Your guess was too low: Guess a number higher ")
            score.set(score.get()-1)
            final_score.set(score.get())

        # Jeżeli zgadywana liczba jest większa
        elif num < x:
            hint.set("Your guess was too High: Guess a number Lower ")
            score.set(score.get()-1)
            final_score.set(score.get())
    else:
        # Wyświetlanie tekstu przegranej jeżeli skończyły nam się tury
         hint.set("Game Over You Lost")

# Stwórz nagłówek z tekstem i czcionką Courier o rozmiarze 25, a następnie umieść go w koordynatach 0.5x0.09
Label(win, text="I challange you to guess the number", font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)

# Stwórz pole do pisania dla wartości guess i czcionką Ubuntu o rozmiarze 50, a następnie umieść go w koordynatach 0.5x0.3
Entry(win, textvariable=guess, width=3,font=("Ubuntu", 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)

# Stwórz guzik "CHECK" z czcionką Courier o rozmiarze 25 i niebieskim tłem, który uruchamia funckej "fun", a następnie
# umieść go w koordynatach 0.5x0.5
Button(win, width=8, text="CHECK", font=("Courier", 25), command=fun, relief=GROOVE,bg="light blue").place(relx=0.5, rely=0.5, anchor=CENTER)

# Stwórz pomarańczowe pole do pisania dla wartości hint i czionką Courier o rozmiarze 15, a następnie umieść go w
# koordynatach 0.5x0.7
Entry(win, textvariable=hint, width=50,font=("Courier", 15), relief=GROOVE,bg="orange").place(relx=0.5, rely=0.7, anchor=CENTER)

# Stwórz nagłówek z tekstem i czcionką Courier o rozmiarze 25, a następnie umieść go w 0.3x0.85
Label(win, text="Score out of 5",font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)

# Stwórz pole do pisania dla wartości final_score i czionką Ubuntu o rozmiarze 24, a następnie umieść go w koordynatach
# 0.61x0.85
Entry(win, textvariable=final_score, width=2,font=("Ubuntu", 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)

# Uruchamianie okna
win.mainloop()
