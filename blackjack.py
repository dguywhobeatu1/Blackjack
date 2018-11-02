from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset
import random

run = 0

#print(len(cards))

class cardback(Sprite):
    cardback = ImageAsset("gray_back.png")
    def __init__(self,  position):
        super().__init__(cardback.cardback, position)


#hearts

class H2(Sprite):
    H2 = ImageAsset("2H.png")
    def __init__(self,  position):
        super().__init__(H2.H2, position)
class H3(Sprite):
    H3 = ImageAsset("3H.png")
    def __init__(self,  position):
        super().__init__(H3.H3, position)
class H4(Sprite):
    H4 = ImageAsset("4H.png")
    def __init__(self,  position):
        super().__init__(H4.H4, position)
class H5(Sprite):
    H5 = ImageAsset("5H.png")
    def __init__(self,  position):
        super().__init__(H5.H5, position)
class H6(Sprite):
    H6 = ImageAsset("6H.png")
    def __init__(self,  position):
        super().__init__(H6.H6, position)
class H7(Sprite):
    H7 = ImageAsset("7H.png")
    def __init__(self,  position):
        super().__init__(H7.H7, position)
class H8(Sprite):
    H8 = ImageAsset("8H.png")
    def __init__(self,  position):
        super().__init__(H8.H8, position)
class H9(Sprite):
    H9 = ImageAsset("9H.png")
    def __init__(self,  position):
        super().__init__(H9.H9, position)
class H10(Sprite):
    H10 = ImageAsset("10H.png")
    def __init__(self,  position):
        super().__init__(H10.H10, position)
class JH(Sprite):
    JH = ImageAsset("JH.png")
    def __init__(self,  position):
        super().__init__(JH.JH, position)
class QH(Sprite):
    QH = ImageAsset("QH.png")
    def __init__(self,  position):
        super().__init__(QH.QH, position)
class KH(Sprite):
    KH = ImageAsset("KH.png")
    def __init__(self,  position):
        super().__init__(KH.KH, position)
class AH(Sprite):
    AH = ImageAsset("AH.png")
    def __init__(self,  position):
        super().__init__(AH.AH, position)


#diamonds
class D2(Sprite):
    D2 = ImageAsset("2D.png")
    def __init__(self,  position):
        super().__init__(D2.D2, position)
class D3(Sprite):
    D3 = ImageAsset("3D.png")
    def __init__(self,  position):
        super().__init__(D3.D3, position)
class D4(Sprite):
    D4 = ImageAsset("4D.png")
    def __init__(self,  position):
        super().__init__(D4.D4, position)
class D5(Sprite):
    D5 = ImageAsset("5D.png")
    def __init__(self,  position):
        super().__init__(D5.D5, position)
class D6(Sprite):
    D6 = ImageAsset("6D.png")
    def __init__(self,  position):
        super().__init__(D6.D6, position)
class D7(Sprite):
    D7 = ImageAsset("7D.png")
    def __init__(self,  position):
        super().__init__(D7.D7, position)
class D8(Sprite):
    D8 = ImageAsset("8D.png")
    def __init__(self,  position):
        super().__init__(D8.D8, position)
class D9(Sprite):
    D9 = ImageAsset("9D.png")
    def __init__(self,  position):
        super().__init__(D9.D9, position)
class D10(Sprite):
    D10 = ImageAsset("10D.png")
    def __init__(self,  position):
        super().__init__(D10.D10, position)
class JD(Sprite):
    JD = ImageAsset("JD.png")
    def __init__(self,  position):
        super().__init__(JD.JD, position)
class QD(Sprite):
    QD = ImageAsset("QD.png")
    def __init__(self,  position):
        super().__init__(QD.QD, position)
class KD(Sprite):
    KD = ImageAsset("KD.png")
    def __init__(self,  position):
        super().__init__(KD.KD, position)
class AD(Sprite):
    AD = ImageAsset("AD.png")
    def __init__(self,  position):
        super().__init__(AD.AD, position)


#spades
class S2(Sprite):
    S2 = ImageAsset("2S.png")
    def __init__(self,  position):
        super().__init__(S2.S2, position)
class S3(Sprite):
    S3 = ImageAsset("3S.png")
    def __init__(self,  position):
        super().__init__(S3.S3, position)
class S4(Sprite):
    S4 = ImageAsset("4S.png")
    def __init__(self,  position):
        super().__init__(S4.S4, position)
class S5(Sprite):
    S5 = ImageAsset("5S.png")
    def __init__(self,  position):
        super().__init__(S5.S5, position)
class S6(Sprite):
    S6 = ImageAsset("6S.png")
    def __init__(self,  position):
        super().__init__(S6.S6, position)
class S7(Sprite):
    S7 = ImageAsset("7S.png")
    def __init__(self,  position):
        super().__init__(S7.S7, position)
class S8(Sprite):
    S8 = ImageAsset("8S.png")
    def __init__(self,  position):
        super().__init__(S8.S8, position)
