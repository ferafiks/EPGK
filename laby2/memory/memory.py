# Importowanie
import random
import pygame
import sys
from pygame.locals import *

# Definiowanie ustawień gry
# Ile milisekund trwa jedna klatka. Łatwo obliczyć z wzoru: 1000/fps
# W tym przypadku 30 oznacza ~33fps
Frame_Speed = 30
# Rozmiary okna
Window_Width = 640
Window_Height = 480
# Prędkość animacji odkrywania i zakrywania pól
Speed_Reveal = 8
# Rozmiar jednego pola w pikselach
Box_Size = 40
# Rozmiar przestrzeni między polami w pikselach
Gap_Size = 10
# Ile pól jest w 1 rzędzie
Board_Width = 10
# Ile pól jest w 1 kolumnie
Board_Height = 7

# Sprawdzanie, czy jest parzysta ilość pól
# (ciężko stworzyć pary przy nieparzystej liczbie pól)
assert (Board_Width * Board_Height) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

# Obliczanie marginesu wokół planszy
X_margin = int((Window_Width - (Board_Width * (Box_Size + Gap_Size))) / 2)
Y_margin = int((Window_Height - (Board_Height * (Box_Size + Gap_Size))) / 2)

# Definiowanie kolorów kształtów
#            R    G    B
Gray     = (100, 100, 100)
Navyblue = ( 60,  60, 100)
White    = (255, 255, 255)
Red      = (255,   0,   0)
Green    = (  0, 255,   0)
Blue     = (  0,   0, 255)
Yellow   = (255, 255,   0)
Orange   = (255, 128,   0)
Purple   = (255,   0, 255)
Cyan     = (  0, 255, 255)

# Definiowanie kolorów ogólnych
BackGround_color = Gray
Light_BackGround_color = Navyblue
Box_Color = Cyan
HighLight_Color = Yellow

# Definiowanie kształtów.
# Nazwa wpisana w ich wartość nie jest istotna. Ważne jest tylko
# to, żeby żaden kształt nie miał takiej samej
CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

# Zapisywanie zdefiniowanych kolorów w tablicy
All_Colors = (Red, Green, Blue, Yellow, Orange, Purple, Cyan)
# Zapisywanie zdefiniowanych kształtów w tablicy
All_Shapes = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)

# Sprawdzanie czy jest na tyle kombinacji kolorów i kształtów, żeby dało
# się wygenerować plansze
assert len(All_Colors)* len(All_Shapes) * 2 >= Board_Width * Board_Height, "Board is too big for the number of shapes/colors defined."



