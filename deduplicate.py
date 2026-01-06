def deduplicate(articles):
    seen = set()
    unique = []

    for article in articles:
        key = (article["title"], article["source"]["name"])
        if key not in seen:
            seen.add(key)
            unique.append(article)

    return unique
