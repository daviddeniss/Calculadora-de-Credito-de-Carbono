import tkinter as tk 
from tkinter import messagebox 
 
# Função para realizar o cálculo 
def calcular(): 
    opcao = var_opcao.get() 
    try: 
        consumo = int(entry_input.get()) 
        if consumo == 0: 
            messagebox.showinfo('Resultado', f'Você não utiliza {combustivel[opcao]}.') 
        else: 
            calc = (consumo * 12) * fatores[opcao] / 1000 
            arvores = (calc * 1000) / 22  # Cada árvore sequestra  aprox. 22 kg de CO2 por ano 
            custo_creditos = calc * preco_credito  # Preço médio de  R$ 75 por crédito de carbono 
 
            messagebox.showinfo('Resultado', f'Seu uso de {combustivel[opcao]} gera {calc:.2f} tonelada(s) de CO₂ por ano.\n' 
            f'Para compensar, seria necessário plantar aproximadamente {arvores:.0f} árvores.\n' 
            f'O custo estimado dos créditos de carbono seria de R${custo_creditos:.2f}.') 
    except ValueError: 
        messagebox.showerror('Erro', 'Por favor, insira um valor numérico válido.') 
 
# Dados de referência 
combustivel = {'1': 'Gasolina', '2': 'Etanol', '3': 'Diesel', '4': 'GNV'} 
fatores = {'1': 2.31, '2': 1.91, '3': 2.68, '4': 2.68} 
preco_credito = 75  # Preço médio em reais por crédito de carbono (1 tonelada de CO2) 
 
# Configuração da interface gráfica 
root = tk.Tk() 
root.title('Calculadora de Emissões de CO₂ (Combustíveis Fósseis)') 
root.geometry('500x300') 
root.config(bg='#2c3e50') #cor do fundo 
 
# Configuração de layout responsivo 
root.columnconfigure([0, 1], weight=1) 
root.rowconfigure([0, 1, 2, 3], weight=1) 
 
# Entrada de texto para o consumo 
tk.Label(root, text='Consumo mensal (em litros):', bg='#2c3e50', fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='ew') 
entry_input = tk.Entry(root) 
entry_input.grid(row=0, column=1, padx=10, pady=10, sticky='ew') 
 
# Opções de seleção 
var_opcao = tk.StringVar(value='1') 
tk.Radiobutton(root, text='Gasolina', variable=var_opcao, value='1', bg='#2c3e50', fg='white', selectcolor='#FF885B').grid(row=1, column=0, padx=10, pady=5, sticky='ew') 
tk.Radiobutton(root, text='Etanol', variable=var_opcao, value='2', bg='#2c3e50', fg='white', selectcolor='#FF885B').grid(row=1, column=1, padx=10, pady=5, sticky='ew') 
tk.Radiobutton(root, text='Diesel', variable=var_opcao, value='3', bg='#2c3e50', fg='white', selectcolor='#FF885B').grid(row=2, column=0, padx=10, pady=5, sticky='ew') 
tk.Radiobutton(root, text='GNV', variable=var_opcao, value='4', bg='#2c3e50', fg='white', selectcolor='#FF885B').grid(row=2, column=1, padx=10, pady=5, sticky='ew') 
 
# Botão de cálculo sem borda 
tk.Button(root, text='Calcular', command=calcular, width=20, 
bg='#00ff9c', fg='black', relief='flat', borderwidth=0).grid(row=3, 
column=0, columnspan=2, pady=10) 
 
# Iniciar o loop principal 
root.mainloop()