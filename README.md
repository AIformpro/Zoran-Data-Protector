# Zoran-Data-Protector

**Data Protector** est la brique de Zoran aSiM dédiée à la protection native des données personnelles.  
Elle assure :  
- le **masquage** automatique des données sensibles (emails, téléphones, identifiants, cartes),  
- la gestion du **TTL adaptatif** (durée de vie limitée des données),  
- l’activation de **rollback ΔM11.3** en cas de violation,  
- la traçabilité via `logs/data_log.json`.  

## 🚀 Fonctionnalités
- Masquage par regex (emails, téléphones, cartes bancaires).  
- TTL configurable pour chaque donnée.  
- Audit log horodaté des traitements.  
- Démonstration reproductible (`demo.py`).  
- Tests unitaires (`tests/test_data_protector.py`).  

## 📖 Démonstration
```bash
python demo.py
```

## 📜 Exemple
```json
{
  "input": {"email": "john.doe@example.com"},
  "output": {"email": "j***@example.com"},
  "ttl": 3600,
  "timestamp": 1693064444.789
}
```

## 🔗 Liens associés
- White Paper : *“Privacy by Design in Mimetic AI”* (à paraître).  
- Contact : tabary01@gmail.com  

## 📄 Licence
MIT — usage libre.  
© 2025, Frédéric Tabary — Projet Zoran aSiM
