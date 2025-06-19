import os
from PyPDF2 import PdfMerger

# Caminho da pasta onde os arquivos PDF estão localizados
pasta_pdfs = r'C:\Users\Visitante\Desktop\exportar DNG\mesclados'

# Cria uma instância do PdfMerger
merger = PdfMerger()

# Lista todos os arquivos na pasta
arquivos = [f for f in os.listdir(pasta_pdfs) if f.endswith('.pdf')]

# Filtra apenas arquivos com nomes numéricos
arquivos_num = [f for f in arquivos if f.split('.')[0].isdigit()]

# Ordena os arquivos numericamente pelo nome
arquivos_num.sort(key=lambda x: int(os.path.splitext(x)[0]))

# Adiciona cada PDF ao merger na ordem
for arquivo in arquivos_num:
    caminho_arquivo = os.path.join(pasta_pdfs, arquivo)
    merger.append(caminho_arquivo)

# Novo caminho para salvar o PDF final na área de trabalho
pdf_final = r'C:\Users\Visitante\Desktop\pdf_mesclado.pdf'

# Escreve o PDF final com os arquivos mesclados
merger.write(pdf_final)

# Fecha o PdfMerger
merger.close()

print(f'PDFs mesclados com sucesso! O arquivo final está em: {pdf_final}')
