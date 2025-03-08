import requests

class AIExplainer:
    def __init__(self):
        self.wikipedia_api = "https://tr.wikipedia.org/api/rest_v1/page/summary/"

    def get_info(self, topic):
        url = self.wikipedia_api + topic.replace(" ", "_")
        
        try:
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("extract", "Bu konuda bilgi bulunamadı.")
            elif response.status_code == 404:
                return "⚠️ Wikipedia'da böyle bir başlık bulunamadı."
            else:
                return f"⚠️ API Hatası: {response.status_code} - Lütfen tekrar deneyin."

        except requests.exceptions.RequestException:
            return "⚠️ İnternet bağlantınızı kontrol edin veya API şu an çalışmıyor olabilir."

