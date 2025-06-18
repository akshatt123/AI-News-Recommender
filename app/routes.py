from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
from app.news_fetcher import fetch_articles
from app.nlp_utils import get_embedding_model
from app.recommender import get_recommendations

router = APIRouter()
embedding_fn = get_embedding_model()

class UserQuery(BaseModel):
    user_input: str

@router.post("/recommend")
def recommend_articles(query: UserQuery):
    try:
        print(" Query:", query.user_input)
        arts = fetch_articles(query.user_input)
        print(" Fetched articles:", arts)
        if not arts:
            return {"error": "No articles"}
        
        df = pd.DataFrame(arts)
        print(" Columns:", df.columns.tolist(), "Rows:", len(df))
        rec_df = get_recommendations(query.user_input, df, embedding_fn)
        print(" Recs returned:", rec_df.shape)
        return rec_df.to_dict(orient="records")
    except Exception as e:
        print(" ROUTES ERROR:", e)
        return {"error": str(e)}
