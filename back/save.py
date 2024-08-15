# save file  in e2dn for game 2D for the moment
import tkinter
import tkinter.filedialog
def save_file():
    file_path=tkinter.filedialog.asksaveasfilename (defaultextension=".txt",filetypes=[("txt files",".txt"),("all files","*.*")])
    if file_path:
        with open(file_path,"w") as f:
            f.write("le fichier de sauvegarde,est prêt!")
        print("le fichier de sauvegarde est enregistrer !")
        