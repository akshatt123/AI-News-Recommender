def get_recommendations(user_input, articles_df, model):
    user_embedding = model(user_input)[0]  # model is now a callable function
    article_embeddings = model(articles_df["content"].tolist())
    
    from sklearn.metrics.pairwise import cosine_similarity
    scores = cosine_similarity([user_embedding], article_embeddings)[0]
    top_indices = scores.argsort()[::-1][:5]
    
    return articles_df.iloc[top_indices]
