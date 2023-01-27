def greeting():
    dato = input("Bienvenido, para crear tu contraseña aleatoria presiona 1. \n")
    if dato != "1":
        print("la opcion digitada no es correcta")
    else:
        return True

def def_chars(chars, num):
        import string
        chars = list(string.ascii_lowercase)
        num = "0123456789"
        return (chars, num)

if greeting() == True:
    def_chars()

    print (f"1-{chars}, 2-{num}")
    

