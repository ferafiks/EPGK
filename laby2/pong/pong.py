import turtle as tl

class PONG:
    # Wywoływane przy tworzeniu nowej instancji klasy
    # Czyli gdy wywołamy PONG()
    # Robimy wszystko na obiekcie self dołączonym
    # jako argument funkcji. W nim tworzymy zmienne
    # i wywołujemy funkcje.
    def __init__(self):
        self.create_window()
        self.leftpaddle()
        self.rightpaddle()
        self.create_ball()
        self.keys()
        self.game()
    def create_window(self):
        self.root = tl.Screen()
        self.root.title("PONG GAME by PythonGeeks")
        self.root.bgcolor("yellow")
        self.root.setup(width=600, height=400)

        # Wyłączenie automatycznego odświeżania okna
        self.root.tracer(0)
    def leftpaddle(self):
        self.left_paddle = tl.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape('square')
        self.left_paddle.color('red')
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)
    def rightpaddle(self):
        self.right_paddle = tl.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape('square')
        self.right_paddle.color('white')
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.right_paddle.penup()
        self.right_paddle.goto(280, 0)
    def create_ball(self):
        self.ball = tl.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('green')
        self.ball.penup()
        self.ball.goto(5,5)
        self.ball_direction_x = 0.2
        self.ball_direction_y = 0.2
    def left_paddle_up(self):
        y = self.left_paddle.ycor()
        y = y + 20
        self.left_paddle.sety(y)
    def left_paddle_down(self):
        y = self.left_paddle.ycor()
        y = y - 20
        self.left_paddle.sety(y)
    def right_paddle_up(self):
        y = self.right_paddle.ycor()
        y = y + 20
        self.right_paddle.sety(y)
    def right_paddle_down(self):
        y = self.right_paddle.ycor()
        y = y - 20
        self.right_paddle.sety(y)
    # Kontrolowanie paletkami
    def keys(self):
        self.root.listen()
        self.root.onkeypress(self.left_paddle_up, "w")
        self.root.onkeypress(self.left_paddle_down, "s")
        self.root.onkeypress(self.right_paddle_up, "Up")
        self.root.onkeypress(self.right_paddle_down, "Down")
    def game(self):
        # Główna pętla gry
        while True:
            self.root.update()

            # Poruszanie piłką
            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            # Odbijanie się od sufitu
            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball_direction_y *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball_direction_y *= -1

            # Restartowanie, jeżeli piłka dotknęła bocznych krawędzi ekranu
            if self.ball.xcor() > 260:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            if self.ball.xcor() < -260:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            # Odbijanie się od prawej paletki
            if (self.ball.xcor() > 210) and (self.ball.xcor() < 220) and (
                    self.ball.ycor() < self.right_paddle.ycor() + 40 and self.ball.ycor() > self.right_paddle.ycor() - 40):
                self.ball.setx(210)
                self.ball_direction_x *= -1

            # Odbijanie się od lewej paletki
            if (self.ball.xcor() < -210) and (self.ball.xcor() > -220) and (
                    self.ball.ycor() < self.left_paddle.ycor() + 40 and self.ball.ycor() > self.left_paddle.ycor() - 40):
                self.ball.setx(-210)
                self.ball_direction_x *= -1


# Główna funkcja programu
def main():
    # Utworzenie nowego obiektu typu PONG, który
    # został zdefiniowany powyżej
    # Samo utworzenie tego obiektu uruchomi naszą grę.
    PONG()

# Jeżeli skrypt został uruchomiony a nie zaimportowany
# do innego skryptu, wywołaj funkcję main
if __name__ == '__main__':
    main()

