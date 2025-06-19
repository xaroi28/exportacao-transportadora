import tkinter as tk
import subprocess

def run_teste():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\teste.py"
    subprocess.run(["python", script_path])

def run_incluir_zeradas():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\mesclados\zerados.py"
    subprocess.run(["python", script_path])

def run_teste_copia():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\mesclados\mesclados.py"
    subprocess.run(["python", script_path])

def run_excluir_pdfs():
    script_path = r"C:\Users\Visitante\Desktop\exportar DNG\excluir_pdfs.py"
    subprocess.run(["python", script_path])

root = tk.Tk()
root.title("Inclusão de Comunicado")

root.geometry("300x250")
root.configure(bg="#2E2E2E")

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
    button.config(width=20) 
    return button

button1 = create_button("Incluir Comunicado", run_teste)
button1.pack(pady=10)

button2 = create_button("Incluir Zeradas", run_incluir_zeradas)  # Novo botão
button2.pack(pady=10)

button3 = create_button("Mesclar NF", run_teste_copia)
button3.pack(pady=10)

button4 = create_button("Limpar Pasta", run_excluir_pdfs)
button4.pack(pady=10)

root.mainloop()
