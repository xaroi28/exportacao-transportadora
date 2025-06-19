import tkinter as tk
import subprocess

# Função para executar o script de incluir comunicado
def run_teste():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\teste.py"
    subprocess.run(["python", script_path])

# Função para executar o script de incluir zeradas
def run_incluir_zeradas():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\mesclados\zerados.py"
    subprocess.run(["python", script_path])

# Função para executar o script de mesclar NF
def run_teste_copia():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\mesclados\mesclados.py"
    subprocess.run(["python", script_path])

# Função para executar o script de excluir PDFs
def run_excluir_pdfs():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\excluir_pdfs.py"
    subprocess.run(["python", script_path])

# Criação da janela principal
root = tk.Tk()
root.title("Inclusão de Comunicado")

# Configuração da largura e altura da janela
root.geometry("300x250")  # Aumentei a altura para acomodar o novo botão
root.configure(bg="#2E2E2E")  # Cor de fundo escura

# Função para estilizar os botões
def create_button(text, command):
    button = tk.Button(
        root, 
        text=text, 
        command=command,
        bg="#4C4C4C",  # Cor de fundo do botão
        fg="#FFFFFF",  # Cor do texto
        font=("Arial", 12, "bold"),
        padx=10,
        pady=5,
        relief=tk.RAISED,
        activebackground="#5C5C5C",  # Cor de fundo quando ativo
        activeforeground="#FFFFFF"  # Cor do texto quando ativo
    )
    button.config(width=20)  # Define a largura do botão
    return button

# Adiciona os botões
button1 = create_button("Incluir Comunicado", run_teste)
button1.pack(pady=10)

button2 = create_button("Incluir Zeradas", run_incluir_zeradas)  # Novo botão
button2.pack(pady=10)

button3 = create_button("Mesclar NF", run_teste_copia)
button3.pack(pady=10)

button4 = create_button("Limpar Pasta", run_excluir_pdfs)
button4.pack(pady=10)

# Inicia o loop da interface
root.mainloop()
