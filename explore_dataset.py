import pandas as pd

# Specifica il percorso del file del dataset
file_path = 'dataset/cleaned_datasetwine.csv'
pd.set_option('display.max_columns', None)

def explore_dataset(file_path):
    # Carica il dataset
    df = pd.read_csv(file_path)

    
    
    # Mostra le prime righe del dataset
    print("Prime 5 righe del dataset:")
    print(df.head())
    
    # Mostra informazioni generali sul dataset
    print("\nInformazioni generali sul dataset:")
    print(df.info())
    
    # Mostra statistiche descrittive del dataset
    print("\nStatistiche descrittive del dataset:")
    print(df.describe())
    
    # Mostra la presenza di valori mancanti
    print("\nValori mancanti per colonna:")
    print(df.isnull().sum())



    print(f"Il dataset originale ha {df.shape[0]} righe e {df.shape[1]} colonne")

# Esplora il dataset
explore_dataset(file_path)
