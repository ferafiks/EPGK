# Program z poradnika
# https://pythongeeks.org/python-dice-rolling-simulator/

# Importowanie bibliotek
import tkinter
from PIL import Image, ImageTk
import random

# Definiowanie obrazków kości
dice = [
    "dice1.png",
    "dice2.png",
    "dice3.png",
    "dice4.png",
    "dice5.png",
    "dice6.png",
]

# Tworzenie okna "root" i zmienianie jego rozmiaru i tytułu
root = tkinter.Tk()
root.geometry("400x400")
root.title("PythonGeeks-Roll the Dice")

# Tworzenie elementu, który będzie wyświetlał nasz obrazek
imageLabel = tkinter.Label(root)
# Dodawanie elementu do okna
imageLabel.pack(expand=True)


# Funkcja do
def roll_dice():
    # Dzięki tej linijsce, diceImage staje się zmienną globalną,
    # co oznacza, że jej wartość będzie zachowywana poza tą funkcją.
    # Musimy to zrobić, by nasz nowo stworzony obrazek nie został
    # usunięty z pamięci po zakończeniu funkcji.
    global diceImage

    # Wybieranie losowego obrazka
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # Aktualizowanie obrazka w elemencie, który go wyświetla
    imageLabel.configure(image=diceImage)


# Losowanie obrazka na start, by nie wyświetlać pustego miejsca
roll_dice()

# Tworzenie guzika do losowania kostki
button = tkinter.Button(root, text="Roll the dice", fg="green", command=roll_dice)
# Dodawanie guzika do okna
button.pack(expand=True)

# Uruchamianie okna
root.mainloop()
