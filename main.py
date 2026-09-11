import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("Projet_2")
root.geometry("600x480")
root.resizable(False, False)
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "dark")
# Création du notebook pour les différentes sections de l'application
main_notebook = ttk.Notebook()
main_notebook.pack(expand=True, fill = tk.BOTH)
# Création des frames pour les différentes sections
frame_repas = tk.Frame(main_notebook)
frame_info = tk.Frame(main_notebook)
# Placement des frames dans le notebook
frame_repas.pack(expand=True, fill=tk.BOTH)
frame_info.pack(expand=True, fill=tk.BOTH)
# Ajout des frames au notebook avec les titres correspondants
main_notebook.add(frame_repas, text="Repas", compound=tk.LEFT)
main_notebook.add(frame_info, text="Information", compound=tk.LEFT)
# Initialisation des listes pour les différentes catégories de plats
entrees = []
plats = []
dessers = []
boissons = []
cnt_entrees = 0
cnt_plats = 0
cnt_dessers = 0
cnt_boissons = 0
# Calcul des parts de chaque catégorie de plats
total = 0
part_entrees = 0
part_plats = 0
part_dessers = 0
part_boissons = 0
partie_plats_ideale = 50
partie_entrees_ideale = 25
partie_desserts_ideale = 10
partie_boissons_ideale = 15

def tot():
    global total, part_entrees, part_plats, part_dessers, part_boissons
    total = cnt_entrees + cnt_plats + cnt_dessers + cnt_boissons
    part_entrees = (cnt_entrees / total * 100) if total > 0 else 0
    part_plats = (cnt_plats / total * 100) if total > 0 else 0
    part_dessers = (cnt_dessers / total * 100) if total > 0 else 0
    part_boissons = (cnt_boissons / total * 100) if total > 0 else 0

def changement_tab():
    tot()
    for widget in frame_repas.winfo_children():
        widget.destroy()
    for widget in frame_info.winfo_children():
        widget.destroy()
    if main_notebook.index("current") == 0:
        place_frame_repas()
    else:
        place_frame_info()

def addition_window():
    # Fonction pour ajouter un repas à la liste des repas
    def ajouter_repas():
        # Récupération des informations du repas à ajouter et ajout du repas à la liste des repas en fonction du type de repas
        global cnt_entrees, cnt_plats, cnt_dessers, cnt_boissons
        global tot, changement_tab
        # Récupération des informations du repas à ajouter et validation des données
        n = entry_nom.get() if entry_nom.get() != "" else "NoNom"
        p = entry_prenom.get() if entry_prenom.get() != "" else "NoPrenom"
        c = int(entry_cnt.get()) if entry_cnt.get() and entry_cnt.get().isdigit() else 0
        t = entry_type.get()
        # Ajout du repas à la liste des repas en fonction du type de repas
        if t == "Entree":
            entrees.append((n, p, c))
            cnt_entrees += c
        elif t == "Plat":
            plats.append((n, p, c))
            cnt_plats += c
        elif t == "Dessert":
            dessers.append((n, p, c))
            cnt_dessers += c
        elif t == "Boisson":
            boissons.append((n, p, c))
            cnt_boissons += c
        # Recalcul des parts de chaque catégorie de plats et mise à jour de l'affichage
        tot()
        root_aj.destroy()
        changement_tab()

    # Creation de la fenetre pour ajouter un repas
    root_aj = tk.Tk()
    root_aj.title("Ajouter un repas")
    root_aj.geometry("600x480")
    root_aj.resizable(False, False)
    root_aj.tk.call("source", "azure.tcl")
    root_aj.tk.call("set_theme", "dark")
    # Creation du frame pour les informations du repas
    frame = tk.Frame(root_aj, relief=tk.SOLID, borderwidth=1, width=400, height=400)
    frame.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
    # Placement des labels et des champs de saisie pour les informations du repas
    nom = tk.StringVar()
    prenom = tk.StringVar()
    cnt = tk.IntVar()
    types = ["Entree", "Plat", "Dessert", "Boisson"]
    type = tk.StringVar(value=types[0])
    label_nom = ttk.Label(frame, text="Entrez le nom: ")
    label_prenom = ttk.Label(frame, text="Entrez le prenom: ")
    label_cnt = ttk.Label(frame, text="Entrez le quantite: ")
    label_type = ttk.Label(frame, text="Entrez le type: ")
    entry_nom = ttk.Entry(frame, textvariable=nom)
    entry_prenom = ttk.Entry(frame, textvariable=prenom)
    entry_cnt = ttk.Entry(frame, textvariable=cnt)
    entry_type = ttk.Combobox(frame, textvariable=type, values=types)
    label_nom.place(anchor=tk.CENTER, relx=0.2, rely=0.2)
    entry_nom.place(anchor=tk.CENTER, relx=0.6, rely=0.2)
    label_prenom.place(anchor=tk.CENTER, relx=0.2, rely=0.4)
    entry_prenom.place(anchor=tk.CENTER, relx=0.6, rely=0.4)
    label_cnt.place(anchor=tk.CENTER, relx=0.2, rely=0.6)
    entry_cnt.place(anchor=tk.CENTER, relx=0.6, rely=0.6)
    label_type.place(anchor=tk.CENTER, relx=0.2, rely=0.8)
    entry_type.place(anchor=tk.CENTER, relx=0.6, rely=0.8)
    button_ajouter = ttk.Button(frame, text="Ajouter", command=ajouter_repas, width=30)
    button_ajouter.place(anchor=tk.CENTER, relx=0.5, rely=0.9)

