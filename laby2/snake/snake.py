import random
import os.path
import pygame

# Kolory
backgroundColor = (255, 255, 255)
textColor = (255, 0, 0)
appleColor = (255, 0, 0)
black = (0, 0, 0)

# Uruchamianie okna
x = pygame.init()
# Ustawianie rozmiaru okna
width_of_screen = 900
height_of_screen = 600
gameWindow = pygame.display.set_mode((width_of_screen, height_of_screen))
# Ustawianie i aktualizowanie tytułu
pygame.display.set_caption("snake game-PythonGeeks")
pygame.display.update()

# Tworzenie zegara dla gry
clock = pygame.time.Clock()
# Ładowanie domyślnej systemowej czcionki
font = pygame.font.SysFont(None, 55)


# Wyświetlanie tekstu na ekranie
def text_on_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])


# Wyświetlanie węża
def plot_snake(gameWindow, color, snake_list, snake_size):
    # snake_list jest listą pozycji poszczególnych części węża. Każda część
    # jest wyświetlana graficzna jako kwadrat o szerokości i wysokości snake_size
    for (x, y) in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Ekran powitania
def welcome():
    game_exit = False

    # Nieskończona pętla aktualizująca okno, do póki
    # nie będziemy chcieli wyjść
    while not game_exit:
        gameWindow.fill((255, 182, 193))
        text_on_screen("Welcome to snakes game by PythonGeeks", black, 90, 250)
        text_on_screen("Press spacebar to play", black, 232, 290)
        for event in pygame.event.get():
            # Wyjdź jeżeli aplikacja chce wyjść
            if event.type == pygame.QUIT:
                game_exit = True
            # Jeżeli spacja została naciśnięta, uruchom grę
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        # Zaktualizuj okno
        pygame.display.update()
        # Poczekaj z renderowaniem, tak żeby było 60 fps
        clock.tick(60)


# Gra
def game():
    game_exit = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    score = 0
    apple_x = random.randint(20, width_of_screen // 2)
    apple_y = random.randint(20, height_of_screen // 2)
    snake_size = 30
    snake_list = []
    snake_length = 1
    fps = 40

    # Ładowanie highscore
    if os.path.isfile("highscore.txt"):
        with open("highscore.txt", "r") as f:
            highscore = f.read()
    else:
        highscore = "0"

    while not game_exit:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
            gameWindow.fill(backgroundColor)
            text_on_screen("Game Over! Press Enter to continue", textColor, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                # Zamykanie aplikacji, jeżeli chce się zamknąć
                if event.type == pygame.QUIT:
                    game_exit = True
                # Sterowanie wężem
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            # Zmiemianie pozycji węża
            snake_x += velocity_x
            snake_y += velocity_y

            # Wykrywanie czy jesteśmy na jabłku
            if abs(snake_x - apple_x) < 20 and abs(snake_y - apple_y) < 20:
                score += 10
                apple_x = random.randint(20, width_of_screen // 2)
                apple_y = random.randint(20, height_of_screen // 2)
                snake_length += 5
                if score > int(highscore):
                    highscore = score

            # Wyświetlanie grafiki
            gameWindow.fill(backgroundColor)
            text_on_screen("Score: " + str(score) + " highscore: " + str(highscore), textColor, 5, 5)
            pygame.draw.rect(gameWindow, appleColor, [apple_x, apple_y, snake_size, snake_size])

            # Aktualizowanie długości węża
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del snake_list[0]

            # Kończymy grę, jeżeli jesteśmy głową w miejscu gdzie jest już nasz tłów
            # snake_list[:-1] - dwukropek pozwala nam wybrać pod-listę listy snake_list
            # która zawiera wszystkie części naszego węża. ujemne liczby oznaczają odliczanie
            # od końca. -1 oznacza przedostatni element. Czyli bierzemy pod-listę od 0 (gdy
            # przed dwukropkiem nic nie ma, oznacza to zero) do przed-ostatniego elementu.
            #
            # Robimy to, bo ostatnim elementem zawsze jest głowa, którą dodawaliśmy
            # kodem powyżej.
            if head in snake_list[:-1]:
                game_over = True

            # Jeżeli udeżyliśmy o któryś z końców ekranu, przegrywamy
            if (snake_x < 0 or snake_x > width_of_screen or snake_y < 0 or snake_y > height_of_screen):
                game_over = True

            # Wyświetlanie węża
            plot_snake(gameWindow, black, snake_list, snake_size)
            pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])

        # Zaktualizuj okno
        pygame.display.update()

        # Poczekaj z renderowaniem, tak żeby zachować ilość klatek na sekunde
        clock.tick(fps)

    # Kod, gdy opuścimy główną pętlę i będziemy chcieli wyjść z aplikacji
    pygame.quit()
    quit()


# Wyświetlanie ekranu powitania na start
welcome()
