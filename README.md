# nlp-sentiment-analysis

## Setup the Project

```
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Exercicio 1

Exercício para dia 17 equipes de até 3

Os dados estão no arquivo imdb.csv;

1) Limpar dados com stopwords , regex, stem ou lemma, (nltk ou spacy)

2) Criar um classificador (não bayes)

3) Calcular a acurácia do seu classificador com testes

______________________________________________________
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Wow, NLTK is really powerful!")
{'neg': 0.0, 'neu': 0.295, 'pos': 0.705, 'compound': 0.8012}

4)Comparar os resultados (acurácia) do sia com os do seu classificador


*Um notebook do jupyter postado em seu github (link na atividade do ava)


## Authors

Developed by: Evandro Matheus Schmitz, Leonardo Fiedler and Recigio Poffo.