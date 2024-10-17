from collections import Counter

# Frecuencia típica de las letras en español (según la tabla proporcionada)
frecuencia_espanol = [
    'e', 'a', 'r', 'o', 'i', 'n', 'l', 'd', 'c', 'u', 't', 
    's', 'm', 'p', 'b', 'f', 'v', 'q', 'j', 'g', 'h', 'x', 
    'ñ', 'z', 'y', 'k', 'w'
]

# Mensaje cifrado
mensaje_cifrado = """

"""

# 1. Contar las frecuencias de las letras en el mensaje cifrado
def contar_frecuencias(mensaje):
    mensaje = mensaje.upper()
    letras_solo = [c for c in mensaje if c.isalpha()]  # Filtramos solo letras
    contador = Counter(letras_solo)
    total_letras = sum(contador.values())
    return {letra: (frecuencia / total_letras) * 100 for letra, frecuencia in contador.items()}

# 2. Mapeo de frecuencias del mensaje cifrado a las letras comunes en español
def crear_mapeo(frecuencias_cifrado):
    # Ordenar las frecuencias de las letras en el texto cifrado (de mayor a menor)
    letras_ordenadas_cifrado = [item[0] for item in sorted(frecuencias_cifrado.items(), key=lambda x: x[1], reverse=True)]
    
    # Crear el mapeo basado en la comparación con la frecuencia de letras en español
    mapeo = {letra_cifrado: letra_espanol for letra_cifrado, letra_espanol in zip(letras_ordenadas_cifrado, frecuencia_espanol)}
    
    return mapeo

# 3. Función para descifrar el mensaje
def descifrar_mensaje(mensaje, mapeo):
    mensaje_descifrado = ""
    for letra in mensaje.upper():
        if letra in mapeo:
            mensaje_descifrado += mapeo[letra]
        else:
            mensaje_descifrado += letra  # Si no está en el mapeo (por ejemplo, espacios), dejarlo igual
    return mensaje_descifrado

# Calcular frecuencias
frecuencias_cifrado = contar_frecuencias(mensaje_cifrado)

# Crear el mapeo de las letras
mapeo_letras = crear_mapeo(frecuencias_cifrado)

# Descifrar el mensaje
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, mapeo_letras)

# Mostrar resultados
print("Mensaje cifrado original:")
print(mensaje_cifrado)
print("\nMensaje descifrado:")
print(mensaje_descifrado)

