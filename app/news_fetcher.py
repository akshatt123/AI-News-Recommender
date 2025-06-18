import requests, os
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "https://newsdata.io/api/1/latest"

def fetch_articles(query, limit=10):
    params = {"apikey": NEWS_API_KEY, "q": query, "language": "en"}
    
    print(" Fetching:", BASE_URL, params)
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        print(" Status code:", resp.status_code)
        resp.raise_for_status()
        data = resp.json()
        print(" Response keys:", list(data.keys()))
    except Exception as e:
        print(" fetch error:", e, resp.text if 'resp' in locals() else "")
        return []
    
    results = data.get("results", [])
    print(f"🧾 Parsed {len(results)} results")
    articles = [
        {
            "title": itm.get("title", ""),
            "content": itm.get("description", "") or "",
            "url": itm.get("link", "") or "",
            "publishedAt": itm.get("pubDate", "") or ""
        }
        for itm in results[:limit]
    ]
    print(" Articles list created:", len(articles))
    return articles
