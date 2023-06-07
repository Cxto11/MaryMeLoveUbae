#importações necessárias para o funcionamento do código. 
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

#Essa função resource_path é usada para obter o caminho absoluto dos recursos (imagens). Ela verifica se a aplicação está sendo executada em um pacote congelado (como um executável), caso contrário, usa o diretório atual como base para encontrar os recursos.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

#Essas linhas criam uma janela principal usando a classe Tk do módulo tkinter. A janela é dimensionada para 700x900 pixels e recebe o título 'Aceitas?'. Também define o plano de fundo da janela para uma cor rosa claro.
root = tk.Tk()
root.title('Aceitas?')
root.geometry('700x900')
root.configure(background='#ffc8dd')

#Essas linhas carregam uma imagem (no formato PhotoImage) a partir de um arquivo "dogo.png" localizado na pasta "foti". Em seguida, cria um rótulo (Label) na janela principal (root) para exibir a imagem em toda a janela.
imagem = PhotoImage(file=resource_path('foti/dogo.png'))
label_imagem = Label(root, image=imagem)
label_imagem.place(x=0, y=0, relwidth=1, relheight=1)

#Essa é uma função de callback chamada quando o mouse se move dentro da janela. Ela verifica a posição do cursor em relação ao botão button_1. Se o cursor estiver próximo o suficiente do botão (dentro de um limite de distância), o botão será movido para uma nova posição aleatória dentro da janela.
def move_button_1(e):
    DISTANCE_THRESHOLD = 60
    if abs(e.x - button_1.winfo_x()) < DISTANCE_THRESHOLD and abs(e.y - button_1.winfo_y()) < DISTANCE_THRESHOLD:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

#Essa função é chamada quando o botão "Sim" é clicado. Ela carrega uma nova imagem ("sela.png") usando a biblioteca PIL, cria um objeto ImageTk.PhotoImage a partir dessa imagem e, em seguida, cria uma nova janela (Toplevel) chamada "Imagem" para exibir a imagem carregada. A imagem é exibida em um rótulo (Label) dentro da janela.
def accepted():
    global tk_image
    image = Image.open(resource_path("foti/sela.png"))
    tk_image = ImageTk.PhotoImage(image)
    dialog = Toplevel(root)
    dialog.title("Imagem")
    dialog.configure(background='#ffc8dd')
    label = tk.Label(dialog, image=tk_image)
    label.pack()

#Essa função é chamada quando o botão "Não" é clicado. Ela exibe uma caixa de mensagem com um título de erro e uma mensagem informando ao usuário que deve tentar novamente com as opções disponíveis. Além disso, ela destrói o botão button_1, removendo-o da interface.
def denied():
    messagebox.showinfo('ERRO #!!!!!#!#!!!!!#', 'TENTE NOVAMENTE COM AS OPÇÕES DISPONIVEIS!!!!!!!!!!!!!!!!')
    button_1.destroy()

#Essas linhas criam um objeto Canvas chamado margin dentro da janela principal. O Canvas é usado para desenhar gráficos e formas, mas neste caso está sendo usado apenas para adicionar um espaço vazio entre os elementos da interface.
margin = Canvas(root, width=900, bg='#ffc8dd', height=0, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

#Essas linhas criam um rótulo (Label) chamado text_id com o texto "Quer Casar Comigo?" e o adicionam à janela principal.
text_id = Label(root, bg='#ffc8dd', text='Quer Casar Comigo?', fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack(anchor='center', pady=100)

#Essas linhas criam um botão (1)
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', relief=tk.RIDGE, bd=3, command=denied,
                     font=('Montserrat', 14, 'bold'))
button_1.pack(anchor='center', pady=20)

#Essa linha vincula o evento de movimento do mouse (<Motion>) à função move_button_1. Isso significa que toda vez que o mouse se mover dentro da janela principal, a função move_button_1 será chamada.
root.bind('<Motion>', move_button_1)

#Essas linhas criam um botão (2)
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=tk.RIDGE, bd=3, command=accepted,
                     font=('Montserrat', 14, 'bold'))
button_2.pack()

root.mainloop()