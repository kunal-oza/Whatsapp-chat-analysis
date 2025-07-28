import chat_code,analyser
import streamlit as st
import matplotlib.pyplot as plt
st.sidebar.title("whatapp chat analysis")
uploaded_file=st.sidebar.file_uploader("choose a file")
if uploaded_file is not None:
    bytes_data=uploaded_file.getvalue()
    data=bytes_data.decode('utf-8')
    df=chat_code.preprocess(data)
    st.title('Top Statatics')
    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,'all')
    user=st.sidebar.selectbox("select user",user_list)
    if st.sidebar.button("show analysis"):
        total_message,total_words,num_unique_word,media_shared,link=analyser.analysis(user,df)
        col1, col2, col3, col4,col5 = st.columns(5)
        with col1:
            st.header('Total Message')
            st.title(total_message)
        with col2:
            st.header("Total Words")
            st.title(total_words)
        with col3:
            st.header("Unique Word")
            st.title(num_unique_word)
        with col4:
            st.header("Media Shared")
            st.title(media_shared)
        with col5:
            st.header("Link Shared")
            st.title(link)
        if user=='all':
            st.title('Most Active')
            x,df1=analyser.most_active(df)
            fig,ax=plt.subplots()
            col1,col2=st.columns(2)
            with col1:
                ax.bar(x.index,x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
            with col2:
                st.dataframe(df1)
        dp=analyser.word_clouds(user,df)
        fig,ax=plt.subplots()
        st.title('WORD CLOUD ')
        ax.imshow(dp)
        st.pyplot(fig)
        words=analyser.top_word_used(user,df)
        fig,ax=plt.subplots()
        ax.bar(words[0],words[1])
        plt.xticks(rotation='vertical')
        st.title('MOST COMMON WORD')
        st.pyplot(fig)
        st.dataframe(words)
        emo=analyser.emojii(user,df)
        st.title('EMOJII ANALYSIS')
        col1,col2=st.columns(2)
        with col1:
            st.dataframe(emo)
        with col2:
            fig,ax=plt.subplots()
            st.header('PIE CHART')
            ax.pie(emo[1],labels=emo[0],autopct='%0.2f')
            st.pyplot(fig)
        timeline=analyser.monthly_timeline(user,df)
        col1,col2=st.columns(2)
        with col1:
            st.header('MONTHLY TIMELINE')
            fig,ax=plt.subplots()
            ax.fill_between(timeline['time'],timeline['message'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header('DAILY TIMELINE')
            daily=analyser.daily_timeline(user,df)
            fig,ax=plt.subplots()
            ax.fill_between(daily['only_date'],daily['message'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        st.title('ACTIVIE MAPS')
        col1,col2=st.columns(2)
        with col1:
            st.header('Activity days')
            day=analyser.day(user,df)
            fig,ax=plt.subplots()
            ax.bar(day['day_name'],day['count'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        with col2:
            st.header('Month Activity')
            month=analyser.month(user,df)
            fig,ax=plt.subplots()
            ax.bar(month['month'],month['count'])
            plt.xticks(rotation='vertical')
            st.pyplot(fig)






        
                