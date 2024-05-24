def caracter_a_bits(caracter):
    # Verificar que el argumento es un carácter único
    if len(caracter) != 1:
        raise ValueError("El argumento debe ser una cadena de un solo carácter")

    # Obtener el valor Unicode del carácter
    valor_unicode = ord(caracter)

    # Convertir el valor Unicode a una cadena de bits de 8 bits
    bits_resultado = format(valor_unicode, '08b')

    return bits_resultado
