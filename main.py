import tkinter as tk
import back.nav as nav


root = tk.Tk()
logo_image=tk.PhotoImage(file="./asset/assetapps/logo.png")
root.iconphoto(False,logo_image)
root.geometry("800x800")
root.title("Engine2d")
create_menu = nav.navbar(root)
root.mainloop()