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
```python
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()
sia.polarity_scores("Wow, NLTK is really powerful!")
```
```console
{'neg': 0.0, 'neu': 0.295, 'pos': 0.705, 'compound': 0.8012}
```

4)Comparar os resultados (acurácia) do sia com os do seu classificador


*Um notebook do jupyter postado em seu github (link na atividade do ava)


## Authors

Developed by: Evandro Matheus Schmitz, Leonardo Fiedler and Recigio Poffo.

## Análise de Resultados com 10k dados

logistic_regression
---
Train - Accuracy: 0.8774444444444445  
Train - Precision: 0.8685542720324875  
Train - Recall: 0.8896000000000001  
Train - Fscore: 0.8789416269136285  

Test - Accuracy: 0.8382  
Test - Precision: 0.8292218953389441  
Test - Recall: 0.8523999999999999  
Test - Fscore: 0.8404873169934663  


xgboost
---
Train - Accuracy: 0.9137777777777778  
Train - Precision: 0.8950002334083923  
Train - Recall: 0.9380666666666666  
Train - Fscore: 0.9159943215020434  

Test - Accuracy: 0.8146000000000001  
Test - Precision: 0.7991287731653458  
Test - Recall: 0.8408  
Test - Fscore: 0.8192952511878564  


mlp
---
Train - Accuracy: 0.9995666666666667  
Train - Precision: 0.9996447404732312  
Train - Recall: 0.9994888888888888  
Train - Fscore: 0.9995662396062135  

Test - Accuracy: 0.7894  
Test - Precision: 0.792118779351039  
Test - Recall: 0.785  
Test - Fscore: 0.788402016300736  

Melhores parâmetros: {'hidden_layer_sizes': 11, 'max_iter': 2000, 'solver': 'lbfgs'}

## Análise de Resultados com 30k dados


logistic_regression
---
Train - Accuracy: 0.8644333333333334  
Train - Precision: 0.853277569694183  
Train - Recall: 0.880251851851852  
Train - Fscore: 0.8665497361716412  

Test - Accuracy: 0.851  
Test - Precision: 0.8405017948165039  
Test - Recall: 0.8664666666666667  
Test - Fscore: 0.8532738359560665  


xgboost
---
Train - Accuracy: 0.9189259259259259  
Train - Precision: 0.9039895699911117  
Train - Recall: 0.9374148148148149  
Train - Fscore: 0.9203979438411685  

Test - Accuracy: 0.8279666666666665  
Test - Precision: 0.8169500726728375  
Test - Recall: 0.8454666666666666  
Test - Fscore: 0.8309464314954284  


mlp
---
Train - Accuracy: 0.998948148148148  
Train - Precision: 0.9990142504608055  
Train - Recall: 0.9988814814814815  
Train - Fscore: 0.9989476337918202  

Test - Accuracy: 0.7951333333333334  
Test - Precision: 0.7916816834940178  
Test - Recall: 0.8012666666666668  
Test - Fscore: 0.7964063442145081  

Melhores parâmetros: {'hidden_layer_sizes': 13, 'max_iter': 1000, 'solver': 'lbfgs'}
