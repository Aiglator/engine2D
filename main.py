import tkinter as tk
from back.background import Background
import back.nav as nav
import back.save as save

root = tk.Tk()

# Charger l'image du logo
logo_image = tk.PhotoImage(file="./asset/assetapps/logo.png")
root.iconphoto(False, logo_image)

# Définir les dimensions de la fenêtre pour qu'elle corresponde à la taille de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

root.title("Engine2d")

# Créer le menu
nav.navbar(root)

# Créer le canvas et la fenêtre de jeu
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Créer et afficher le fond avec grille
background = Background(canvas, screen_width, screen_height)
background.draw_background()

root.mainloop()