import pandas as pd
import os

def clean_and_merge_data(raw_data_dir='data/raw/'):
    """
    Standardizes and merges World Happiness Report CSVs from 2015-2022.
    """
    all_years = []
    
    # Mapping for column standardization
    column_mapping = {
        'Country': ['Country', 'Country or region', 'Country name'],
        'Happiness Score': ['Happiness Score', 'Happiness.Score', 'Score', 'Ladder score'],
        'GDP per capita': ['Economy (GDP per Capita)', 'Economy..GDP.per.Capita.', 'GDP per capita', 'Explained by: GDP per capita'],
        'Social Support': ['Family', 'Social support', 'Explained by: Social support'],
        'Healthy Life Expectancy': ['Health (Life Expectancy)', 'Health..Life.Expectancy.', 'Healthy life expectancy', 'Explained by: Healthy life expectancy'],
        'Freedom': ['Freedom', 'Freedom to make life choices', 'Explained by: Freedom to make life choices'],
        'Generosity': ['Generosity', 'Explained by: Generosity'],
        'Corruption': ['Trust (Government Corruption)', 'Trust..Government.Corruption.', 'Perceptions of corruption', 'Explained by: Perceptions of corruption']
    }

    files = sorted([f for f in os.listdir(raw_data_dir) if f.endswith('.csv')])
    
    for file in files:
        year = file.split('.')[0]
        df = pd.read_csv(os.path.join(raw_data_dir, file))
        
        # Standardize columns using the mapping
        new_df = pd.DataFrame()
        new_df['Year'] = [int(year)] * len(df)
        
        for standard_name, variants in column_mapping.items():
            for variant in variants:
                if variant in df.columns:
                    new_df[standard_name] = df[variant]
                    break
        
        all_years.append(new_df)
    
    # Merge all years and handle missing values [cite: 318, 320]
    final_df = pd.concat(all_years, ignore_index=True)
    final_df = final_df.dropna(subset=['Happiness Score'])
    
    # Save processed data
    os.makedirs('data/processed/', exist_ok=True)
    final_df.to_csv('data/processed/merged_happiness_data.csv', index=False)
    print(f"Successfully merged {len(files)} years of data.")
    return final_df

# Run cleaning
merged_df = clean_and_merge_data()