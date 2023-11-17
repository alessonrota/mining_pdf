import PyPDF2
import pandas as pd
import re

def find_keywords_in_pdf(file_path, keywords):
    # Abre o arquivo PDF
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        results = []

        # Percorre cada página do PDF
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()

            # Para cada palavra-chave, busca no texto
            for keyword in keywords:
                for match in re.finditer(r'\b{}\b'.format(re.escape(keyword)), text):
                    start_index = max(match.start() - 100, 0)
                    end_index = min(match.end() + 100, len(text))

                    # Extrai o contexto da palavra-chave
                    context = text[start_index:end_index]

                    # Adiciona o resultado à lista
                    results.append({
                        'File Name': file_path,
                        'Page': page_num + 1,
                        'Keyword': keyword,
                        'Context': context
                    })

        return results

# Define o caminho do arquivo PDF e as palavras-chave
file_path = 'caminho_do_seu_arquivo.pdf'
keywords = ['palavra1', 'palavra2', 'palavra3']

# Busca as palavras-chave no PDF
results = find_keywords_in_pdf(file_path, keywords)

# Cria um DataFrame com os resultados
df = pd.DataFrame(results)

# Salva o DataFrame em um arquivo CSV
df.to_csv('resultados_de_pesquisa.csv', index=False)

# Imprime as primeiras linhas do DataFrame para verificação
print(df.head())
