
# ÍNDICE
1. [Título](#peticion-de-entradas-al-usuario)
2. [Funcionalidad preventiva](#creación-de-funcionalidad-para-evitar-fallos-por-parte-del-usuario)
3. [Resumen de cambios](#resumen-de-ramas-y-comentarios)

# Petición de entradas al usuario

## Creación de funcionalidad para evitar fallos por parte del usuario

- [x] Definición de función para pedir inputs numéricos
    - Función `inp_int` que **devuelve** un tipo *int*.
    - Prevención de **errores** con `try-except`.

- [x] Definición de función para pedir inputs de cadenas válidas (que contengan algún caracter)
    - Función `inp_str` que **devuelve** un tipo *str*.
    - Prevención de **errores** con `try-except` y condicionales que:
        1. **Eliminan** todos los carácteres de espacio *\s* -> método `.strip`.
        2. **Miden** la longitud de la cadena final para ver si cumple la condición -> método `.count`.

- [ ] **Pruebas finales** con `print` de los resultados.

:sunglasses:

## Resumen de ramas y comentarios

|rama|comentario|
|:---|:---:|
|master|"initial commit"|
|develop|"add: basic input integer functionality"|


:fire: