# Projet Python - Analyse et strategie d'investissement

Ce projet propose une solution simple, complete et accessible pour un projet de finance en Python.

Le projet contient 4 parties :

1. constitution d'une base de donnees financieres ;
2. definition d'une strategie d'investissement ;
3. allocation et gestion d'un portefeuille ;
4. backtest sur plus de 5 ans.

Le style du code est volontairement simple pour rester proche d'un niveau debutant.

## Choix du projet

- Source des donnees : Yahoo Finance avec `yfinance`
- Nombre d'entreprises : 30 actions americaines
- Historique : du 1er janvier 2020 au 1er mars 2026
- Frequence : journaliere
- Benchmark : S&P 500 (`^GSPC`)

## Strategie choisie

La strategie est une strategie de suivi de tendance tres simple :

- on calcule une moyenne mobile courte sur 20 jours ;
- on calcule une moyenne mobile longue sur 50 jours ;
- si la moyenne mobile 20 jours est superieure a la moyenne mobile 50 jours, l'action est selectionnee ;
- sinon, on ne la prend pas.

Ensuite :

- le portefeuille est reequilibre au debut de chaque mois ;
- on garde au maximum 10 actions ;
- les poids sont egaux entre les actions selectionnees.

## Contenu des fichiers

- `main.py` : script principal
- `src/config.py` : parametres du projet
- `src/data_loader.py` : telechargement et preparation des donnees
- `src/strategy.py` : calcul des signaux
- `src/portfolio.py` : allocation du portefeuille
- `src/backtest.py` : simulation et resultats
- `rapport_projet.md` : rapport redige

## Installation

```bash
pip install -r requirements.txt
```

## Execution

```bash
python main.py
```

## Resultats produits

Le script cree un dossier `outputs/` avec :

- `price_data.csv` : prix historiques des actions
- `benchmark_data.csv` : prix historiques du benchmark
- `signals.csv` : signaux d'achat
- `portfolio_weights.csv` : poids du portefeuille
- `portfolio_value.csv` : evolution de la valeur du portefeuille
- `trade_results.csv` : details des trades
- `summary.txt` : resume final

## Remarque

Le telechargement de donnees demande une connexion internet au moment de l'execution.
