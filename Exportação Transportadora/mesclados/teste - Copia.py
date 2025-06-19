import os
from PyPDF2 import PdfReader, PdfWriter
import sys

def merge_all_pdfs(pdf_directory, output_pdf):
    writer = PdfWriter()
    
    pdf_files = sorted([f for f in os.listdir(pdf_directory) if f.endswith('.pdf')])

    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_directory, pdf_file)
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

def print_progress(current, total):
    percent = (current / total) * 100
    bar_length = 40
    block = int(round(bar_length * percent / 100))
    progress_bar = '█' * block + '-' * (bar_length - block)
    sys.stdout.write(f'\r|{progress_bar}| {percent:.2f}%')
    sys.stdout.flush()

mesclados_directory = r"C:\Users\marcos.tulio\Desktop\exportar DNG\mesclados"
output_pdf_path = os.path.join(mesclados_directory, "todos_os_pdfs_mesclados.pdf")

pdf_files = [f for f in os.listdir(mesclados_directory) if f.endswith('.pdf')]
total_processes = len(pdf_files)
current_process = 0

merge_all_pdfs(mesclados_directory, output_pdf_path)

print_progress(total_processes, total_processes)
print("\nProcesso concluído.")
