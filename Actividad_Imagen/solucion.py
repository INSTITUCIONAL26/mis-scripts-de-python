import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def procesar_mi_imagen(ruta_del_archivo):
    try:
        img = Image.open(ruta_del_archivo)
        
        array_imagen = np.array(img)
        
        print("El array de la imagen es:")
        print(array_imagen)
        
        plt.imshow(array_imagen)
        plt.title("Imagen Renderizada desde Array")
        plt.axis('off')
        plt.show()
        
    except Exception as e:
        print(f"Error: No se pudo encontrar la imagen. Revisa la ruta. {e}")

procesar_mi_imagen(r"C:\Users\MARCOGALU\OneDrive\Desktop\Ciencia Datos 2026\Reconocimiento Visual\arreglo_RV.png")

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def separar_canales_rgb(ruta_del_archivo):
    img = Image.open(ruta_del_archivo).convert("RGB")
    mi_imagen_como_array = np.array(img)
    
    array_imagen_rojo = mi_imagen_como_array[:, :, 0]
    array_imagen_verde = mi_imagen_como_array[:, :, 1]
    array_imagen_azul = mi_imagen_como_array[:, :, 2]
    
    print("Shapes canales (R, G, B):")
    print(array_imagen_rojo.shape)
    print(array_imagen_verde.shape)
    print(array_imagen_azul.shape)
    print()
    print("Resumen valores por canal (min, max):")
    print("R:", array_imagen_rojo.min(), array_imagen_rojo.max())
    print("G:", array_imagen_verde.min(), array_imagen_verde.max())
    print("B:", array_imagen_azul.min(), array_imagen_azul.max())
    
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    axs[0].imshow(array_imagen_rojo, cmap='gray')
    axs[0].set_title("Canal Rojo (grayscale)")
    axs[0].axis('off')
    
    axs[1].imshow(array_imagen_verde, cmap='gray')
    axs[1].set_title("Canal Verde (grayscale)")
    axs[1].axis('off')
    
    axs[2].imshow(array_imagen_azul, cmap='gray')
    axs[2].set_title("Canal Azul (grayscale)")
    axs[2].axis('off')
    
    plt.tight_layout()
    plt.show()

ruta = r"C:\Users\MARCOGALU\OneDrive\Desktop\Ciencia Datos 2026\Reconocimiento Visual\arreglo_RV.png"
if os.path.exists(ruta):
    procesar_mi_imagen(ruta)
    separar_canales_rgb(ruta)
else:
    print("ERROR: no se encontró la imagen en:", ruta)

