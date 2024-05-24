def palabra_a_bits(palabra):
    # Verificar que el argumento es una cadena no vacía
    if not palabra:
        raise ValueError("El argumento debe ser una cadena no vacía")

    # Convertir cada carácter en su representación en bits de 8 bits
    bits_list = [format(ord(caracter), '08b') for caracter in palabra]

    # Unir los bits en una sola cadena con espacios
    bits_resultado = ' '.join(bits_list)

    return bits_resultado