import os
import sys

# Caminho para a pasta onde os PDFs estão localizados
base_directory = r"C:\Users\Visitante\Desktop\exportar DNG"

# Caminho específico do PDF mesclado na área de trabalho
pdf_mesclado_path = r"C:\Users\Visitante\Desktop\pdf_mesclado.pdf"

# Caminho da pasta "sem boletos"
sem_boletos_directory = r"C:\Users\Visitante\Desktop\teste AF\sem boletos"

# Função para excluir todos os PDFs em subpastas e em locais adicionais
def delete_all_pdfs(directory):
    total_pdfs = 0

    # Conta todos os PDFs nas subpastas de exportar DNG
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                total_pdfs += 1

    # Conta os PDFs da pasta "sem boletos"
    if os.path.exists(sem_boletos_directory):
        for file in os.listdir(sem_boletos_directory):
            if file.endswith('.pdf'):
                total_pdfs += 1

    # Conta o pdf_mesclado
    if os.path.exists(pdf_mesclado_path):
        total_pdfs += 1

    current_process = 0

    # Exclui PDFs na pasta exportar DNG e subpastas
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(dirpath, file)
                os.remove(pdf_path)
                current_process += 1
                print_progress(current_process, total_pdfs)

    # Exclui PDFs na pasta "sem boletos"
    if os.path.exists(sem_boletos_directory):
        for file in os.listdir(sem_boletos_directory):
            if file.endswith('.pdf'):
                pdf_path = os.path.join(sem_boletos_directory, file)
                os.remove(pdf_path)
                current_process += 1
                print_progress(current_process, total_pdfs)

    # Exclui o pdf_mesclado da área de trabalho
    if os.path.exists(pdf_mesclado_path):
        os.remove(pdf_mesclado_path)
        current_process += 1
        print_progress(current_process, total_pdfs)

# Função para atualizar a barra de progresso
def print_progress(current, total):
    percent = (current / total) * 100
    bar_length = 40
    block = int(round(bar_length * percent / 100))
    progress_bar = '█' * block + '-' * (bar_length - block)
    sys.stdout.write(f'\r|{progress_bar}| {percent:.2f}%')
    sys.stdout.flush()

# Executa a função para excluir os PDFs
delete_all_pdfs(base_directory)

# Finaliza a barra de progresso
print_progress(1, 1)
print("\nTodos os PDFs foram excluídos.")
