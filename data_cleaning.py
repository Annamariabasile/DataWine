import pandas as pd

# percorso file del dataset originale
original_file_path = 'dataset/datasetwine.csv'
# percorso file del dataset pulito
cleaned_file_path = 'dataset/cleaned_datasetwine.csv'

def clean_dataset(file_path, cleaned_file_path):
    df = pd.read_csv(file_path)
    
    # Esempi di operazioni di pulizia
    df.dropna(inplace=True)  # Rimuovi righe con valori mancanti 

    #elimina colonne regione_1, regione_2, assaggiatore_twitter
    columns_to_drop = ['Unnamed: 0','region_1', 'region_2', 'taster_twitter_handle']  # Sostituisci con i nomi delle colonne da eliminare
    df.drop(columns=columns_to_drop, axis=1, inplace=True)

    #elimina duplicati
    df=df.drop_duplicates()
    
    # Salva il dataset pulito
    df.to_csv(cleaned_file_path, index=False)
    print(f"Dataset pulito salvato in: {cleaned_file_path}")
    
    return df

# pulisco il dataset e lo salvo
df = clean_dataset(original_file_path, cleaned_file_path)

