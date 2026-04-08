def inp_int(msg: str = "ESCRIBE UN ENTERO: ", errmsg: str = "Valor incorrecto o desbordado") -> int:
    val: int = 0;
    while True:
        try:
            val = int(input(msg));
            break
        except Exception:
            print(errmsg)
    return val;

