# 🤖 GenerativeTaxBot

An AI-powered **Telegram chatbot** designed to answer tax-related queries using state-of-the-art Natural Language Processing. It leverages **HuggingFace's BART model**, **FAISS** for semantic similarity, and a web scraping pipeline to provide real-time, context-aware responses.

---

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-BART-orange?style=for-the-badge&logo=Huggingface&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram%20Bot-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![FAISS](https://img.shields.io/badge/FAISS-VectorSearch-blue?style=for-the-badge&logo=facebook&logoColor=white)
![WebScraping](https://img.shields.io/badge/WebScraping-BeautifulSoup-green?style=for-the-badge&logo=python)

---

## 📌 Overview

GenerativeTaxBot is built to:
- 🧠 Understand and respond to tax-related questions.
- 🔍 Use semantic search with FAISS over scraped content.
- 💬 Integrate seamlessly with Telegram for easy access.

---

## 🛠 Features

- ✅ BART-based generative model for smart responses
- ✅ Web scraping using BeautifulSoup
- ✅ Embedding generation using HuggingFace Transformers
- ✅ Semantic search with FAISS
- ✅ Telegram chatbot interface
- ✅ Scalable and extendable for other domains

---

## 📁 Folder Structure

```
GenerativeTaxBot/
│
├── main.py                 # Entry point: Telegram bot logic
├── create_faiss.py         # Builds the FAISS vector database
├── embeddings.py           # BART model + FAISS search logic
├── webscrape.py            # Scrapes tax data from URLs
├── embeddings.pt           # Saved vector embeddings
├── questions.txt           # Sample questions for testing
├── /doc/                   # Text data scraped from websites
├── /__pycache__/           # Compiled Python cache
└── README.md               # Project documentation
```

---

## 🧪 Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/nagasriramnani/GenerativeTaxBot.git
cd GenerativeTaxBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Scrape tax data

```bash
python webscrape.py
```

### 4. Generate FAISS vector index

```bash
python create_faiss.py
```

### 5. Add your Telegram Bot Token

Edit `main.py` and add your Telegram bot token:
```python
updater = Updater("YOUR_BOT_TOKEN", use_context=True)
```

### 6. Run the bot

```bash
python main.py
```

Now open Telegram and start chatting with your bot 🎉

---

## 💡 Example Queries

| User Query                      | Sample Response                                              |
|--------------------------------|--------------------------------------------------------------|
| What is TDS?                   | TDS stands for Tax Deducted at Source...                    |
| Do I need to file an ITR?      | You must file if income exceeds the exemption limit.        |
| What is the last date to file? | Usually, it is July 31 for individuals.                     |

---

## 🔍 Technologies Used

| Tool            | Purpose                              |
|-----------------|--------------------------------------|
| **Python 3.8+** | Programming Language                 |
| **BART Model**  | Natural Language Generation          |
| **FAISS**       | Semantic Similarity Search Engine    |
| **Telegram API**| Chatbot Frontend                     |
| **BeautifulSoup** | Web scraping HTML text data       |
| **HuggingFace** | Pretrained NLP Transformers          |

---

## 🎯 System Architecture

```
User (Telegram)
     |
     ↓
 Telegram Bot API
     |
     ↓
   main.py
     ↓
embeddings.py (calls FAISS + BART)
     ↓
create_faiss.py (builds index from scraped data)
     ↓
webscrape.py (HTML scraping using BeautifulSoup)
```
---

## 👨‍💻 Author

- **Naga Sri Ram Kochetti**
- 📧 Email: [nagasriramkochetti@gmail.com](mailto:nagasriramkochetti@gmail.com)
- 💼 [LinkedIn Profile](https://www.linkedin.com/in/nagasriramkochetti)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## ⭐️ Show Your Support

If you found this project helpful, please ⭐️ star the repo and share it!

---

## 🙌 Contributing

Pull requests are welcome. Please see [CONTRIBUTING.md](https://github.com/nagasriramnani/GenerativeTaxBot/blob/main/CONTRIBUTING.md) for more details.
