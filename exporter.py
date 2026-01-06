import pandas as pd

def export_csv(articles, filename="news.csv"):
    df = pd.DataFrame([{
        "title": a["title"],
        "source": a["source"]["name"],
        "published": a["publishedAt"],
        "url": a["url"]
    } for a in articles])

    df.to_csv(filename, index=False)

def export_excel(articles, filename="news.xlsx"):
    df = pd.DataFrame([{
        "title": a["title"],
        "source": a["source"]["name"],
        "published": a["publishedAt"],
        "url": a["url"]
    } for a in articles])

    df.to_excel(filename, index=False)
