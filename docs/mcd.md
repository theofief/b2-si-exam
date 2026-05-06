# MCD (Modèle Conceptuel de Données)

Entités:
- Distributeur (id_distributeur, nombre_balles, etat_courant)
- Historique (id, id_distributeur, action, timestamp, etat_avant, etat_apres)

Associations:
- Un `Distributeur` possède zéro ou plusieurs `Historique`.
