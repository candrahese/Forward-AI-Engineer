import requests

class ProsaNLPIntegrator:
    def __init__(self, api_key):
        self.base_url = "https://api.prosa.ai/v1"
        self.headers = {"X-API-Key": api_key}

    def analyze_sentiment(self, text):
        payload = {"text": text}
        response = requests.post(f"{self.base_url}/sentiment", json=payload, headers=self.headers)
        return response.json()