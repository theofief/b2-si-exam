# MLD (Modèle Logique de Données)

Table `distributeur`:
- id_distributeur : INTEGER PRIMARY KEY
- nombre_balles : INTEGER NOT NULL
- etat_courant : TEXT NOT NULL

Table `historique`:
- id : INTEGER PRIMARY KEY
- id_distributeur : INTEGER REFERENCES distributeur(id_distributeur)
- action : TEXT
- timestamp : DATETIME
- etat_avant : TEXT
- etat_apres : TEXT