# Główna funkcja programu
def main():
    # Inicjalizacia pygame
    pygame.init()

    # Definiowanie globalnych
    # Frame_Speed_Clock - główny zegar gry
    # DIS_PlaySurf - reprezentuje obraz w oknie (surface) - to w nim będziemy
    # rysować grafikę programu
    global Frame_Speed_Clock, DIS_PlaySurf
    Frame_Speed_Clock = pygame.time.Clock()
    DIS_PlaySurf = pygame.display.set_mode((Window_Width, Window_Height))

    # Definiowanie koordynatów myszki
    X_mouse = 0
    Y_mouse = 0

    # Ustawianie tytułu okna
    pygame.display.set_caption('Memory Game by PythonGeeks')

    # Tworzenie planszy z losowymi elementami do odkrycia
    Board = Randomized_Board()
    # Tworzenie tablicy przechowującej dane o tym które pola
    # zostały odsłonięte
    Boxes_revealed = GenerateData_RevealedBoxes(False)

    # Zmienna przechowująca numer pola które jest odsłonięte
    # na czas szukania pary do niego
    first_Selection = None


    DIS_PlaySurf.fill(BackGround_color)

    # Rozpoczynanie gry
    # Funkcja głównie odpowiedzialna za początkową animację
    Start_Game(Board)

    # Główna pętla programu
    while True:
        mouse_Clicked = False

        # Rysowanie grafiki
        DIS_PlaySurf.fill(BackGround_color)
        Draw_Board(Board, Boxes_revealed)

        # Wykrywanie eventów
        for event in pygame.event.get():
            # Jeżeli aplikacja chce wyjść lub nacisneliśmy Escape
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            # Jeżeli położenie myszki zmieniło się
            elif event.type == MOUSEMOTION:
                X_mouse, Y_mouse = event.pos
            # Jeżeli kliknęliśmy myszką
            elif event.type == MOUSEBUTTONUP:
                X_mouse, Y_mouse = event.pos
                mouse_Clicked = True

        # Zaznaczanie pola myszką
        # Jeżeli koordynaty w tablicy pola nie są równe None
        # to oznacza, że myszka leży na jakimś polu
        x_box, y_box = Box_Pixel(X_mouse, Y_mouse)
        if x_box != None and y_box != None:
            # Jeżeli pole jest wciąż zasłonięte, rysujemy otoczkę
            # wokół niego
            if not Boxes_revealed[x_box][y_box]:
                Draw_HighlightBox(x_box, y_box)

            # Jeżeli pole jest wciąż zasłonięte oraz klikneliśmy
            # na nie, odsłaniamy je
            if not Boxes_revealed[x_box][y_box] and mouse_Clicked:
                # Odsłanianie pola
                Reveal_Boxes_Animation(Board, [(x_box, y_box)])
                Boxes_revealed[x_box][y_box] = True

                # Jeżeli klikneliśmy dopiero pierwsze pole w parze,
                # zapisujemy je i czekamy aż klikniemy następne.
                # Jeżeli nie, to robimy to co jest po else
                if first_Selection == None:
                    first_Selection = (x_box, y_box)
                else:
                    # Odczyutjemy kolor i kształt zaznaczonych pól
                    icon1shape, icon1color = get_Shape_Color(Board, first_Selection[0], first_Selection[1])
                    icon2shape, icon2color = get_Shape_Color(Board, x_box, y_box)
                    # Jeżeli para jest nie zgodna, pokazujemy pola przez chwilę
                    # a następnie ponownie je zakrywamy
                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Pokazujemy wynik przez 1 sekundę (1000 milisekund)
                        pygame.time.wait(1000)
                        # Animacja zakrywania obydwu pól
                        Cover_Boxes_Animation(Board, [(first_Selection[0], first_Selection[1]), (x_box, y_box)])
                        # Zapisywanie pól jako zakryte
                        Boxes_revealed[first_Selection[0]][first_Selection[1]] = False
                        Boxes_revealed[x_box][y_box] = False
                    # Jeżeli para była zgodna oraz odkryliśmy już wszystko,
                    # kończymy grę
                    elif Won(Boxes_revealed):
                        Game_Won(Board)
                        pygame.time.wait(2000)

                        Board = Randomized_Board()
                        Boxes_revealed = GenerateData_RevealedBoxes(False)

                        Draw_Board(Board, Boxes_revealed)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        Start_Game (Board)
                    first_Selection = None

        pygame.display.update()
        Frame_Speed_Clock.tick(Frame_Speed)



# Tworzenie 2 wymiarowej tablicy dla każdego elementu planszy
# i wypełnianie go wartością val
def GenerateData_RevealedBoxes(val):
    Boxes_revealed = []
    for i in range(Board_Width):
        Boxes_revealed.append([val] * Board_Height)
    return Boxes_revealed



# Tworzenie planszy
def Randomized_Board():
    # Tworzenie listy z wszystkimi ikonami wszystkich kolorów
    icon = []
    for color in All_Colors:
        for shape in All_Shapes:
            icon.append( (shape, color) )

    # Tasowanie ich kolejności
    random.shuffle(icon)
    # Kalkulowanie potrzebną liczbę rodzaji elementów (pół ilości elementów na planszy)
    num_IconsUsed = int(Board_Width * Board_Height / 2)
    # Tworzenie ostatecznej listy z potasowanymi wszystkimi elementami na planszy
    # Mnożymy razy dwa, bo chcemy, żeby każdy element miał swoją parę
    icon = icon[:num_IconsUsed] * 2
    random.shuffle(icon)

    # Wypełmnianie planszy
    # board - lista z kolumnami
    # column - lista z elementami kolumny
    board = []
    for x in range(Board_Width):
        column = []
        for y in range(Board_Height):
            # Dodawanie pierwszego elememntu z brzegu i usuwanie go
            # z listy dostępnych elementów
            column.append(icon[0])
            del icon[0]

        # Dodawanie kolumny do listy
        board.append(column)
    return board


# Funkcja pomocnicza do podzielenia listy na mniejsze pod-listy o danym rozmiarze
# Używana na początku by chwilowo odsłonić kawałki planszy
def Split_Groups(group_Size, List):
    result = []
    for i in range(0, len(List), group_Size):
        result.append(List[i:i + group_Size])
    return result


