# MPD (Modèle Physique de Données)

Exemple SQL (SQLite) pour créer les tables :

```sql
CREATE TABLE distributeur (
  id_distributeur INTEGER PRIMARY KEY,
  nombre_balles INTEGER NOT NULL,
  etat_courant TEXT NOT NULL
);

CREATE TABLE historique (
  id INTEGER PRIMARY KEY,
  id_distributeur INTEGER,
  action TEXT,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  etat_avant TEXT,
  etat_apres TEXT,
  FOREIGN KEY(id_distributeur) REFERENCES distributeur(id_distributeur)
);
```
