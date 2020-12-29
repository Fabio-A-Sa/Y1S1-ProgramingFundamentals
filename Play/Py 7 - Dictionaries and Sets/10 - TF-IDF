# Created on December, 2020
# @author: Fábio Araújo de Sá

def tf_count(N, n, times):
    # Calculates tf * idf form
    
    from math import log as l
    idf = l(N/n) if n!= 0 else 0
    
    return round(idf*times, 3)

def tfidf(documents):
    
    # Sorted words by occurrence without repetition
    words = []
    for sentence in documents:
        sentence = sentence.lower()
        palavras_separadas = sentence.split()
        for word in palavras_separadas:
            if word not in words:
                words.append(word.lower())
    
    # A dict with all of words
    tf_idf = {}
    for word in words:
        tf_idf[word] = tf_idf.get(word, "something_beautifull")

    # Counter 1 - How many times the "word" appears in the documents' sentences?
    def qtd(word):
        
        n = 0
        for sentence in documents:
            sentence = sentence.lower()
            if word in sentence.split():
                n = n + 1
            else:
                continue
            
        return n
        
    # Counter 2 - How many times the "word" appears in each documents' sentences?
    for word in words:
        counter = []
        for sentence in documents:
            sentence = sentence.lower()
            times = 0
            for x in range(len(sentence.split())):
                if (sentence.split())[x] == word:
                        times = times + 1
                else:
                    continue
            N = len(documents)
            counter.append(tf_count(N, qtd(word), times))
        tf_idf[word] = counter
    
    return tf_idf
