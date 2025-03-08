import json
import datetime

class LearningAssistant:
    def __init__(self, filename="learning_progress.json"):
        self.filename = filename
        self.progress = self.load_progress()

    def load_progress(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_progress(self):
        with open(self.filename, "w") as file:
            json.dump(self.progress, file, indent=4)

    def mark_learned(self, concept):
        today = datetime.date.today().isoformat()
        self.progress[concept] = today
        self.save_progress()
        print(f"✅ {concept} bugün öğrenildi olarak işaretlendi.")

    def check_progress(self, concept):
        today = datetime.date.today()
        last_learned = self.progress.get(concept)

        if last_learned:
            last_date = datetime.date.fromisoformat(last_learned)
            days_since = (today - last_date).days

            if days_since > 7:
                print(f"🔔 {concept} konusunu tekrar etme zamanı! {days_since} gün geçmiş.")
            else:
                print(f"📘 {concept} konusunu {days_since} gün önce öğrendin, tekrar etmeye gerek yok.")
        else:
            print(f"❌ {concept} daha önce öğrenilmemiş.")

    def show_all_progress(self):
        print("\n📌 Öğrenme Geçmişi:")
        for concept, date in self.progress.items():
            print(f"- {concept}: {date}")
