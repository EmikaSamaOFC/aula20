import pandas as pd
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para carregar dados do CSV
def load_data():
    return pd.read_csv('olimpiadas_2024.csv')

# Função para gerar gráficos
def generate_plot():
    chart_type = chart_type_var.get()
    fig, ax = plt.subplots(figsize=(8, 6))

    if chart_type == "Barra":
        df.plot(kind='bar', x='País', y=['Medalhas_Ouro', 'Medalhas_Prata', 'Medalhas_Bronze'], ax=ax)
    elif chart_type == "Linha":
        df.plot(kind='line', x='País', y=['Medalhas_Ouro', 'Medalhas_Prata', 'Medalhas_Bronze'], ax=ax)
    elif chart_type == "Pizza":
        medalhas = df[['Medalhas_Ouro', 'Medalhas_Prata', 'Medalhas_Bronze']].sum()
        ax.pie(medalhas, labels=medalhas.index, autopct='%1.1f%%')
        ax.set_title('Distribuição de Medalhas')
    else:
        return

    ax.set_title('Medalhas por País')
    ax.set_xlabel('País')
    ax.set_ylabel('Número de Medalhas')
    plt.tight_layout()

    # Limpar o canvas e exibir o novo gráfico
    canvas.get_tk_widget().pack_forget()
    new_canvas = FigureCanvasTkAgg(fig, master=window)
    new_canvas.draw()
    new_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Carregar dados
df = load_data()

# Configuração da Interface Gráfica
window = tk.Tk()
window.title("Análise dos Dados das Olimpíadas 2024")

# Label
label = tk.Label(window, text="Escolha o Tipo de Gráfico")
label.pack(pady=10)

# Radio Buttons para escolher o tipo de gráfico
chart_type_var = tk.StringVar(value="Barra")
bar_radio = tk.Radiobutton(window, text="Barra", variable=chart_type_var, value="Barra")
line_radio = tk.Radiobutton(window, text="Linha", variable=chart_type_var, value="Linha")
pie_radio = tk.Radiobutton(window, text="Pizza", variable=chart_type_var, value="Pizza")

bar_radio.pack()
line_radio.pack()
pie_radio.pack()

# Botão para gerar o gráfico
plot_button = tk.Button(window, text="Gerar Gráfico", command=generate_plot)
plot_button.pack(pady=10)

# Canvas para exibir o gráfico
fig = plt.figure()  # Inicializar um objeto figure globalmente
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Iniciar o loop da interface gráfica
window.mainloop()
