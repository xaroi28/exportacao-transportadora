import os
from PyPDF2 import PdfMerger

pasta_pdfs = r'C:\Users\Visitante\Desktop\exportar DNG\mesclados'

merger = PdfMerger()

arquivos = [f for f in os.listdir(pasta_pdfs) if f.endswith('.pdf')]

arquivos_num = [f for f in arquivos if f.split('.')[0].isdigit()]

arquivos_num.sort(key=lambda x: int(os.path.splitext(x)[0]))

for arquivo in arquivos_num:
    caminho_arquivo = os.path.join(pasta_pdfs, arquivo)
    merger.append(caminho_arquivo)

pdf_final = r'C:\Users\Visitante\Desktop\pdf_mesclado.pdf'

merger.write(pdf_final)

merger.close()

print(f'PDFs mesclados com sucesso! O arquivo final está em: {pdf_final}')
