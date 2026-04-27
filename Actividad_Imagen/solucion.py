import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# PUNTO 1: Diseñar un método que reciba la ubicación de un archivo JPG
def procesar_mi_imagen(ruta_del_archivo):
    try:
        # Cargamos la imagen
        img = Image.open(ruta_del_archivo)
        
        # PUNTO 2: Convertir la imagen en un array
        array_imagen = np.array(img)
        
        # Imprimir el array en la consola para ver los números
        print("El array de la imagen es:")
        print(array_imagen)
        
        # Renderizar (mostrar) el array obtenido
        plt.imshow(array_imagen)
        plt.title("Imagen Renderizada desde Array")
        plt.axis('off') # Esto quita los números de los ejes
        plt.show()
        
    except Exception as e:
        print(f"Error: No se pudo encontrar la imagen. Revisa la ruta. {e}")

# --- AQUÍ EJECUTAMOS EL MÉTODO ---
# Reemplaza 'tu_imagen.jpg' por el nombre real de tu foto
# Asegúrate de que la foto esté en la misma carpeta que este archivo .py
procesar_mi_imagen(r"C:\Users\MARCOGALU\OneDrive\Desktop\Ciencia Datos 2026\Reconocimiento Visual\arreglo_RV.png")

def separar_canales_rgb(ruta_del_archivo):
    # Volvemos a cargar la imagen y convertirla en array
    img = Image.open(ruta_del_archivo)
    array_imagen = np.array(img)
    
    # Separamos las capas (R=0, G=1, B=2)
    # El cuarto valor (255) que ves en tu terminal es el canal 'Alpha' (transparencia), 
    # pero para RGB solo necesitamos los 3 primeros.
    canal_rojo = array_imagen[:, :, 0]
    canal_verde = array_imagen[:, :, 1]
    canal_azul = array_imagen[:, :, 2]
    
    # Creamos una ventana con 3 espacios (1 fila, 3 columnas)
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    # Renderizamos cada matriz con su respectivo mapa de color
    axs[0].imshow(canal_rojo, cmap='Reds')
    axs[0].set_title("Canal Rojo")
    axs[0].axis('off')
    
    axs[1].imshow(canal_verde, cmap='Greens')
    axs[1].set_title("Canal Verde")
    axs[1].axis('off')
    
    axs[2].imshow(canal_azul, cmap='Blues')
    axs[2].set_title("Canal Azul")
    axs[2].axis('off')
    
    plt.tight_layout()
    plt.show()
# 1. Definimos la ruta una sola vez usando la 'r' al principio
ruta = r"C:\Users\MARCOGALU\OneDrive\Desktop\Ciencia Datos 2026\Reconocimiento Visual\arreglo_RV.png"

# 2. Ejecuta el punto 1 y 2 (Pasamos la variable 'ruta')
procesar_mi_imagen(ruta)

# 3. Ejecuta el punto 3 (Pasamos la misma variable)
separar_canales_rgb(ruta)   