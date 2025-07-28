from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji
def analysis(user,df):
    # Get the user's data
    if user!='all':
        df=df[df['user']==user]
    total_message=df.shape[0]
    total_words=[]
    for i in df['message']:
        words=i.split()
        total_words.extend(words)
    num_unique_word=len(set(total_words))
    media_shared=df[df['message']=='<Media omitted>'].shape[0]
    link=[]
    extractor = URLExtract()
    for i in df['message']:
        link.extend(extractor.find_urls(i))
    return total_message,len(total_words),num_unique_word,media_shared,len(link)
def most_active(df):
    x=df['user'].value_counts()
    df=round((df['user'].value_counts()/df.shape[0])*100).reset_index().rename(columns={'user':'name','count':'percentage'})
    return x, df
def word_clouds(user,df):
    # Get the user's data
    if user!='all':
        df=df[df['user']==user]
    wc=WordCloud(width=500,height=400,background_color='white')
    dp=wc.generate(df['message'].str.cat(sep=' '))
    return dp
def top_word_used(user,df):
    word=[]
    if user!='all':
        df=df[df['user']==user]
    temp=df[df['user']!='group_notification']
    temp=temp[temp['message']!='<Media omitted>']
    for i in temp['message']:
        word.extend(i.split())
    return pd.DataFrame(Counter(word).most_common(10))
def emojii(user,df):
    if user!='all':
        df=df[df['user']==user]
    emojis=[]
    for i in df['message']:
        emojis.extend([c for c in i if c in emoji.EMOJI_DATA])
    return pd.DataFrame(Counter(emojis).most_common(6))
def monthly_timeline(user,df):
    if user!='all':
        df=df[df['user']==user]
    timeline=df.groupby(['year','month_num','month']).count()['message'].reset_index()
    time=[]
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i]+'-'+str(timeline['year'][i]))
    timeline['time']=time
    return timeline
def daily_timeline(user,df):
    if user!='all':
        df=df[df['user']==user]
    timeline=df.groupby('only_date').count()['message'].reset_index()
    return timeline
def day(user,df):
    if user!='all':
        df=df[df['user']==user]
    return df['day_name'].value_counts().reset_index()
def month(user,df):
    if user!='all':
        df=df[df['user']==user]
    return df['month'].value_counts().reset_index()

    


    
    

