import vectorFunc as vF
defVector = '''
Vektoren sind eindeutig durch die Angabe einer Masszahl und einer Richtung definiert.
'''  

veclistA, veclistB = vF.vecInput()

vecResult = vF.vecAdd2D(veclistA,veclistB)
vF.vec2D(vecResult)

vecResult = vF.vecSub2D(veclistA,veclistB)
vF.vec2D(vecResult)


