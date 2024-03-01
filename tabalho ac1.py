def media():
    ap1 = float(input("infomorme a nota da ap1:"))
    ap2 = float(input("informe a nota da ap2:"))
    ac = float(input("informe a nota da ac:"))

    media = (ap1 + ap2) * 0.4 + ac * 0.2

    print(" A média é", round(media, 2))

def outra_media():

    return (ap1 + ap2) * 0.4 + ac * 0.2

def main ():
    media()

    ap1, ap2, ac = le_notas()
    print(outra_media(7,8,9.2))
    print(outra_media(7.7, 6.5,7.3))