# Funkcja pomocnicza do znalezienia koordynatów lewego górnego rogu w oknie
# (np. 483x902) dla danego pola w tablicy (np. 2x3)
def leftTop_Coord(x_box, y_box):
    left = x_box * (Box_Size + Gap_Size) + X_margin
    top = y_box * (Box_Size + Gap_Size) + Y_margin
    return (left, top)


# Funkcja pomocnicza do znalezienia koordynatów pola w tablicy (np. 2x3)
# z koordynatów okna (np. 483x902)
def Box_Pixel(x, y):
    for x_box in range(Board_Width):
        for y_box in range(Board_Height):
            left, top = leftTop_Coord(x_box, y_box)
            box_Rect = pygame.Rect(left, top, Box_Size, Box_Size)
            if box_Rect.collidepoint(x, y):
                return (x_box, y_box)
    return (None, None)


# Rysowanie kształtu
def Draw_Icon(shape, color, x_box, y_box):
    # Obliczanie ćwiartki i połowy rozmiaru jednego pola
    quarter = Box_Size // 4
    half = Box_Size // 2

    # Obliczanie koordynatów pola w którym będziemy rysować kształt
    left, top = leftTop_Coord(x_box, y_box)

    # Rysowanie kształtu w zależności od rodzaju
    if shape == CIRCLE:
        # Rysowanie kółka polega na narysowaniu dwóch kółek
        # od środka pola, gdzie jedno jest koloru pola, aby
        # rezultat wyglądał jak pączek
        pygame.draw.circle(DIS_PlaySurf, color, (left + half, top + half), half - 5)
        pygame.draw.circle(DIS_PlaySurf, BackGround_color, (left + half, top + half), quarter - 5)
    elif shape == SQUARE:
        # Rysowanie kwadratu polega na rysowaniu recta
        # z przesuniętego o ćwiartkę lewego górnego rogu
        # o rozmiarze połowy pola
        pygame.draw.rect(DIS_PlaySurf, color, (left + quarter, top + quarter, half, half))
    elif shape == DIAMOND:
        # Rysowanie diamentu polega na narysowaniu polygona przechodzącego
        # przez 4 punkty: góra, prawo, dół, lewo
        pygame.draw.polygon(DIS_PlaySurf, color, ((left + half, top), (left + Box_Size - 1, top + half), (left + half, top + Box_Size - 1), (left, top + half)))
    elif shape == LINES:
        # Rysowanie lini w skos
        # 4 w range oznacza, że i będzie przeskakiwać o 4
        # czyli i będzie miało wartości 0, 4, 8, ...
        for i in range(0, Box_Size, 4):
            pygame.draw.line(DIS_PlaySurf, color, (left, top + i), (left + i, top))
            pygame.draw.line(DIS_PlaySurf, color, (left + i, top + Box_Size - 1), (left + Box_Size - 1, top + i))
    elif shape == OVAL:
        # OVAL jest elipsą zajmującą całą szerokość pola i połowę wysokości
        # Zaczynamy od lewego górnego rogu i rysujemy w nim elipse
        # Y musi zostać przesunięty o ćwiartkę, by wyśrodkować nasz kształt
        pygame.draw.ellipse(DIS_PlaySurf, color, (left, top + quarter, Box_Size, half))


# Funkcja pomocnicza do odczytywania kształtu i koloru ikony
# znajdującej się na danym polu
def get_Shape_Color(board, x_box, y_box):
    return board[x_box][y_box][0], board[x_box][y_box][1]


# Rysowanie pola zakrytego po części w zależności od coverage
# coverage = 1.0 → całkowicie zakryte
# coverage = 0.0 → całkowicie odkryte
def Box_Cover(board, boxes, coverage):
    # Przechodzenie przez wszystkie pola które mamy narysować
    for box in boxes:
        # Kalkulowanie koordynatów na ekranie pola
        left, top = leftTop_Coord(box[0], box[1])
        # Rysowanie tła w miejsce pola
        pygame.draw.rect(DIS_PlaySurf, BackGround_color, (left, top, Box_Size, Box_Size))
        # Odczytywanie kolor i kształ ikony znajdujący się w polu
        shape, color = get_Shape_Color(board, box[0], box[1])
        # Rysowanie ikony w polu
        Draw_Icon(shape, color, box[0], box[1])
        # Jeżeli pole nie jest całkowicie odsłonięte, rysujemy zasłone
        if coverage > 0:
            pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, coverage, Box_Size))

    # Aktualizowanie okna i czekanie przez 1 klatkę
    pygame.display.update()
    Frame_Speed_Clock.tick(Frame_Speed)


