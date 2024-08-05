import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    if message.content.startswith('/selam'):
        await message.channel.send(f'As Ben {client.user} Nasıl yardımcı olabilirim?')

    elif message.content.startswith('/iklim'):
        await message.channel.send(f'İKLİM DEĞİŞİKLİĞİ HAKKINDAKİ KODLAR: 1) /nedir  2) /ciddiliği  3) /nedenler  4) /önlemler')

    elif message.content.startswith('/nedir'):
        await message.channel.send(f' Ben MUNDO iklim değişikliği: nedeni ne olursa olsun iklimin ortalama durumunda ve değişkenliğinde onlarca yıl ya da daha uzun süre boyunca gerçekleşen değişiklikler')

    elif message.content.startswith('/ciddiliği'):
        await message.channel.send(f' Ben MUNDO Çevresel Etkiler: Doğal afetlerin artışı, ekosistemlerin bozulması ve deniz seviyelerinin yükselmesi gibi sonuçlar doğurur.Ekonomik Etkiler: Tarım, enerji ve su kaynakları üzerindeki olumsuz etkiler ekonomik kayıplara yol açar.Sağlık Riskleri: Sıcak hava dalgaları, hava kirliliği ve suyla bulaşan hastalıklar sağlık sorunlarına neden olabilir.Sosyal ve Politik Sorunlar: Göç, çatışma ve toplumsal gerilimler artabilir.Bu nedenlerle, iklim değişikliği hem bireyler hem de toplumlar için büyük bir endişe kaynağıdır ve herkes için önemli bir meseledir.')


    elif message.content.startswith("/nedenler") :
        await message.channel.send(f'Ben MUNDO Sera Gazları: Karbondioksit (CO2), metan (CH4) ve azot oksitler (N2O) gibi gazların atmosferde birikmesi.Ormansızlaşma: Ağaçların kesilmesi, karbon emilimini azaltır.Tarım: Metan ve azot oksit salınımı.Sanayi ve Enerji: Fosil yakıtların kullanımı.Ulaşım: Yakıtlı araçların emisyonları.Atık Yönetimi: Çöplerin çürümesiyle metan gazı oluşumu.Bu faktörler, küresel sıcaklıkların artmasına ve iklim değişikliğine neden olur.')

    elif message.content.startswith('/önlemler'):
        await message.channel.send(f' Ben MUNDO Sera Gazlarını Azaltın: Yenilenebilir enerji kaynaklarını kullanın ve enerji tasarrufu yapın.Ormanları Korumak: Ağaç dikme ve ormanları koruma projelerini destekleyin.Sürdürülebilir Tarım: Tarım yöntemlerini daha sürdürülebilir hale getirin.Ulaşımı Düzenleyin: Toplu taşıma, bisiklet ve elektrikli araçları tercih edin.Geri Dönüşüm: Atıkları azaltın ve geri dönüşüm yapın.Bu adımlar, iklim değişikliğinin etkilerini azaltmada önemli rol oynar.')

client.run("")