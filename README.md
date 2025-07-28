# 📊 WhatsApp Chat Analyzer

A powerful and interactive tool to analyze your WhatsApp chat history using **Python** and **Streamlit**. This project extracts insights like most active users, word usage, emojis, timelines, and much more — all visualized beautifully in an easy-to-use web interface.

---

## 🔍 Features

- 📈 **Top Statistics**: Total messages, words, media, links, and unique words.
- 👥 **Most Active Users**: See who chats the most in your group.
- ☁️ **Word Cloud**: Visualize common words in your chats.
- 💬 **Common Words**: Bar chart of the top 10 most used words.
- 😂 **Emoji Analysis**: Which emojis are used most? See it as a chart.
- 📆 **Monthly & Daily Timeline**: Track message activity over time.
- 🗺️ **Activity Maps**: Most active days and months for chatting.

---

## 🚀 How It Works

This tool uses:
- `chat_code.py` to preprocess your chat data
- `analyser.py` to compute stats and generate visuals
- `streamlit._app.py` to build a user interface with **Streamlit**

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/whatsapp-chat-analyzer.git
   cd whatsapp-chat-analyzer
   ```


2. **Run the app** // **make sure you have installed all the dependences file**
   ```bash
   streamlit run streamlit._app.py
   ```

---

## 📄 How To Use

1. Export your WhatsApp chat (without media).
2. Open the app in your browser.
3. Upload your `.txt` file from WhatsApp.
4. Select a user or view overall stats.
5. Explore your chat insights interactively!

---

## 🛠 Tech Stack

- Python 🐍
- Pandas
- Streamlit
- Matplotlib
- WordCloud
- Emoji
- URLExtract
