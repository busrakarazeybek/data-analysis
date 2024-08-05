import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)
    # Perform data cleaning operations
    df.dropna(inplace=True)
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved to {output_file}")

if __name__ == "__main__":
    clean_data('data/raw/sample_data.csv', 'data/processed/cleaned_data.csv')
