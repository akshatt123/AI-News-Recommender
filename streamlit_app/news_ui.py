import streamlit as st
import requests
import base64

image_path = "streamlit_app/img1.jpg"  

def get_base64_of_bin_file(bin_file_path):
    with open(bin_file_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(image_path):
    bin_str = get_base64_of_bin_file(image_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}
    
    .news-card {{
        background-color: rgba(0, 0, 0, 0.85);
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
        color: #f1f1f1;
        transition: 0.3s;
    }}
    .news-card:hover {{
        transform: scale(1.01);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.5);
    }}
    .article-title {{
        font-size: 1.4rem;
        font-weight: 700;
        color: #00acee;
    }}
    .article-meta {{
        font-size: 0.85rem;
        color: #ccc;
    }}
    .article-content {{
        font-size: 1.05rem;
        margin-top: 0.5rem;
        color: #ddd;
    }}
        h1, h2, h3 {{
            color: #aaaaaa !important;
        }}
        .stTextInput label{{
            color: #000000 !important;
        }}
        .stButton>button{{
            color: #dddddd !important;
        }}
        .stTextInput>div>input  {{
            color: #dddddd !important;
            background-color: rgba(0, 0, 0, 0.5);
        }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

st.set_page_config(page_title="📰 AI News Recommender", layout="wide")
set_background(image_path)

st.markdown("<h1 style='text-align: center;'>📰 AI News Recommender</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🔍 Get real-time, AI-curated news tailored to your interests</h3>", unsafe_allow_html=True)
st.markdown("---")

user_topic = st.text_input("Enter a topic or keyword", placeholder="e.g., AI, climate, sports, tech")

if st.button("🚀 Get News"):
    if user_topic.strip() == "":
        st.warning("⚠️ Please enter a topic.")
    else:
        with st.spinner("Fetching AI-curated articles..."):
            try:
                response = requests.post("http://localhost:8000/recommend", json={"user_input": user_topic})
                data = response.json()

                if isinstance(data, dict) and data.get("error"):
                    st.error("❌ " + data["error"])
                elif isinstance(data, list) and len(data) > 0:
                    st.success(f"✅ {len(data)} articles found for: **{user_topic}**")

                    for article in data:
                        st.markdown(
                            f"""
                            <div class="news-card">
                                <div class="article-title">{article['title']}</div>
                                <div class="article-meta">🕒 {article['publishedAt']}</div>
                                <div class="article-content">{article['content']}</div>
                                <a href="{article['url']}" target="_blank">🔗 <b>Read Full Article</b></a>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                else:
                    st.info("😕 No news found. Try another topic.")

            except Exception as e:
                st.error(f"Error: {e}")
