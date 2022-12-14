from gensim.models import Word2Vec

model = Word2Vec.load('../data/wiki.model')

print('Python, 파이썬')
print(model.wv.most_similar(['Python', '파이썬']))
print()
print('positive(아빠, 여성), negative=남성')
print(model.wv.most_similar(positive=['아빠', '여성'], negative='남성'))
print()
print('positive(왕자, 여성), negative=남성')
print(model.wv.most_similar(positive=['왕자', '여성'], negative='남성')[:5])
print()
print('positive=(서울, 일본), negative=한국')
print(model.wv.most_similar(positive=['서울', '일본'], negative='한국')[:5])
print()
print('positive=(오른쪽, 남자), negative=왼쪽')
print(model.wv.most_similar(positive=['오른쪽', '남자'], negative='왼쪽')[:5])
print()
print('서울, 맛집')
print(model.wv.most_similar(positive=['서울', '맛집']))
print()
print('고양이')
print(model.wv['고양이'])

