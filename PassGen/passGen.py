## Import ##
import os
import string
import random
import sqlite3


## Variable GLOBALE ##
conn = sqlite3.connect("database.db")
curs = conn.cursor()

## Sqlite3 ##
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "database.db")
def CreateDB():
    global conn
    global curs

    conn = sqlite3.connect(db_path)
    curs = conn.cursor()

    ## Creation DB / table ##
    curs.execute("""
            CREATE TABLE IF NOT EXISTS PassWord (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                MotsDePasse TEXT,
                Site TEXT, 
                Url TEXT,
                Pseudo TEXT,
                Note TEXT
                );
            """)

############################################################################

## Fonction ##


#

def Display():
    os.system("cls")
    print("--------------------------------------------")
    print("1. Générer un nouveau mots de passe ")
    print("--------------------------------------------")
    print("2. Accéder au mots de passe enregistrée ")
    print("--------------------------------------------")
    print("3. Exit ")
    print("--------------------------------------------")
    print("\n")


#

def DispTable():
    os.system("cls")
    print("--------------------------------------------")
    print("              Vos Mots de passe :           ")
    print("--------------------------------------------")
    print("\n")
    result = curs.execute("SELECT MotsDePasse, SIte, Url, Pseudo, Note FROM PassWord")
    data = result.fetchall()
    for row in data:
        print(f"Site : {row[1]}")
        print(f"Mots de passe : {row[0]}")
        print(f"Url : {row[2]}")
        print(f"Pseudo : {row[3]}")
        print(f"Note : {row[4]}")
        print("\n")
        print("--------------------------------------------")
        print("\n")
    print("\n")   


#

def  GenPass(scalePsdw):
    char_Az = string.ascii_letters
    char_specialKey = string.punctuation
    char_Number = string.digits
    all_char = char_Az + char_specialKey + char_Number
    finalPaswd = []

    if scalePsdw == "rdm":
        len_pswd = random.randint(12, 150)

    else:
        len_pswd = int(scalePsdw)
    

    for i in range(len_pswd):
        finalPaswd.append(random.choice(all_char))
    finalPaswd = "".join(finalPaswd)
    
    os.system("cls")
    site = input("Entrée le nom du site -> ")
    url = input("Url -> ")
    pseudo = input("Pseudo -> ")
    note = input("Note particullière -> ")
    print("\n")
    input("Appuyée sur [Entrée] pour continuée")
    allData = (finalPaswd, site, url, pseudo, note)
    curs.execute("""
                 
            INSERT INTO PassWord (MotsDePasse, Site, Url, Pseudo, Note)
                 VALUES (?, ?, ?, ?, ?)""", allData
                )
    conn.commit()

    os.system("cls")
    print("--------------------------------------------")
    print("              RECAPITULATIF :               ")
    print("--------------------------------------------")
    print("\n \n")
    print("Site : ", site)
    print("mots de passe (taille[",len_pswd,"]) : ",finalPaswd)
    print("Url : ",url)
    print("Pseudo : ", pseudo)
    print("Note : ",note)
    print("\n")




    


## Début script ##
choice = None
while choice != 3:
    CreateDB()
    Display()
    while True:
        try:
            choice = int(input("Choisir une action : "))
            if choice in [1, 2 ,3]:
                break
            else:
                Display()
                print("Entrée une valeur correcte ! ")
        except ValueError:
            Display()
            print("Cette action n'est pas possible ! ")

    if choice == 1:
        scalePswd = input("Entrée une taille de mots de passe (recommander min 12 ! / alléatoire entrée 'rdm') -> ")
        GenPass(scalePswd)
        input("Appuyée sur [Entrée] pour fermée ... ")
        print("\n \n")
        conn.close()
        
    if choice == 2:
        DispTable()
        input("Appuyée sur [Entrée] pour fermée ... ")
        print("\n \n")
        conn.close()
    
    if choice == 3:
        input("Appuyée sur [Entrée] pour quittée ... ")
        conn.close()
        exit()
    
