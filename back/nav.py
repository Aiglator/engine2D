import tkinter as tk

def navbar(root):
    menubar = tk.Menu(root)
    
    # Créer le menu Fichier
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New", command=lambda: print("New"))
    file_menu.add_command(label="Open", command=lambda: print("Open"))
    file_menu.add_command(label="Save", command=lambda: print("Save"))
    file_menu.add_command(label="Exit",command=root.quit)    
    # Ajouter le menu Fichier à la barre de menu
    menubar.add_cascade(label="File", menu=file_menu)
    
    edit_menu = tk.Menu(menubar, tearoff=0)
    edit_menu.add_command(label="Annuler", command=lambda: print("Annuler action"))
    edit_menu.add_command(label="Refaire", command=lambda: print("Refaire action"))
    edit_menu.add_separator()
    edit_menu.add_command(label="Couper", command=lambda: print("Couper"))
    edit_menu.add_command(label="Copier", command=lambda: print("Copier"))
    edit_menu.add_command(label="Coller", command=lambda: print("Coller"))
    menubar.add_cascade(label="Édition", menu=edit_menu)

    # Menu Exécution
    run_menu = tk.Menu(menubar, tearoff=0)
    run_menu.add_command(label="Exécuter", command=lambda: print("Exécuter le jeu"))
    run_menu.add_command(label="Déboguer", command=lambda: print("Déboguer le jeu"))
    menubar.add_cascade(label="Exécution", menu=run_menu)

    # Menu Outils
    tools_menu = tk.Menu(menubar, tearoff=0)
    tools_menu.add_command(label="Options", command=lambda: print("Options de configuration"))
    tools_menu.add_command(label="Outils de développement", command=lambda: print("Outils de développement"))
    menubar.add_cascade(label="Outils", menu=tools_menu)
    
    # Configurer la fenêtre principale pour utiliser cette barre de menu
    root.config(menu=menubar)
