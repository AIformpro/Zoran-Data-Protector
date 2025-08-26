# Zoran-Data-Protector — Privacy by Design pour Zoran aSiM

## 🌍 Contexte
Le RGPD et l’AI Act exigent des garanties explicites pour la protection des données personnelles : minimisation, masquage, limitation temporelle (TTL), transparence et auditabilité. **Zoran aSiM** intègre ces mécanismes dans un module dédié : **Data Protector**.

## ⚙️ Fonctionnement
- Chaque donnée est passée par un **filtre regex** (email, tel, CB).  
- Les données sensibles sont automatiquement masquées (ex : `j***@mail.com`).  
- Chaque entrée est associée à un **TTL** (ex. 1h). Après expiration, rollback ΔM11.3 ou purge.  
- Les traitements sont consignés dans `logs/data_log.json`.  

## 📜 Exemple concret
```json
{
  "input": {"phone": "+33612345678"},
  "output": {"phone": "+33******678"},
  "ttl": 600,
  "timestamp": 1693064888.123
}
```

## 🧪 Démonstration
`demo.py` simule : la protection d’un email, d’un téléphone, d’une carte, et l’application d’un TTL court.  

## 📊 Objectifs
- Offrir une **preuve technique RGPD/AI Act** intégrée.  
- Minimiser l’exposition des données sensibles.  
- Donner aux régulateurs une **preuve reproductible**.  

## 🔗 Suites
- White Paper : *“Privacy by Design in Mimetic AI”*.  
- Intégration future avec **Zoran-Eco-Metrics**.
