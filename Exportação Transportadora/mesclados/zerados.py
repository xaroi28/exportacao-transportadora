import os
import PyPDF2
import re
from docx import Document
import win32com.client as win32
import uuid  


pasta_pdf = r'C:\Users\Visitante\Desktop\exportar DNG\mesclados'
pasta_temp = os.path.join(pasta_pdf, 'temp')  

if not os.path.exists(pasta_temp):
    os.makedirs(pasta_temp)

caminho_word = r'C:\Users\Visitante\Desktop\exportar DNG\imagem\VOLUME ZERADO.docx'

def extrair_texto_pdf(caminho_pdf):
    with open(caminho_pdf, 'rb') as arquivo:
        leitor_pdf = PyPDF2.PdfReader(arquivo)
        texto = ""
        for pagina in range(len(leitor_pdf.pages)):
            texto += leitor_pdf.pages[pagina].extract_text()
        return texto

def verificar_volume_zerado(texto_pdf):
    resultado = re.search(r'(\d+)\s*VOLUME', texto_pdf)
    if resultado:
        valor_antes_volume = resultado.group(1) 
        if valor_antes_volume == "0":
            return True
    return False

def substituir_e_gerar_pdf(numero_nf):
    doc = Document(caminho_word)
    
    for paragrafo in doc.paragraphs:
        if '654321' in paragrafo.text:
            paragrafo.text = paragrafo.text.replace('654321', str(numero_nf))
    
    numero_nf_anterior = numero_nf - 1
    for paragrafo in doc.paragraphs:
        if '123456' in paragrafo.text:
            paragrafo.text = paragrafo.text.replace('123456', str(numero_nf_anterior))
    nome_aleatorio = str(uuid.uuid4()) 

    caminho_docx_temp = os.path.join(pasta_temp, f'{nome_aleatorio}.docx')
    caminho_pdf_temp = os.path.join(pasta_temp, f'{nome_aleatorio}.pdf')
    
    doc.save(caminho_docx_temp)

    word = win32.Dispatch("Word.Application")
    doc = word.Documents.Open(caminho_docx_temp)
    doc.SaveAs(caminho_pdf_temp, FileFormat=17) 
    doc.Close()
    word.Quit()

    return caminho_pdf_temp

def mesclar_pdfs(pdf_lista, caminho_pdf_saida):
    pdf_writer = PyPDF2.PdfWriter()
    
    for pdf in pdf_lista:
        with open(pdf, 'rb') as arquivo_pdf:
            pdf_reader = PyPDF2.PdfReader(arquivo_pdf)
            for pagina in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[pagina])

    with open(caminho_pdf_saida, 'wb') as arquivo_saida:
        pdf_writer.write(arquivo_saida)

def encontrar_nfs_zeradas():
    arquivos_zerados = []
    for arquivo in os.listdir(pasta_pdf):
        if arquivo.endswith('.pdf'):
            caminho_pdf = os.path.join(pasta_pdf, arquivo)
            texto_pdf = extrair_texto_pdf(caminho_pdf)
            if verificar_volume_zerado(texto_pdf):
                numero_nf = int(arquivo.split('.')[0]) 
                arquivos_zerados.append((numero_nf, caminho_pdf))
    return arquivos_zerados

def renomear_arquivos(originais):
    renomeados = []
    for arquivo in originais:
        novo_nome = arquivo.replace('.pdf', ' - original.pdf')
        novo_caminho = os.path.join(pasta_pdf, os.path.basename(novo_nome))
        os.rename(arquivo, novo_caminho)
        renomeados.append(novo_caminho)
    return renomeados

def excluir_arquivos(*arquivos):
    for arquivo in arquivos:
        if os.path.exists(arquivo):
            os.remove(arquivo)
            print(f"Arquivo {arquivo} excluído.")

nfs_zeradas = encontrar_nfs_zeradas()

if nfs_zeradas:
    for numero_nf, caminho_pdf_zerada in nfs_zeradas:
        print(f"Processando a NF zerada {numero_nf}...")
        
        numero_nf_anterior = numero_nf - 1
        caminho_pdf_anterior = os.path.join(pasta_pdf, f"{numero_nf_anterior}.pdf")

        arquivos_renomeados = renomear_arquivos([caminho_pdf_zerada, caminho_pdf_anterior])
        
        caminho_pdf_aviso = substituir_e_gerar_pdf(numero_nf)
        
        caminho_pdf_saida = os.path.join(pasta_pdf, f"{numero_nf}.pdf")
        mesclar_pdfs([caminho_pdf_aviso] + arquivos_renomeados, caminho_pdf_saida)
        
        print(f"Arquivo gerado: {caminho_pdf_saida}")
        
        excluir_arquivos(*arquivos_renomeados)
else:
    print("Não foram encontradas NFs com volume zerado.")
