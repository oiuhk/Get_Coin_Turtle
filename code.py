from turtle import Turtle
from random import randint

class Sprite(Turtle):
    ''' Основной класс - движающая черепашка '''
    def __init__(self, x: int, y: int, shp: str = "classic", clr: str = 'black') -> None:
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.left(180)
        self.step = 10
        self.points = 0
    
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(), sprite.ycor())
        if dist < 20:
            return True
        return False
    
    def move_right(self):
        self.goto(self.xcor() + self.step, self.ycor())

    def move_left(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.step)
    

class Enemy(Sprite):
    ''' Подвижные боты '''
    def __init__(self, x: int, y: int, shp: str = "turtle", clr: str = 'black') -> None:
        Sprite.__init__(self, x, y, shp, clr)
        self.goto(x, y)
        self.color(clr)
        self.shape(shp)
        self.step = 10
        self.speed(20)

    def move_forward(self) -> None:
        self.goto(self.xcor(), self.ycor() + self.step)
    
    def move_back(self) -> None:
        self.goto(self.xcor(), self.ycor() - self.step)

    def move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start
        
        self.x_end = x_end
        self.y_end = y_end
        
        self.goto(x_start, y_start)

        self.setheading(self.towards(x_end, y_end))
    
    def make_step(self):
        self.forward(self.step)

        if self.distance(self.x_end, self.y_end) < self.step:
            self.move(self.x_end, self.y_end, self.x_start, self.y_start)
            

def main():
    player = Sprite(x=170, y=160, shp='turtle', clr='green')

    scr = player.getscreen()
    
    coin = Sprite(x=-200, y=-200, shp='circle', clr='yellow')

    bot1 = Enemy(x=-200, y=100, shp='triangle', clr='red')
    bot2 = Enemy(x=200, y=-100, shp='triangle', clr='red')
    bot3 = Enemy(x=-140, y=-185, shp='triangle', clr='red')

    bot1.move(x_start=-200, y_start=100, x_end=200, y_end=100)
    bot2.move(x_start=200, y_start=-100, x_end=-120, y_end=-100)
    bot3.move(x_start=-140, y_start=-185, x_end=-140, y_end=150)
    
    score = 0

    scr.onkey(player.move_right,'Right')
    scr.onkey(player.move_left,'Left')
    scr.onkey(player.move_up,'Up')
    scr.onkey(player.move_down,'Down')

    scr.listen()

    while score < 3:
        bot1.make_step()
        bot2.make_step()
        bot3.make_step()

        if player.is_collide(coin):
            score += 1
            coin.goto(randint(-80, 80), randint(-80, 80))

        if player.is_collide(bot1 or bot2 or bot3):
            coin.hideturtle()
            break

    if score == 3:
        bot1.hideturtle()
        bot2.hideturtle()
        bot3.hideturtle()
        


    player.done()



if __name__ == '__main__':
    main()