class S9(Sprite):
    S9 = ImageAsset("9S.png")
    def __init__(self,  position):
        super().__init__(S9.S9, position)
class S10(Sprite):
    S10 = ImageAsset("10S.png")
    def __init__(self,  position):
        super().__init__(S10.S10, position)
class JS(Sprite):
    JS = ImageAsset("JS.png")
    def __init__(self,  position):
        super().__init__(JS.JS, position)
class QS(Sprite):
    QS = ImageAsset("QS.png")
    def __init__(self,  position):
        super().__init__(QS.QS, position)
class KS(Sprite):
    KS = ImageAsset("KS.png")
    def __init__(self,  position):
        super().__init__(KS.KS, position)
class AS(Sprite):
    AS = ImageAsset("AS.png")
    def __init__(self,  position):
        super().__init__(AS.AS, position)


#clubs
class C2(Sprite):
    C2 = ImageAsset("2C.png")
    def __init__(self,  position):
        super().__init__(C2.C2, position)
class C3(Sprite):
    C3 = ImageAsset("3C.png")
    def __init__(self,  position):
        super().__init__(C3.C3, position)
class C4(Sprite):
    C4 = ImageAsset("4C.png")
    def __init__(self,  position):
        super().__init__(C4.C4, position)
class C5(Sprite):
    C5 = ImageAsset("5C.png")
    def __init__(self,  position):
        super().__init__(C5.C5, position)
class C6(Sprite):
    C6 = ImageAsset("2C.png")
    def __init__(self,  position):
        super().__init__(C6.C6, position)
class C7(Sprite):
    C7 = ImageAsset("7C.png")
    def __init__(self,  position):
        super().__init__(C7.C7, position)
class C8(Sprite):
    C8 = ImageAsset("8C.png")
    def __init__(self,  position):
        super().__init__(C8.C8, position)
class C9(Sprite):
    C9 = ImageAsset("9C.png")
    def __init__(self,  position):
        super().__init__(C9.C9, position)
class C10(Sprite):
    C10 = ImageAsset("10C.png")
    def __init__(self,  position):
        super().__init__(C10.C10, position)
class JC(Sprite):
    JC = ImageAsset("JC.png")
    def __init__(self,  position):
        super().__init__(JC.JC, position)
class QC(Sprite):
    QC = ImageAsset("QC.png")
    def __init__(self,  position):
        super().__init__(QC.QC, position)
class KC(Sprite):
    KC = ImageAsset("KC.png")
    def __init__(self,  position):
        super().__init__(KC.KC, position)
class AC(Sprite):
    AC = ImageAsset("AC.png")
    def __init__(self,  position):
        super().__init__(AC.AC, position)
        

cards = [H2, H3, H4, H5, H6, H7, H8, H9, H10, JH, QH, KH, AH, D2, D3, D4, D5, D6, D7, D8, D9, D10, JD, QD, KD, AD, S2, S3, S4, S5, S6, S7, S8, S9, S10, JS, QS, KS, AS, C2, C3, C4, C5, C6, C7, C8, C9, C10, JC, QC, KC, AC]
random.shuffle(cards)

s = cards[0]
a = s((50,150))
a.scale = 0.1

cards.pop(0)

b = cards[0]
c = b((150,150))
c.scale = 0.1

cards.pop(0)

q = cards[0]
w = q((50,25))
w.scale = .1
cards.pop(0)
if q == H10 or q == JH or q == QH or q == KH or q == AH or q == D10 or q == JD or q == QD or q == KD or q == AD or q == S10 or q == JS or q == QS or q == KS or q == AS or q == C10 or q == JC or q == QC or q == KC or q == AC:
    r = cards[0]
    if r == H10 or r == JH or r == QH or r == KH or r == AH or r == D10 or r == JD or r == QD or r == KD or r == AD or r == S10 or r == JS or r == QS or r == KS or r == AS or r == C10 or r == JC or r == QC or r == KC or r == AC:
        print("Dealer has blackjack")
        j = r((150,25))
        j.scale = .1
    cards.pop(0)
r = cards[0]
cards.pop(0)

e = cardback((150, 25))
e.scale = .1
t = 1

print("press space to being")
def pauseplay(event):
    global t
    t = 1
    print("Press H to hit or S to stay")

def step():
    global t
    while t == 2:
        r((150,25))
        r.scale = .1
        t = 3
    
def stay(event):
    global t, r
    if t == 1:
        print("You stayed")
        t = 2
yourscore = 0
#getting the starting score
if a == H2:
    yourscore += 2
    print(yourscore)
elif a == S2:
    yourscore += 2
    print(yourscore)
elif a == D2:
    yourscore += 2
    print(yourscore)
elif a == C2:
    yourscore += 2
    print(yourscore)
elif a == H3:
    yourscore += 3
    print(yourscore)
elif a == S3:
    yourscore += 3
    print(yourscore)
elif a == D3:
    yourscore += 3
    print(yourscore)
