# score_df.py
# DataFrameから平均・最大・最小・国別比較などを抽出

def basic_stats(df):
    """列ごとの平均・最大・最小を計算"""
    return {
        "mean": df[["math", "reading", "science"]].mean(),
        "max": df[["math", "reading", "science"]].max(),
        "min": df[["math", "reading", "science"]].min(),
    }

def country_score(df, country_name):
    """特定の国のスコアを取得"""
    row = df[df["country"] == country_name]
    return row.to_dict(orient="records")[0] if not row.empty else None

