# Memory

Chyba największa przykładowa gra ze wszystkich (przynajmniej mi zajęło trochę z okomentowaniem).

## Jak tworzyć nowe ikony

Program automatycznie tworzy listę losowych ikon z listy kolorów i kształtów, które są zdefiniowane na początku skryptu.

Dodawanie (lub modyfikowanie) nowych kolorów jest proste. Trzeba dodać nową zmienną i zapisać w niej kolor tak jak w innych, a potem dodać ją do listy `All_Colors` znajdującej się troszeczkę niżej.

Kształty natomiast są trochę bardziej skomplikowane. Koło kolorów są też wypisane kształty które później są przypisywane do listy `All_Shapes`, jednak wartości tych zmiennych nie mają większego znaczenia (można nawet je zmienić, byle żeby się od siebie różniły). Zeby kształt był poprawnie rysowany na ekranie, trzeba jeszcze dodać kod do rysowania go w funkcji `Draw_Icon` (linijka 262). Polecam sugerowanie się kodem do innych kształtów.
