import csv
import os
from gtts import gTTS

# Danh sách từ mẫu
vocab_list = [
    {"word": "Annotation", "meaning": "Chú thích"},
    {"word": "Container", "meaning": "Bộ chứa"},
    {"word": "Deployment", "meaning": "Triển khai"},
    {"word": "Application", "meaning": "Ứng dụng"},
    {"word": "Platform", "meaning": "Nền tảng"},
    {"word": "Specification", "meaning": "Đặc tả"},
    {"word": "Enterprise", "meaning": "Doanh nghiệp"},
    {"word": "Community", "meaning": "Cộng đồng"},
    {"word": "Tutorial", "meaning": "Hướng dẫn"},
    {"word": "Server", "meaning": "Máy chủ"}
]

# Thư mục đầu ra
output_folder = "j2ee"
media_folder = os.path.join(output_folder, "media")
os.makedirs(media_folder, exist_ok=True)

# Hàm tạo file âm thanh
def generate_audio(word, save_path):
    tts = gTTS(text=word, lang="en")
    tts.save(save_path)

# Hàm lấy phiên âm đơn giản (tự điền ví dụ hoặc dùng API nếu có)
def get_ipa(word):
    fake_ipa_dict = {
        "Annotation": "/ˌæn.əˈteɪ.ʃən/",
        "Container": "/kənˈteɪ.nər/",
        "Deployment": "/dɪˈplɔɪ.mənt/",
        "Application": "/ˌæp.lɪˈkeɪ.ʃən/",
        "Platform": "/ˈplæt.fɔːm/",
        "Specification": "/ˌspes.ɪ.fɪˈkeɪ.ʃən/",
        "Enterprise": "/ˈen.tə.praɪz/",
        "Community": "/kəˈmjuː.nə.ti/",
        "Tutorial": "/tjuːˈtɔː.ri.əl/",
        "Server": "/ˈsɜː.vər/"
    }
    return fake_ipa_dict.get(word, "")

# Tạo file CSV cho Anki
csv_file = os.path.join(output_folder, "anki_vocab.csv")
with open(csv_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Word", "IPA", "Meaning", "Audio"])

    for item in vocab_list:
        word = item["word"]
        meaning = item["meaning"]
        ipa = get_ipa(word)
        audio_filename = f"{word}.mp3"
        audio_path = os.path.join(media_folder, audio_filename)

        # Tạo file âm thanh
        generate_audio(word, audio_path)

        # Viết vào file CSV
        audio_field = f"[sound:{audio_filename}]"
        writer.writerow([word, ipa, meaning, audio_field])

print(f"✅ Đã tạo file Anki tại: {csv_file}")
print(f"🎧 Âm thanh lưu trong: {media_folder}")
