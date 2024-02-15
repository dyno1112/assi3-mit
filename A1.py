import nltk
nltk.download('stopwords')
nltk.download('punkt')

import re
text="""
Mumbai (/mʊmˈbaɪ/ ⓘ, Marathi: [ˈmumbəi], IAST: Muṃbaī; formerly known as Bombay[a] — the official name until 1995) is the capital city of the Indian state of Maharashtra. Mumbai is the de facto financial centre and the most populous city of India with an estimated city proper population of 12.5 million (1.25 crore).[19] Mumbai is the centre of the Mumbai Metropolitan Region, the sixth most populous metropolitan area in the world with a population of over 23 million (2.3 crore) living within the Mumbai Metropolitan Region.[20] Mumbai lies on the Konkan coast on the west coast of India and has a deep natural harbour. In 2008, Mumbai was named an alpha world city.[21][22]
"""

formatted_text=re.sub('[^a-zA-Z]',' ',text)


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize,sent_tokenize
stopWords=set(stopwords.words("english"))
print(stopWords)
words=word_tokenize(formatted_text)
wordfreq={}
print(formatted_text)
print(words)
for word in words:
        if word in stopWords:
             continue
        if word in wordfreq:
             wordfreq[word] += 1
        else:
             wordfreq[word] = 1
print(wordfreq)
maximum_frequency=max(wordfreq.values())
for word in wordfreq.keys():
      wordfreq[word]=(wordfreq[word]/maximum_frequency)
sentences=sent_tokenize(text)
sentenceValue={}
for sentence in sentences:
    for word, freq in wordfreq.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                 sentenceValue[sentence]+=freq
            else:
                 sentenceValue[sentence]=freq
import heapq
summary=''
summary_sentences=heapq.nlargest(4,sentenceValue,key=sentenceValue.get)
summary=''.join(summary_sentences)
print(summary)                     
                                       



