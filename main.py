def inp_int(msg: str = "ESCRIBE UN ENTERO: ", errmsg: str = "Valor incorrecto o desbordado") -> int:
    val: int = 0;
    while True:
        try:
            val = int(input(msg));
            break
        except Exception:
            print(errmsg)
    return val;

def inp_str(msg: str = "ESCRIBE UNA CADENA: ", errmsg: str = "Valor incorrecto o desbordado") -> str:
    val: str = "";
    while True:
        try:
            val = input(msg);
            if (val.strip().count == 0):
                print(errmsg)
            else:
                break
        except Exception:
            print(errmsg)
    return val;

nombre: str = inp_str("Escribe tu nombre: ")
edad: int = inp_int("Escribe tu edad: ")

print(f"Te llamas {nombre}")
print(f"Tu edad es: {edad}")
print("Un placer conocerte! :)")