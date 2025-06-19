import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import sys

sem_boletos_directory = r"C:\Users\Visitante\Desktop\teste AF\sem boletos"
os.makedirs(sem_boletos_directory, exist_ok=True)

def create_pdf_with_image(image_path):
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    
    width, height = letter
    original_image_width = 400  # Largura original
    original_image_height = 100  # Altura original
    increased_width = original_image_width + 130  # Aumenta a largura total em 130px
    increased_height = original_image_height + 150  # Aumenta a altura em 90px

    
    x_position = (width - increased_width) / 2
    y_position = 20 

    c.drawImage(image_path, x_position, y_position, width=increased_width, height=increased_height)
    c.save()
    
    packet.seek(0)
    return PdfReader(packet)

def add_image_to_pdf(original_pdf, image_path, output_pdf):
    reader = PdfReader(original_pdf)
    writer = PdfWriter()

    overlay_pdf = create_pdf_with_image(image_path)
    
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        if i < len(overlay_pdf.pages):
            page.merge_page(overlay_pdf.pages[0]) 
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

def merge_nf_and_boletos(nf_pdf, boleto_pdfs, output_pdf):
    writer = PdfWriter()
    reader_nf = PdfReader(nf_pdf)

    for page in reader_nf.pages:
        writer.add_page(page)

    for boleto_pdf in boleto_pdfs:
        reader_boleto = PdfReader(boleto_pdf)
        for page in reader_boleto.pages:
            writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)

def merge_all_pdfs(pdf_list, output_pdf):
    writer = PdfWriter()
    for pdf in pdf_list:
        reader = PdfReader(pdf)
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

image_path = r"C:\Users\Visitante\Desktop\exportar DNG\imagem\image.png"

pdf_directory = r"C:\Users\Visitante\Desktop\exportar DNG"
altered_directory = os.path.join(pdf_directory, "alterados")
merged_directory = os.path.join(pdf_directory, "mesclados")

os.makedirs(altered_directory, exist_ok=True)
os.makedirs(merged_directory, exist_ok=True)

boletos_por_nf = {}

for filename in os.listdir(pdf_directory):
    if filename.startswith("bol") and filename.endswith(".pdf"):
        parts = filename.split('_')
        if len(parts) > 1:
            nf_number = parts[1][-6:]
            if nf_number not in boletos_por_nf:
                boletos_por_nf[nf_number] = []
            boletos_por_nf[nf_number].append(os.path.join(pdf_directory, filename))

total_processes = len(boletos_por_nf) + len([f for f in os.listdir(pdf_directory) if f.startswith("nf") and f.endswith(".pdf")])
current_process = 0

for filename in sorted(os.listdir(pdf_directory)):
    if filename.startswith("nf") and filename.endswith(".pdf"):
        parts = filename.split('_')
        if len(parts) > 1:
            nf_number = parts[1][-6:]
            nf_pdf_path = os.path.join(pdf_directory, filename)

            if nf_number in boletos_por_nf:
                for i, boleto_pdf_path in enumerate(boletos_por_nf[nf_number]):
                    boleto_output_path = os.path.join(altered_directory, f"{nf_number} - {i + 1}.pdf")
                    add_image_to_pdf(boleto_pdf_path, image_path, boleto_output_path)
                merge_nf_and_boletos(
                    nf_pdf_path,
                    sorted([os.path.join(altered_directory, f"{nf_number} - {i + 1}.pdf") for i in range(len(boletos_por_nf[nf_number]))]),
                    os.path.join(merged_directory, f"{nf_number}.pdf")
                )

            else:
                new_nf_path = os.path.join(sem_boletos_directory, filename)
                os.rename(nf_pdf_path, new_nf_path)

            current_process += 1
            print_progress(current_process, total_processes)

all_merged_pdfs = sorted([os.path.join(merged_directory, f) for f in os.listdir(merged_directory) if f.endswith('.pdf')])
if all_merged_pdfs:
    final_output_path = os.path.join(pdf_directory, "todas_as_nfs_mescladas.pdf")
    merge_all_pdfs(all_merged_pdfs, final_output_path)

print_progress(total_processes, total_processes)
print("\nProcesso concluído.")
