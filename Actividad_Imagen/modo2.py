import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def abrir_imagen_con_tk(ruta: str = None, max_size=(1200, 800)):
    """
    Abre una ventana Tkinter mostrando la imagen.
    Si ruta es None, abre un FileDialog para seleccionar.
    Ajusta la imagen manteniendo la relación de aspecto si es muy grande.
    """
    if ruta is None:
        ruta = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[("Imagen", "*.png *.jpg *.jpeg *.bmp *.gif")]
        )
        if not ruta:
            return

    if not os.path.exists(ruta):
        messagebox.showerror("Error", f"No existe la ruta: {ruta}")
        return

    try:
        img = Image.open(ruta).convert("RGBA")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir la imagen: {e}")
        return

    w, h = img.size
    mw, mh = max_size
    scale = min(1.0, mw / w, mh / h)
    if scale < 1.0:
        new_size = (int(w * scale), int(h * scale))
        img = img.resize(new_size, Image.LANCZOS)

    root = tk.Tk()
    root.title(os.path.basename(ruta))

    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack(expand=True, fill="both")

    btn = tk.Button(root, text="Cerrar", command=root.destroy)
    btn.pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    ruta_local = os.path.join(os.path.dirname(__file__), "arreglo_RV.png")
    if os.path.exists(ruta_local):
        abrir_imagen_con_tk(ruta_local)
    else:
        abrir_imagen_con_tk(None)











































