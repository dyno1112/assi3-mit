import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("p1.txt")as f:
 text=f.read()
 wordcloud1=WordCloud(collacations=False).generate(text)
 plt.imshow(wordcloud1)
 plt.axis("off")
 plt.show()
