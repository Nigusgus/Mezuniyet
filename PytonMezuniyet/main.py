import discord
from discord.ext import commands
import json
import random

# 1. BOT AYARLARI
intents = discord.Intents.default()
intents.message_content = True  # Mesajları okuyabilmesi için gerekli

bot = commands.Bot(command_prefix="!", intents=intents)

# 2. VERİLER VE MOTİVASYON SÖZLERİ
motivasyon_sozleri = [
    "🚀 'Kod yazmak şiir yazmak gibidir.' - Bugün harika işler çıkaracaksın!",
    "✨ Unutma: En iyi programcı, hata yapmaktan korkmayandır.",
    "📚 Ders çalışırken ara vermeyi unutma, beyninin de şarja ihtiyacı var! ☕",
    "💪 Zorlandığın anlar, aslında en çok geliştiğin anlardır.",
    "🌟 Bugünün küçük bir adımı, yarının büyük başarısı olacak!",
    "💻 Hata (bug) bulduğunda sevin, çünkü bir şeyi daha öğrendin!"
]

def programi_yukle():
    try:
        with open('config.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['ders_programi']
    except FileNotFoundError:
        return {"Hata": "config.json dosyası bulunamadı!"}

# 3. ETKİLEŞİMLİ BUTON VE ARAYÜZ SİSTEMİ
class ProgramView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None) # Butonun süresiz aktif kalması için

    @discord.ui.button(label="Ders Programını Gönder 📚", style=discord.ButtonStyle.blurple, custom_id="btn_program")
    async def program_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        program = programi_yukle()
        secilen_soz = random.choice(motivasyon_sozleri)
        
        # Öğrenciye özel şık panel (Embed)
        embed = discord.Embed(
            title="📅 Haftalık Ders Programı",
            description=f"> *{secilen_soz}*\n\nİşte bu haftaki derslerin listesi:",
            color=discord.Color.green()
        )
        
        for gun, ders in program.items():
            embed.add_field(name=gun, value=ders, inline=False)
            
        embed.set_footer(text="Okul Yönetimi Bilgi Sistemi | Başarılar Dileriz")
        
        # ephemeral=True: Sadece butona basan öğrenci görür
        await interaction.response.send_message(embed=embed, ephemeral=True)

# 4. BOT OLAYLARI (EVENTS)
@bot.event
async def on_ready():
    print(f'✅ Sistem Aktif! Bot İsmi: {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Öğrencilere yardım ediyor 🎓"))

# 5. ADMİN KOMUTLARI
@bot.command()
@commands.has_permissions(administrator=True) # Sadece adminler kullanabilir
async def kurulum(ctx):
    """Adminlerin ders programı butonunu kanala sabitlemesini sağlar."""
    embed = discord.Embed(
        title="🎓 Çevrimiçi Okul Bilgi Sistemi",
        description=(
            "Merhaba Öğrenciler!\n\n"
            "Ders saatlerinizi kaçırmamak için aşağıdaki butonu kullanabilirsiniz. "
            "Butona tıkladığınızda program size özel olarak gönderilecektir."
        ),
        color=discord.Color.gold()
    )
    view = ProgramView()
    await ctx.send(embed=embed, view=view)

@bot.command()
async def rehber(ctx):
    embed = discord.Embed(
        title="📖 Bot Kullanım Kılavuzu",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="🧑‍🎓 Öğrenciler İçin", 
        value="Kurulum yapılan kanaldaki butona tıklayarak ders programını alabilirsiniz. Mesaj size özel iletilir.", 
        inline=False
    )
    embed.add_field(
        name="👨‍🏫 Adminler İçin", 
        value="`!kurulum` yazarak ders programı butonunu aktif edebilirsiniz. \n`!temizle [sayı]` yazarak kanalı temizleyebilirsiniz.", 
        inline=False
    )
    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def temizle(ctx, miktar: int = 5):
    await ctx.channel.purge(limit=miktar)
    await ctx.send(f"✅ {miktar} mesaj temizlendi.", delete_after=3)

# Hata Yakalama (Yetkisi olmayan biri !kurulum yazarsa)
@kurulum.error
async def kurulum_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("❌ Bu komutu sadece okul adminleri kullanabilir!", delete_after=5)

# 6. BOTU ÇALIŞTIR
# Kopyaladığın Token'ı buraya yapıştır:
bot.run('')