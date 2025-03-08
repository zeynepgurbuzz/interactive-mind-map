from mind_map import MindMap
from concept import Concept
from ai_explainer import AIExplainer
from learning_assistant import LearningAssistant

def main_menu():
    my_mind_map = MindMap("Zihin Haritam")
    assistant = LearningAssistant()
    explainer = AIExplainer()

    while True:
        print("\n📌 Zihin Haritası Yönetimi")
        print("1. Yeni kavram ekle")
        print("2. Mevcut kavramları listele")
        print("3. AI açıklaması al")
        print("4. Öğrenme sürecini takip et")
        print("5. Kavramları terminalde göster")
        print("6. Çıkış yap")
        choice = input("Seçiminiz: ")

        if choice == "1":
            title = input("Kavram Adı: ")
            description = input("Açıklama: ")
            importance = int(input("Önem Seviyesi (1-10): "))
            concept = Concept(title, description, importance)
            my_mind_map.add_concept(concept)
            print(f"✅ {title} eklendi!")

        elif choice == "2":
            my_mind_map.display_map()

        elif choice == "3":
            topic = input("Hangi kavramın açıklamasını almak istersin? ")
            info = explainer.get_info(topic)
            print("\n📖 AI Açıklaması:")
            print(info)

        elif choice == "4":
            concept = input("Hangi konuyu kontrol etmek istiyorsun? ")
            assistant.check_progress(concept)

        elif choice == "5":
            print("\n📌 Terminaldeki Kavramlar:")
            my_mind_map.display_map()

        elif choice == "6":
            print("Çıkış yapılıyor...")
            break

        else:
            print("❌ Geçersiz seçim, tekrar deneyin!")

if __name__ == "__main__":
    main_menu()
