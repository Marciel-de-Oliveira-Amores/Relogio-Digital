import tkinter as tk
from time import strftime

# Função para atualizar o tempo
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Configuração da janela principal
root = tk.Tk()
root.title('Relógio Digital')

# Rótulo para exibir o tempo
lbl = tk.Label(root, font=('calibri', 40, 'bold'),
               background='purple',
               foreground='white')

# Posicionamento do rótulo na janela
lbl.pack(anchor='center')

# Chamada inicial para a função time
time()

# Executar o loop principal da aplicação
root.mainloop()
