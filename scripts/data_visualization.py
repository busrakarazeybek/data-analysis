import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(input_file):
    df = pd.read_csv(input_file)
    # Create a simple plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='category', y='value', data=df)
    plt.title('Category vs Value')
    plt.savefig('reports/visualization.png')
    plt.show()

if __name__ == "__main__":
    visualize_data('data/processed/cleaned_data.csv')
