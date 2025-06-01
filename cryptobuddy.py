BOT_NAME = "CryptoBuddy"
BOT_TONE = "Friendly and helpful"


crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

def get_recommendation(user_query):
    query = user_query.lower()
    if "sustainable" in query or "eco" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f"Invest in {recommend}! 🌱 It’s eco-friendly and has long-term potential!"
    elif "trending" in query or "rising" in query:
        trending = [k for k, v in crypto_db.items() if v["price_trend"] == "rising"]
        return f"{', '.join(trending)} are trending up! 🚀"
    elif "long-term" in query or "growth" in query:
        candidates = [k for k, v in crypto_db.items() if v["price_trend"] == "rising" and v["market_cap"] == "high"]
        if candidates:
            return f"{candidates[0]} is trending up and has a high market cap! 🚀"
        else:
            return "Cardano (ADA) is trending up and has a top-tier sustainability score! 🚀"
    else:
        return "Sorry, I can only answer about trending, sustainable, or long-term growth cryptos. Crypto is risky—always do your own research!"


def chat():
    print(f"{BOT_NAME}: Hey there! I’m your {BOT_TONE} crypto assistant.")
    print("Ask me about trending, sustainable, or long-term growth cryptos!")
    while True:
        user_query = input("You: ")
        if user_query.lower() in ["exit", "quit"]:
            print(f"{BOT_NAME}: Goodbye! Remember: Crypto is risky—always do your own research!")
            break
        response = get_recommendation(user_query)
        print(f"{BOT_NAME}: {response}")

if __name__ == "__main__":
    chat()