# Rapport de projet

## 1. Introduction

L'objectif de ce projet est de construire une strategie d'investissement simple avec Python, de la tester sur des donnees reelles et d'analyser les resultats obtenus.

Le projet a ete realise avec des donnees boursieres provenant de Yahoo Finance. Le travail porte sur 30 entreprises americaines importantes, avec des donnees journalieres entre le 1er janvier 2020 et le 1er mars 2026.

## 2. Constitution de la base de donnees financieres

### 2.1 Entreprises selectionnees

Les 30 entreprises etudiees sont :

AAPL, MSFT, AMZN, GOOGL, META, NVDA, TSLA, JPM, V, MA, JNJ, PG, HD, KO, PEP, PFE, ABBV, MRK, BAC, WMT, DIS, NFLX, ADBE, CRM, NKE, MCD, XOM, CVX, INTC, AMD.

Ce choix permet d'avoir plusieurs secteurs :

- technologie ;
- sante ;
- consommation ;
- energie ;
- finance ;
- divertissement.

### 2.2 Historique des donnees

L'historique choisi couvre plus de 5 ans :

- date de debut : 1 janvier 2020 ;
- date de fin : 1 mars 2026.

### 2.3 Frequence des donnees

La frequence retenue est journaliere.

Ce choix est simple a manipuler et suffisant pour un premier projet d'analyse financiere.

### 2.4 Source des donnees

La source retenue est Yahoo Finance via la bibliotheque Python `yfinance`.

Les prix de cloture ajustes sont utilises pour tenir compte des splits et des dividendes.

## 3. Strategie d'investissement

### 3.1 Idee de la strategie

La strategie choisie est une strategie de suivi de tendance.

Le principe est le suivant :

- on calcule une moyenne mobile courte sur 20 jours ;
- on calcule une moyenne mobile longue sur 50 jours ;
- si la moyenne mobile courte est au-dessus de la moyenne mobile longue, on considere que la tendance est haussiere ;
- dans ce cas, l'action peut entrer dans le portefeuille.

Cette strategie est simple, facile a expliquer et classique dans l'analyse technique.

### 3.2 Regle de decision

Pour chaque action :

- signal d'achat = 1 si moyenne mobile 20 jours > moyenne mobile 50 jours ;
- sinon signal = 0.

## 4. Allocation et optimisation du portefeuille

### 4.1 Construction du portefeuille

Le portefeuille suit les regles suivantes :

- reequilibrage au debut de chaque mois ;
- maximum 10 actions dans le portefeuille ;
- repartition egale entre les actions selectionnees.

Par exemple, si 5 actions sont selectionnees, chaque action recoit 20 % du portefeuille.

### 4.2 Contraintes du portefeuille

Les contraintes choisies sont simples :

- pas plus de 10 actions ;
- uniquement les actions ayant un signal positif ;
- poids egaux pour eviter une allocation trop compliquee.

### 4.3 Gestion du risque

Pour rester dans une logique simple de debutant, il n'y a pas de mecanisme complexe de gestion du risque.

La protection principale vient de deux elements :

- diversification sur plusieurs entreprises ;
- sortie automatique d'une action quand le signal n'est plus positif au reequilibrage suivant.

## 5. Backtest de la strategie

### 5.1 Methode

Le backtest est realise sur toute la periode de 2020 a 2026.

Les etapes sont :

1. telecharger les prix ;
2. calculer les signaux ;
3. construire les poids du portefeuille ;
4. calculer les rendements journaliers ;
5. comparer le portefeuille a un benchmark.

### 5.2 Benchmark

Le benchmark choisi est le S&P 500 avec le ticker `^GSPC`.

Ce benchmark est pertinent car les actions selectionnees sont majoritairement des grandes entreprises americaines.

## 6. Indicateurs analyses

Les indicateurs retenus sont volontairement simples :

- rendement total du portefeuille ;
- rendement total du benchmark ;
- nombre de trades ;
- probabilite de reussite des trades ;
- gain moyen des trades gagnants ;
- perte moyenne des trades perdants.

Ces indicateurs permettent deja de repondre aux questions demandees dans le projet.

## 7. Reponse aux questions du sujet

### La strategie est-elle statistiquement rentable ?

La reponse depend des resultats obtenus lors de l'execution du script. Si le rendement total du portefeuille est positif et correct sur toute la periode, on peut conclure que la strategie semble rentable sur l'echantillon teste.

### Quelle est la probabilite de reussite des trades ?

Elle est calculee dans le fichier `summary.txt` avec le pourcentage de trades gagnants.

### Quel est le gain moyen lorsque la strategie fonctionne ?

Il s'agit de la moyenne des rendements des trades positifs.

### Quelle est la perte moyenne lorsque la strategie echoue ?

Il s'agit de la moyenne des rendements des trades negatifs.

## 8. Conclusion

Ce projet montre qu'il est possible de construire une strategie d'investissement simple avec Python en utilisant des donnees reelles.

Le code reste volontairement facile a lire :

- peu de fonctions compliquees ;
- logique claire ;
- fichiers bien separes.

Le projet est donc adapte a un travail de groupe de niveau debutant tout en restant complet sur les 4 parties demandees.
