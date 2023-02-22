import pandas as pd
import numpy as np

df = pd.read_csv('Youtube_ing.csv')

#1- ilk 10 kaydı getirin

result = df.head(10)

#2- ikinci 5 kaydı getirin.

result = df[5:].head()

#3- Dataset' de bulunan kolon isimleri ve sayısını bulun

result = df.columns
result = len(df.columns)

#4- Aşağıda bulunan bazı kolonları silin ve kalan kolonları listede gösterin
df.drop(['thumbnail_link','comments_disabled'],inplace=True,axis=1)

#print(df)

#5- Beğenme (like) ve beğenmeme (dislike) sayılarının ortalamasını gösterin

result = df[['likes','dislikes']].mean()

#6- ilk 50 videonun like ve dislike kolonarını getirin

result = df[['likes','dislikes']].head(50)

#7- En çok görüntülenen video hangisidir?

result = df[df['views']==df['views'].max()]['title']

#8- En düşük görüntülenen video hangisidir?

result = df[df['views']==df['views'].min()]['title']

#9- En fazla görüntülenen ilk 10 video hangisidir?

result = df.sort_values('views',ascending=False).head(10)[['title','views']]

#10- Kategoriye göre begeni ortalamalarını sıralı şekilde getirin

result = df.groupby('category_id').mean().sort_values('likes')['likes']

#11- Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.

result = df.groupby('category_id').count().sort_values('comment_count',ascending=False)['comment_count']

#12 Her kategoride kaç video vardır?

result = df['category_id'].value_counts()

#13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösterin

#df['title_length'] = df['title'].str.len()
#print(df)
#df['title_length'] = df['title'].apply(len)  alternatif

#14- Her video için kullanılan tag sayısını yeni kolonda gösterin.

df['tag_count'] = df['tags'].apply(lambda x: len(x.split('|')))  #tag isimlerini | e göre ayırıp sayısını hesapladık.

#def tagCount(tag):
#    return  len(tag.split('|'))
#df['tag_count'] = df['tags'].apply(tagCount)


#15- En popüler videoları listeleyin. (like/dislike oranına göre)
def likedislikeoranhesapla(dataset):

    likesList = list(dataset['likes'])
    dislikesList = list(dataset['dislikes'])

    liste = list(zip(likesList,dislikesList))  #tuple a çevirme (1024,65)

    oranListesi = []

    for like,dislike in liste:
        if (like + dislike) == 0:
            oranListesi.append(0)
        else:
            oranListesi.append(like/(like+dislike))
    return oranListesi

df['like/dislike'] = likedislikeoranhesapla(df)
result = df.sort_values('like/dislike',ascending=False)[['title','likes','like/dislike']]

print(result)