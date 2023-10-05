import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Baixe os recursos do NLTK (necessário apenas na primeira execução)
nltk.download('vader_lexicon')

# URL da página
url = "https://www.infomoney.com.br/mercados/ceo-da-apple-se-desfaz-de-us-41-milhoes-em-acoes-da-companhia-na-sua-maior-venda-em-dois-anos/"
#url = "https://pt.wikipedia.org/wiki/BOM"

# Função para analisar o sentimento do texto
def analyze_sentiment(text):
    # Inicialize o analisador de sentimentos
    sia = SentimentIntensityAnalyzer()

    # Calcule a polaridade do sentimento
    sentiment = sia.polarity_scores(text)

    # Determine o sentimento com base na polaridade composta
    if sentiment['compound'] > 0.05:
        return "Positivo"
    elif sentiment['compound'] < -0.05:
        return "Negativo"
    else:
        return "Neutro"

# Recupere o texto da página
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
text = soup.get_text()

# Pré-processamento de texto
text = re.sub(r'[^\w\s]', '', text)
text = text.lower()

# Analise o sentimento do texto
sentiment = analyze_sentiment(text)

# Exiba o resultado
print(f"Sentimento do Texto: {sentiment}")