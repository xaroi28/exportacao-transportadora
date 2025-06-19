import os
import sys

base_directory = r"C:\Users\Visitante\Desktop\exportar DNG"

pdf_mesclado_path = r"C:\Users\Visitante\Desktop\pdf_mesclado.pdf"

sem_boletos_directory = r"C:\Users\Visitante\Desktop\teste AF\sem boletos"

def delete_all_pdfs(directory):
    total_pdfs = 0
    for dirpath, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                total_pdfs += 1

    if os.path.exists(sem_boletos_directory):
        for file in os.listdir(sem_boletos_directory):
            if file.endswith('.pdf'):
                total_pdfs += 1

    if os.path.exists(pdf_mesclado_path):
        total_pdfs += 1

    current_process = 0

    for dirpath, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_path = os.path.join(dirpath, file)
                os.remove(pdf_path)
                current_process += 1
                print_progress(current_process, total_pdfs)

    if os.path.exists(sem_boletos_directory):
        for file in os.listdir(sem_boletos_directory):
            if file.endswith('.pdf'):
                pdf_path = os.path.join(sem_boletos_directory, file)
                os.remove(pdf_path)
                current_process += 1
                print_progress(current_process, total_pdfs)

    if os.path.exists(pdf_mesclado_path):
        os.remove(pdf_mesclado_path)
        current_process += 1
        print_progress(current_process, total_pdfs)

def print_progress(current, total):
    percent = (current / total) * 100
    bar_length = 40
    block = int(round(bar_length * percent / 100))
    progress_bar = '█' * block + '-' * (bar_length - block)
    sys.stdout.write(f'\r|{progress_bar}| {percent:.2f}%')
    sys.stdout.flush()

delete_all_pdfs(base_directory)

print_progress(1, 1)
print("\nTodos os PDFs foram excluídos.")
