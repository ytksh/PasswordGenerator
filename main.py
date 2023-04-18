import tkinter as tk
import random
import string
import pyperclip

root = tk.Tk()
# definindo largura e altura da janela com base na resolução do usuário
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.4)
window_height = int(screen_height * 0.4)
root.geometry(f"{window_width}x{window_height}")
root.title("Gerador de Senhas")

password_label = tk.Label(root, text="Sua senha: ")
password_label.pack(pady=10)

length_label = tk.Label(root, text="Tamanho da senha: ")
length_label.pack()

length_slider = tk.Scale(root, from_=8, to=32, orient=tk.HORIZONTAL)
length_slider.set(10)
length_slider.pack()

include_label = tk.Label(root, text="Incluir:")
include_label.pack()

var1 = tk.IntVar()
include_specials = tk.Checkbutton(root, text="Caracteres especiais", variable=var1)
include_specials.pack()

var2 = tk.IntVar()
include_numbers = tk.Checkbutton(root, text="Números", variable=var2)
include_numbers.pack()

var3 = tk.IntVar()
include_letters = tk.Checkbutton(root, text="Letras", variable=var3)
include_letters.pack()

def generate_password():
    if var1.get() == 0 and var2.get() == 0 and var3.get() == 0:
        password_label.config(text="Por favor, selecione pelo menos um tipo de caractere")
        return
    if length_slider.get() == 0:
        password_label.config(text="Por favor, selecione um tamanho de senha maior que zero")
        return
    chars = ''
    if var1.get() == 1:
        chars += string.punctuation
    if var2.get() == 1:
        chars += string.digits
    if var3.get() == 1:
        chars += string.ascii_letters
    password = ''.join(random.choices(chars, k=length_slider.get()))
    password_label.config(text="Sua senha: " + password)

generate_button = tk.Button(root, text="Gerar Senha", command=generate_password)
generate_button.pack(pady=10)

def copy_to_clipboard():
    password = password_label["text"].split(": ")[1]
    pyperclip.copy(password)

copy_button = tk.Button(root, text="Copiar para Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
