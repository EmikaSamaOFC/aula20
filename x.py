import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Label, Button, filedialog

def load_data(file_path):
    """
    Carrega os dados de um arquivo CSV.
    """
    return pd.read_csv(file_path)

def plot_sales_analysis(df):
    """
    Cria gráficos de análise de vendas.
    """
    plt.figure(figsize=(12, 6))

    # Gráfico de vendas por produto
    sales_by_product = df.groupby('produto')['quantidade_vendida'].sum().reset_index()
    sns.barplot(x='produto', y='quantidade_vendida', data=sales_by_product)
    plt.title('Quantidade Vendida por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.show()
    
    # Gráfico de vendas ao longo do tempo
    df['data'] = pd.to_datetime(df['data'])
    sales_by_date = df.groupby('data')['quantidade_vendida'].sum().reset_index()
    sns.lineplot(x='data', y='quantidade_vendida', data=sales_by_date)
    plt.title('Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.show()

def open_file():
    """
    Abre um arquivo CSV e realiza a análise de vendas.
    """
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        df = load_data(file_path)
        plot_sales_analysis(df)

def create_interface():
    """
    Cria uma interface gráfica simples para carregar o arquivo CSV.
    """
    root = Tk()
    root.title('Análise de Vendas')
    
    Label(root, text='Clique para carregar dados de vendas:').pack(pady=10)
    Button(root, text='Abrir Arquivo CSV', command=open_file).pack(pady=10)
    
    root.mainloop()

# Executa a interface gráfica diretamente
create_interface()