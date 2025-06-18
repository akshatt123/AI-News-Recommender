# 📰 AI News Recommender System

An intelligent, personalized news recommendation system powered by **Transformers**, **Deep Learning**, and **NLP**, built to deliver real-time, relevant articles based on user interests. The system uses **semantic similarity**, **LLMs**, and **vector search** to provide recommendations — all accessible via a **FastAPI backend** and a **Streamlit frontend**.

---

## 🚀 Features

- 🔎 User-topic-based news recommendations using semantic embeddings
- 🧠 Transformer-based models (BERT, GPT) for understanding article context
- 🔗 Real-time news fetching via NewsData.io API
- 🧬 Content-based vector similarity using FAISS
- 🖥️ Streamlit UI for seamless user interaction
- ☁️ Scalable deployment-ready (AWS Lambda, Docker, FastAPI)
- ✅ Unit-tested routes and modules for robustness

---

## 🗂️ Project Structure

```
AI-News-Recommender/
│
├── app/
│   ├── main.py                
│   ├── routes.py              
│   ├── db.py                  
│   ├── recommender.py         
│   ├── nlp_utils.py           
│   └── models/
│       ├── user_model.py      
│       └── article_model.py   
│
├── streamlit_app/
│   └── news_ui.py             
│
├── requirements.txt  
├── .gitignore        
└── README.md
             
```

---

##  Recommendation Workflow

1. **User Input**: User enters topics of interest via Streamlit.
2. **News Fetching**: Latest articles are fetched using the NewsData.io API (`/latest` endpoint).
3. **Embedding Generation**: Both user query and article content are embedded using a transformer model.
4. **Similarity Scoring**: Cosine similarity between user embedding and articles.
5. **Ranking & Display**: Top-N relevant articles shown on UI.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akshatt123/AI-News-Recommender.git
cd AI-News-Recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Backend

```bash
uvicorn app.main:app --reload
```

### 4. Run Streamlit Frontend

```bash
cd streamlit_app
streamlit run news_ui.py
```

---

## 🔑 Environment Variables

Create a `.env` file with the following:

```env
NEWSDATA_API_KEY=your_newsdata_api_key
```

---

## ✨ Future Improvements

- 🧠 Hybrid recommendations (content + collaborative)
- 📱 Mobile-friendly interface
- 📊 Analytics dashboard for user feedback
- 🧾 Multi-language news support

---

