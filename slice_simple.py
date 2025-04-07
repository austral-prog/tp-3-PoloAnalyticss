def slice_simple():
    texto = "Awesome"
    
    letras3 = texto[:3].lower()
    print(letras3)

    otras3 = texto[2:5]
    print(otras3)

    primeraparte = texto[:4]
    segundaparte = texto[-3:]
    print(primeraparte + segundaparte)# Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
slice_simple()    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
