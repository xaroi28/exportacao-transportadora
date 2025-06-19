# Exportacao-transportadora

Este projeto foi desenvolvido em Python com o objetivo de automatizar o tratamento de notas fiscais e boletos em PDF, otimizando tarefas manuais que antes eram repetitivas e suscetíveis a erros. Entre as funcionalidades principais, destacam-se:

Inserção automática de uma imagem padrão em boletos, utilizando bibliotecas como reportlab e PyPDF2;

Mesclagem de notas fiscais com seus respectivos boletos, criando um documento final unificado;

Identificação de notas fiscais sem boletos correspondentes, com separação automática desses arquivos;

Leitura do conteúdo textual dos PDFs para localizar notas com volume zerado, e geração dinâmica de comunicados personalizados via integração com arquivos Word (python-docx e win32com);

Interface gráfica com Tkinter, que centraliza a execução de scripts operacionais (mesclar, limpar, gerar comunicados, etc.);

Barra de progresso no terminal para acompanhar o andamento das execuções;

Limpeza automática de arquivos temporários e PDFs processados, garantindo organização das pastas ao final do processo.

Este é um projeto simples, desenvolvido em um curto período e com foco prático, com soluções diretas e eficientes para atender demandas operacionais urgentes. Apesar da sua simplicidade, ele proporcionou ganhos reais de produtividade ao eliminar tarefas manuais e padronizar documentos gerados diariamente.
