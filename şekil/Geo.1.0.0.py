choose=int(input("kac köşeli olsun"))
import turtle as tr
def Köse():
    ok = tr.Turtle()
    var = (choose - 2) * 180 / choose
    for i in range(choose):
        ok.forward(100)
        ok.left(180-var)
Köse()