elif a == C3:
    yourscore += 3
    print(yourscore)
elif a == H4:
    yourscore += 4
    print(yourscore)
elif a == S4:
    yourscore += 4
    print(yourscore)
elif a == D4:
    yourscore += 4
    print(yourscore)
elif a == C4:
    yourscore += 4
    print(yourscore)
elif a == H5:
    yourscore += 5
    print(yourscore)
elif a == C5:
    yourscore += 5
    print(yourscore)
elif a == D5:
    yourscore += 5
    print(yourscore)
elif a == S5:
    yourscore += 5
    print(yourscore)
elif a == H6:
    yourscore += 6
    print(yourscore)
elif a == S6:
    yourscore += 6
    print(yourscore)
elif a == D6:
    yourscore += 6
    print(yourscore)
elif a == C6:
    yourscore += 6
    print(yourscore)
elif a == H7:
    yourscore += 7
    print(yourscore)
elif a == C7:
    yourscore += 7
    print(yourscore)
elif a == S7:
    yourscore += 7
    print(yourscore)
elif a == D7:
    yourscore += 7
    print(yourscore)
elif a == D8:
    yourscore += 8
    print(yourscore)
elif a == C8:
    yourscore += 8
    print(yourscore)
elif a == S8:
    yourscore += 8
    print(yourscore)
elif a == H8:
    yourscore += 8
    print(yourscore)
elif a == D9:
    yourscore += 9
    print(yourscore)
elif a == H9:
    yourscore += 9
    print(yourscore)
elif a == S9:
    yourscore += 9
    print(yourscore)
elif a == C9:
    yourscore += 9
    print(yourscore)
elif a == AH:
    yourscore += 1
    print(yourscore)
elif a == AH:
    yourscore += 1
    print(yourscore)
elif a == AC:
    yourscore += 1
    print(yourscore)
elif a == AD:
    yourscore += 1
    print(yourscore)
else:
    yourscore += 1
    print(yourscore)
print("yourscore" + str(yourscore))

m = 2
def hit(event):
    global cards, y, m, yourscore
    y = 150
    o = cards[0]
    p = o((100*m+50,y))
    p.scale = .1
    cards.pop(0)
    m = m + 1
    print(str(o))
    if o == H2:
        yourscore += 2
        print(yourscore)
    elif o == S2:
        yourscore += 2
        print(yourscore)
    elif o == D2:
        yourscore += 2
        print(yourscore)
    elif o == C2:
        yourscore += 2
        print(yourscore)

    elif o == H3:
        yourscore += 3
        print(yourscore)
    elif o == S3:
        yourscore += 3
        print(yourscore)
    elif o == D3:
        yourscore += 3
        print(yourscore)
    elif o == C3:
        yourscore += 3
        print(yourscore)
    elif o == H4:
        yourscore += 4
        print(yourscore)
    elif o == S4:
        yourscore += 4
        print(yourscore)
    elif o == D4:
        yourscore += 4
        print(yourscore)
    elif o == C4:
        yourscore += 4
        print(yourscore)
    elif o == H5:
        yourscore += 5
        print(yourscore)
    elif o == C5:
        yourscore += 5
        print(yourscore)
    elif o == D5:
        yourscore += 5
        print(yourscore)
    elif o == S5:
        yourscore += 5
        print(yourscore)
    elif o == H6:
        yourscore += 6
        print(yourscore)
    elif o == S6:
        yourscore += 6
        print(yourscore)
    elif o == D6:
        yourscore += 6
        print(yourscore)
    elif o == C6:
        yourscore += 6
        print(yourscore)
    elif o == H7:
        yourscore += 7
        print(yourscore)
    elif o == C7:
        yourscore += 7
        print(yourscore)
    elif o == S7:
        yourscore += 7
        print(yourscore)
    elif o == D7:
        yourscore += 7
        print(yourscore)
    elif o == D8:
        yourscore += 8
        print(yourscore)
    elif o == C8:
        yourscore += 8
        print(yourscore)
    elif o == S8:
        yourscore += 8
        print(yourscore)
    elif o == H8:
        yourscore += 8
        print(yourscore)
    elif o == D9:
        yourscore += 9
        print(yourscore)
    elif o == H9:
        yourscore += 9
        print(yourscore)
    elif o == S9:
        yourscore += 9
        print(yourscore)
    elif o == C9:
        yourscore += 9
        print(yourscore)
    elif o == AH:
        yourscore += 1
        print(yourscore)
    elif o == AH:
        yourscore += 1
        print(yourscore)
    elif o == AC:
        yourscore += 1
        print(yourscore)
    elif o == AD:
        yourscore += 1
        print(yourscore)
    else:
        yourscore += 1
        print(yourscore)
    if yourscore > 21:
        print("You busted")










myapp = App()
app = App(500,500)  
app.run(step)
myapp.listenKeyEvent('keydown','space',pauseplay)
myapp.listenKeyEvent('keydown','s',stay)
myapp.listenKeyEvent('keydown','h',hit)

