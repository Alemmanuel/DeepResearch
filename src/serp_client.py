import os
import requests
from typing import List, Dict

class SerpClient:

    def __init__(self):
        self.api_key = os.getenv("SERPAPI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ SERPAPI_API_KEY no está definida en .env")

        self.base = "https://serpapi.com/search"

    def search(self, query: str, num: int = 10) -> List[Dict]:
        params = {
            "q": query,
            "api_key": self.api_key,
            "num": num
        }

        resp = requests.get(self.base, params=params, timeout=20)
        resp.raise_for_status()

        data = resp.json()
        organic = data.get("organic_results", [])

        results = []
        for idx, item in enumerate(organic):
            results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet", ""),
                "link": item.get("link"),
                "source": item.get("displayed_link"),
                "rank": idx + 1
            })

        return results
