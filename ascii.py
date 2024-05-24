def byte_a_ascii(byte_binario):
    # Verificar que el argumento es una cadena de 8 bits
    if len(byte_binario) != 8 or not all(bit in '01' for bit in byte_binario):
        raise ValueError("El argumento debe ser una cadena de 8 bits (solo 0 y 1)")

    # Convertir la cadena de bits en un valor entero
    valor_entero = int(byte_binario, 2)

    # Obtener el carácter ASCII correspondiente
    caracter = chr(valor_entero)

    # Convertir el valor entero a su representación hexadecimal
    valor_hexadecimal = format(valor_entero, 'x')

    # Formatear el resultado
    resultado = f"{caracter}-{valor_hexadecimal}"

    return resultado
