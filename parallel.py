from spacy.lang.en.stop_words import STOP_WORDS
import re           

def process_frame(nlp, text,vocab,total_words):
   
     # chama a função responsável por criar a lista de lemmas
    # limpeza inicial do texto
    # colcoar em caixa baixa
    clean_text = text.lower()

    # remover tags depois de adicionar espaços entre elas, desta forma evitamos
    # certas questões quanto a remover tags, mas elas estarem grudadas no texto 
    # e colarem palavras
    #clean_text = strip_tags(space_tags(clean_text))

    #analisa texto
    doc = nlp(clean_text)
    
    #exporta todos os tokens
    token_list = [token for token in doc]
    
    #exporta todos os tokens evitando stopwords e pontuações
    filtered_tokens = [token for token in doc if not token.is_stop and not token.is_punct]
    
    # pega o lemma dos tokens removendo qualquer outro indicio de caracter especial ou stopword
    # comentei o list comprehention pois estava ficando embaralhado grande o com muita repetição de chamadas
    # lemmas = [ token.lemma_ for token in filtered_tokens if clean_special_chars(token.lemma_) and clean_special_chars(token.lemma_) not in STOP_WORDS]
    
    lemmas = []
    for token in filtered_tokens:
        clean_lemma = re.sub(r'[^a-zA-Z_]+', '', token.lemma_)
        if clean_lemma and clean_lemma not in STOP_WORDS:
            lemmas.append(token.lemma_)

    #conta total words
    #with total_words.get_lock():
    total_words.value += len(lemmas)
    print('total', total_words.value)
    
    for i in range(len(lemmas)):
        if lemmas[i] not in vocab: 
            vocab.append(lemmas[i])
        
    print('vocab', len(vocab))
            