def l_nom(type):
    # Fonction pour afficher la liste des repas en fonction du type
    # Creation de la fenetre pour afficher la liste des repas
    root_list = tk.Tk()
    root_list.title(f"Liste des {type}")
    root_list.geometry("600x480")
    root_list.resizable(False, False)
    root_list.tk.call("source", "azure.tcl")
    root_list.tk.call("set_theme", "dark")
    cols = ("Nom", "Prenom", "Quantite")
    # Selection de la liste des repas en fonction du type
    if type == "Entree":
        food = entrees
    elif type == "Plat":
        food = plats
    elif type == "Dessert":
        food = dessers
    else:
        food = boissons
    # Creation du treeview pour afficher la liste des repas
    tree = ttk.Treeview(root_list, columns=cols, show="headings")
    tree.grid(row=0, column=0, sticky="nsew")
    # Placement des titres des colonnes et de la largeur des colonnes
    tree.heading("Nom", text="Nom")
    tree.heading("Prenom", text="Prenom")
    tree.heading("Quantite", text="Quantite")
    tree.column("#1", width=190)
    tree.column("#2", width=190)
    tree.column("#3", width=190)
    # Insertion des repas dans le treeview
    for elem in food:
        tree.insert("", tk.END, values=elem)
    # Placement du scrollbar pour le treeview
    scroll = ttk.Scrollbar(root_list, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)
    scroll.grid(row=0, column=1, sticky="ns")
    # Placement du bouton pour fermer la fenetre
    button_sortie = ttk.Button(root_list, text="Sortie", command=root_list.destroy, width=30)
    button_sortie.grid(row=1, column=0, pady=10)

def annuler():
    # Fonction pour annuler le repas et réinitialiser les données
    global entrees, plats, dessers, boissons
    entrees = []
    plats = []
    dessers = []
    boissons = []
    tot()

