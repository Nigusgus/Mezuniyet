# 🎓 Online Okul Etkileşimli Discord Botu

Bu proje, bir çevrimiçi okulun öğrencileri ve öğretmenleri arasındaki iletişimi kolaylaştırmak, ders programına erişimi hızlandırmak ve sunucu yönetimini daha eğlenceli hale getirmek için geliştirilmiş bir **Python** botudur.

## ✨ Özellikler

* **Etkileşimli Arayüz:** Karmaşık komutlar yerine butonlar ve menülerle kolay kullanım.
* **Anlık Ders Programı:** Tek tıkla güncel ders programına ulaşım.
* **Kullanıcı Dostu:** Öğrenciler için basit, net ve sezgisel mesaj tasarımları (Embeds).
* **Eğlence Faktörü:** Öğrencileri motive edecek interaktif dokunuşlar.

## 🛠️ Kullanılan Teknolojiler

* **Dil:** [Python 3.10+](https://www.python.org/)
* **Kütüphane:** [discord.py](https://discordpy.readthedocs.io/en/stable/)
* **Veri Yönetimi:** JSON / SQLite (Ders programı depolama için)

## 🚀 Kurulum Talimatları (Adminler İçin)

Botu kendi sunucunuza kurmak için aşağıdaki adımları takip edin:

1.  **Depoyu Klonlayın:**
    ```bash
    git clone [https://github.com/KULLANICI_ADIN/PROJE_ADIN.git](https://github.com/KULLANICI_ADIN/PROJE_ADIN.git)
    cd PROJE_ADIN
    ```

2.  **Gereksinimleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Discord Bot Token Alın:**
    * [Discord Developer Portal](https://discord.com/developers/applications) üzerinden bir uygulama oluşturun.
    * "Bot" sekmesinden tokenınızı kopyalayın.
    * `.env` dosyası oluşturup `TOKEN=senin_tokenin` şeklinde kaydedin.

4.  **Botu Çalıştırın:**
    ```bash
    python main.py
    ```

## 📖 Kullanım Kılavuzu

### 🧑‍🎓 Öğrenciler İçin
* Botun bulunduğu kanaldaki **"Ders Programını Gör 📚"** butonuna tıklamanız yeterlidir.
* Program size özel (ephemeral) olarak gönderilir, böylece kanal kalabalıklaşmaz.

### 👨‍🏫 Adminler İçin
* `!kurulum` komutunu kullanarak butonun yer alacağı ana mesajı oluşturabilirsiniz.
* Ders programı güncellemeleri için `config.json` dosyasını düzenleyebilirsiniz.

## 🎨 Önizleme
*(Buraya botun çalıştığına dair bir ekran görüntüsü eklemek harika olur!)*

---
*Bu proje KODLAND Python Kursu Mezuniyet Projesi kapsamında geliştirilmiştir.*
