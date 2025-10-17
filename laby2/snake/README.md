# Snake

## WAŻNE

Gra ma funkcję zapisywania highscora w pliku `highscore.txt`. Plik ten jest zapisywany w folderze z którego uruchamia się skrypt. Czyli, jeżeli uruchomi się go z folderu `laby2`, plik `highscore` zostanie w nim zapisany. Ostrzegam, byście sobie nie zaśmiecili komputera.

## PyGame

Gra ta kożysta z biblioteki pygame do tworzenia okna i wyświetlania grafiki. W razie jakiś pytań można łatwo wyszukać odpowiedź w dokumentacji pygame'a albo w wyszukiwarce zawierając w pytaniu `pygame`.

## Problemy z wersją na UPEL

Wąż z upela nie działa z 2 powodów:
1. Plik `highscore.txt` nie istnieje
2. Inty (liczby całe) zamieniają się na floaty (liczby dziesiętne) przy dzieleniu.

Ta wersja nie wczytuje pliku `highscore.txt` jeżeli nie istnieje oraz zamieniła wszystkie znaki `/` przy dzieleniu liczb całkowitych na `//` (`/` zawsze zwraca liczbe dziesiętną, a `//` liczbę całkowitą nie zależnie od tego jakiego typu są liczby które się dzieli).