# Funkcja odtwarzająca animacje odkrywania wybranych pól
def Reveal_Boxes_Animation(board, boxesToReveal):
    # Przechodzenie przez każdą klatkę animacji
    # Co klatkę, wartość coverage zmienia się o -Speed_Reveal
    # które jest 3 argumentem range
    for coverage in range(Box_Size, (-Speed_Reveal) - 1, -Speed_Reveal):
        # Rysowanie pola
        Box_Cover(board, boxesToReveal, coverage)


# Funkcja odtwarzająca animacje zakrywania wybranych pól
def Cover_Boxes_Animation(board, boxesToCover):
    # Przechodzenie przez każdą klatkę animacji
    # Co klatkę, wartość coverage zmienia się o Speed_Reveal
    # które jest 3 argumentem range
    for coverage in range(0, Box_Size + Speed_Reveal, Speed_Reveal):
        # Rysowanie pola
        Box_Cover(board, boxesToCover, coverage)


# Rysowanie planszy
def Draw_Board(board, revealed):
    # Przechodzimy przez wszystkie kolumny
    for x_box in range(Board_Width):
        # Przechodzimy przez wszystkie pola
        for y_box in range(Board_Height):
            # Kalkulujemy koordynaty lewego górnego rogu pola
            left, top = leftTop_Coord(x_box, y_box)
            # Jeżeli pole jest dalej zakryte, rysujemy błękitny kwadrat
            if not revealed[x_box][y_box]:
                pygame.draw.rect(DIS_PlaySurf, Box_Color, (left, top, Box_Size, Box_Size))
            # W przeciwnym wypadku, rysujemy kształt, który znajduje się w polu
            else:
                shape, color = get_Shape_Color(board, x_box, y_box)
                Draw_Icon(shape, color, x_box, y_box)


# Rysowanie otoczki wokół pola nad którym jest myszka
def Draw_HighlightBox(x_box, y_box):
    left, top = leftTop_Coord(x_box, y_box)
    # Rysowanie kwadratu pustego w środku
    pygame.draw.rect(DIS_PlaySurf, HighLight_Color, (left - 5, top - 5, Box_Size + 10, Box_Size + 10), 4)


# Rozpoczynanie gry
def Start_Game(board):

    covered_Boxes = GenerateData_RevealedBoxes(False)
    boxes = []
    for x in range(Board_Width):
        for y in range(Board_Height):
            boxes.append( (x, y) )
    random.shuffle(boxes)
    box_Groups = Split_Groups(8, boxes)

    Draw_Board(board, covered_Boxes)
    for boxGroup in box_Groups:
        Reveal_Boxes_Animation(board, boxGroup)
        Cover_Boxes_Animation(board, boxGroup)


# Wyświetlanie animacji wygranej gry
def Game_Won (board):
    # Tworzymy listę z stanem gry w którym wszystkie pola
    # są odkryte
    coveredBoxes = GenerateData_RevealedBoxes(True)
    # Kolory tła, które będziemy wyświetlać naprzemian
    color_1 = Light_BackGround_color
    color_2 = BackGround_color

    # Animacja wygranej będzie trwała przez 13 zamian koloru tła
    for i in range(13):
        # Podmieniamy kolory tła i rysujemy tło
        (color_1, color_2) = (color_2, color_1)
        DIS_PlaySurf.fill(color_1)
        # Rysowanie planszy
        Draw_Board(board, coveredBoxes)

        # Aktualizowanie okna i czkeanie przez 3/10 sekundy (300 milisekund)
        pygame.display.update()
        pygame.time.wait(300)

# Funkcja sprawdzająca czy wygraliśmy
def Won(Boxes_revealed):
    # Sprawdzamy wszystkie kolumny
    for i in Boxes_revealed:
        # Jeżeli w jakiejkolwiek kolumnie jest zakryte pole,
        # zwracamy False (czyli, że nie wygraliśmy jeszcze)
        if False in i:
            return False

    # Jeżeli wszystkie pola są odkryte, zwracamy True
    return True


# Jeżeli skrypt został uruchomiony a nie zaimportowany
# do innego skryptu, wywołaj funkcję main
if __name__ == '__main__':
    main()