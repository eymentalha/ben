import discord
from discord.ext import commands

# Botun Discord API'ye bağlanması için gerekli izinler
intents = discord.Intents.default()
intents.message_content = True  # Botun mesaj içeriğine erişimine izin veriyoruz.

# Botu başlatıyoruz
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık!')  # Botun başarılı bir şekilde bağlandığını belirten mesaj

# Çevre dostu tavsiyeler veren komut
@bot.command()
async def çevre_tavsiyesi(ctx):
    tavsiyeler = [
        "Plastik yerine cam şişeler kullanarak atık üretimini azaltabilirsiniz.",
        "Evde geri dönüşüm kutuları oluşturun ve her malzemeyi doğru kutuya yerleştirin.",
        "Tek kullanımlık plastiklerden kaçınarak sürdürülebilir alışveriş torbaları kullanın.",
        "Gıda atıklarını kompost yaparak doğaya katkı sağlayabilirsiniz.",
        "Elektronik cihazları kapalı tutarak enerji tasarrufu sağlayın."
    ]
    await ctx.send("Bugünün çevre dostu tavsiyeleri:\n" + "\n".join(tavsiyeler))

# Geri dönüşüm önerisi
@bot.command()
async def geri_donusum(ctx):
    await ctx.send("Geri dönüştürülebilir malzemeler: Cam, kağıt, plastik ve metal. Unutmayın, geri dönüşüm gezegenimize fayda sağlar!")

# Atık azaltma komutu
@bot.command()
async def atik_azaltma(ctx):
    await ctx.send("Atık azaltmanın yolları: \n1. Tek kullanımlık plastiklerden kaçının. \n2. Yeniden kullanılabilir su şişeleri kullanın. \n3. Organik atıkları kompost yaparak değerlendirin.")


bot.run("token")