def place_frame_repas():
    
    def valider_repas(flag):
        global annuler
        global partie_boissons_ideale, partie_desserts_ideale, partie_entrees_ideale, partie_plats_ideale
        global part_boissons, part_dessers, part_entrees, part_plats
        
        if flag:
            showinfo(title="Repas équilibré", message="Le repas est bien équilibré!")
            annuler()
            changement_tab()
        else:
            info = []
            if part_plats < partie_plats_ideale:
                info.append("Plats")
            if part_entrees < partie_entrees_ideale:
                info.append("Entrées")
            if part_dessers < partie_desserts_ideale:
                info.append("Desserts")
            if part_boissons < partie_boissons_ideale:
                info.append("Boissons")
            message = "Le repas n'est pas équilibré!\n"
            for element in info:
                message += f"Il manque des {element}.\n"
            showerror(title="Repas non équilibré", message=message)

    # Initialisation de bool pour la logique pour le repas
    flag_equilibre = True
    if total == 0:
        button_ajouter = ttk.Button(frame_repas, text="Ajouter un repas", command=addition_window, width=30)
        button_ajouter.pack(anchor=tk.CENTER, padx= 200, pady=180)
    else:
        button_ajouter = ttk.Button(frame_repas, text="+", command=addition_window, width=5)
        button_ajouter.place(anchor=tk.CENTER, relx= 0.9, rely=0.9)
        # Logique pour voir si le repas est equilibre
        message = ""
        if part_plats < partie_plats_ideale:
            flag_equilibre=False
            message += "Il manque des plats.\n"
        if part_entrees < partie_entrees_ideale:
            flag_equilibre=False
            message += "Il manque des entrées.\n"
        if part_dessers < partie_desserts_ideale:
            flag_equilibre=False
            message += "Il manque des desserts.\n"
        if part_boissons < partie_boissons_ideale:
            flag_equilibre=False
            message += "Il manque des boissons.\n"
        # Initiation du frame pour la decision
        frame_decision = tk.Frame(frame_repas, relief=tk.SOLID, borderwidth=1, width=350, height=100)
        frame_decision.place(anchor=tk.CENTER, relx=0.5, rely=0.15)
        
        if flag_equilibre == False:
            # Affichage du message "Repas est équilibré!"
            label_decision = ttk.Label(frame_decision,
                                    text="Repas n'est pas equilibre!\n" + message[0:-1])
            label_decision.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        else:
            # Affichage du message "Repas est équilibré!"
            label_decision = ttk.Label(frame_decision,
                                    text="Repas est équilibré!")
            label_decision.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        # Création des frames pour les différentes catégories de plats
        frame_entrees = tk.Frame(frame_repas, relief=tk.SOLID, borderwidth=1, width=300, height=50)
        frame_entrees.place(anchor=tk.CENTER, relx=0.5, rely=0.35)
        frame_plats = tk.Frame(frame_repas, relief=tk.SOLID, borderwidth=1, width=300, height=50)
        frame_plats.place(anchor=tk.CENTER, relx=0.5, rely=0.5)
        frame_desserts = tk.Frame(frame_repas, relief=tk.SOLID, borderwidth=1, width=300, height=50)
        frame_desserts.place(anchor=tk.CENTER, relx=0.5, rely=0.65)
        frame_boissons = tk.Frame(frame_repas, relief=tk.SOLID, borderwidth=1, width=300, height=50)
        frame_boissons.place(anchor=tk.CENTER, relx=0.5, rely=0.8)
        # Placement des labels pour les différentes catégories de plats
        # Placement des entrees
        label_entrees = ttk.Label(frame_entrees, text=f"Entrées : {len(entrees)} - {part_entrees:.2f}%")
        label_entrees.place(anchor=tk.CENTER,relx=0.25, rely=0.5)
        butt_entrees = ttk.Button(frame_entrees, text="Voir plus...",  padding=[10, 5], command=lambda: l_nom("Entree"))
        butt_entrees.place(anchor=tk.CENTER, relx=0.75, rely=0.5)
        # Placement des plats
        label_plats = ttk.Label(frame_plats, text=f"Plats : {len(plats)} - {part_plats:.2f}%")
        label_plats.place(anchor=tk.CENTER,relx=0.25, rely=0.5)
        butt_plats = ttk.Button(frame_plats, text="Voir plus...", padding=[10, 5], command=lambda: l_nom("Plat"))
        butt_plats.place(anchor=tk.CENTER, relx=0.75, rely=0.5)
        # Placement des desserts
        label_desserts = ttk.Label(frame_desserts, text=f"Desserts : {len(dessers)} - {part_dessers:.2f}%")
        label_desserts.place(anchor=tk.CENTER,relx=0.25, rely=0.5)
        butt_desserts = ttk.Button(frame_desserts, text="Voir plus...",  padding=[10, 5], command=lambda: l_nom("Dessert"))
        butt_desserts.place(anchor=tk.CENTER, relx=0.75, rely=0.5)
        # Placement des boissons
        label_boissons = ttk.Label(frame_boissons, text=f"Boissons : {len(boissons)} - {part_boissons:.2f}%")
        label_boissons.place(anchor=tk.CENTER,relx=0.25, rely=0.5)
        butt_boissons = ttk.Button(frame_boissons, text="Voir plus...",  padding=[10, 5], command=lambda: l_nom("Boisson"))
        butt_boissons.place(anchor=tk.CENTER, relx=0.75, rely=0.5)
        butt_valider = ttk.Button(frame_repas, text="Valider le repas", width=30, command=lambda: valider_repas(flag_equilibre))
        butt_valider.place(anchor=tk.CENTER, relx=0.5, rely=0.95)
    
def creator():
    showinfo(title="Creator_information", message="L'application a ete cree par Anton KUZMENKO - l'etudiant de L2 MIASHS Jean Jaures.")
    
def place_frame_info():
    button_creator = ttk.Button(frame_info, text="Creator", command=creator, width=30, padding=[6,10])
    button_sortie = ttk.Button(frame_info, text="Sortie", command=root.destroy, width=30, padding=[6,10])
    #
    button_creator.place(anchor=tk.CENTER, relx=0.5, rely=0.3)
    button_sortie.place(anchor=tk.CENTER, relx=0.5, rely=0.6)

tot()
main_notebook.bind("<<NotebookTabChanged>>", lambda x: changement_tab())
changement_tab()
root.mainloop()