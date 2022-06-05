import googletrans
from googletrans import Translator
 
# print(googletrans.LANGUAGES)


d = googletrans.LANGUAGES

text1 = "안녕하세요" 
t = Translator()

for i in d:
    trans1 = t.translate(text1, src='en', dest=i) 
    print(f"{d[i]} 의 인삿말 : ", trans1.text)



# d =googletrans.LANGUAGES

# text1 = "안녕하세요" 
# t = Translator()

# for i in d:
#     trans1 = t.translate(text1, src='en', dest=i) 
#     print(f"{d[i]} 의 인삿말 : ", trans1.text)