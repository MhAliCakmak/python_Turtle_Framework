choose = int(input("kac köşeli olsun"))
import turtle as tr
from random import sample
def köse(a):
    var = (choose - 2) * 180 / choose
    for i in range(choose):
        ok.forward(a)
        ok.left(180 - var)
my_color = ["red", "blue", "yellow", "cyan", "green", "purple"]
ok = tr.Turtle()
ok.speed(0)
kenar = 10
ok.pencolor("red")
for i in range(100):
    istek = sample(my_color, 1)
    ok.color(istek)
    köse(kenar)
    kenar = kenar + 5
    ok.right(20)
