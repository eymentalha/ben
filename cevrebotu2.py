import discord
from discord.ext import commands
import random

# Botun Discord API'ye bağlanması için gerekli izinler
intents = discord.Intents.default()
intents.message_content = True  # Botun mesaj içeriğine erişimine izin veriyoruz.

# Botu başlatıyoruz
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')  # Botun başarılı bir şekilde bağlandığını belirten mesaj

# Çevre Dostu Sorular & Cevaplar (Quiz)
@bot.command()
async def cevre_sorusu(ctx):
    sorular = [
        ("Plastiklerin doğada ne kadar sürede çözüldüğünü biliyor musun?", ["Yüzyıllar", "Günler", "Saatler"], "Yüzyıllar"),
        ("Geri dönüşüm kutusuna hangi malzeme atılabilir?", ["Plastik", "Yemek Artığı", "Ayakkabı"], "Plastik"),
        ("Kompost yapmak için hangi malzeme kullanılır?", ["Kahve Telvesi", "Plastik", "Cam Şişe"], "Kahve Telvesi")
    ]
    soru, cevaplar, dogru_cevap = random.choice(sorular)
    random.shuffle(cevaplar)
    
    await ctx.send(f"Soru: {soru}\nCevap seçenekleri: {', '.join(cevaplar)}")
    
    def check(message):
        return message.author == ctx.author and message.content.lower() in [cevap.lower() for cevap in cevaplar]

    try:
        cevap = await bot.wait_for("message", check=check, timeout=30)
        if cevap.content.lower() == dogru_cevap.lower():
            await ctx.send("Tebrikler, doğru cevap!")
        else:
            await ctx.send(f"Yanlış cevap. Doğru cevap: {dogru_cevap}")
    except TimeoutError:
        await ctx.send("Zaman doldu! Cevap veremediniz.")


# Çevre dostu görevler
@bot.command()
async def cevre_gorevi(ctx):
    gorevler = [
        "Bugün 10 dakika boyunca dışarıda çöpleri topla! ♻️",
        "Evde plastik yerine kağıt kullanmaya çalış! 📜",
        "Kompost yapmak için eski yemekleri sakla! 🥕"
    ]
    gorev = random.choice(gorevler)
    await ctx.send(f"Bugünün çevre görevi: {gorev}")


# Atık azaltma görevleri
@bot.command()
async def atik_gorevi(ctx):
    görevler = [
        "Bugün plastik şişe yerine metal bir şişe kullanmaya karar ver!",
        "Evde geri dönüşüm kutusu oluştur ve tüm aileye bunu öğret!",
        "Dışarı çıkarken kendi alışveriş torbanı almayı unutma!"
    ]
    görev = random.choice(görevler)
    await ctx.send(f"Bugün bu görevi yapmayı unutma: {görev}")
    
bot.run("token")
