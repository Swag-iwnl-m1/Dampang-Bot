import discord
import requests
import asyncio
import random
import os
from discord.ext import commands, tasks
from discord import app_commands
import yt_dlp as youtube_dl

# ID server discord
GUILD_ID = 1166227158805516400 


intents = discord.Intents.default()
intents.message_content = True 
intents.messages = True 
intents.guilds = True
intents.members = True 

bot = commands.Bot(command_prefix="$", intents=intents)

Brainrot = [
      "Berlele", "Ariz ajalah", "Abyan caboel", "Ariz mabok", "Boni Hyper", 
    "Helmy miliarder", "Aryadikan", "Ketawa steak😂", "Lesley mcl", "Harith Binal",
    "Entitas fikes", "Geprek bu de", "Indomie dobel", "Gus Vigo", "Dark sistem",
    "Abyankan", "KluivertOut", "RAM 2GB", "SSD SATA" , "Ketec Keqing", "Geprek Jesen", 
    "Steak Ariz", "Warnet SuperNova", "Bakwan Teteh", "Yae Mikocok", "Mouse Johta", 
    "Johta Ninja 250cc", "Helmy F1", "Alip XSR", "Lele BKT", "Anomali Priok", "Kalkulus 3",
]

Brainrot_gambar = [
    "Brainrot_gambar/gambar1.jpeg",
    "Brainrot_gambar/gambar2.jpeg"
]

kata_kasar = [

    "anjing","bangsat","babi",
    "rajungan","memek","ngentot"
]

warnings = {} 


class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=None, intents=intents)
        self.loop_mode = False  
        self.current_song = None 

    async def setup_hook(self):
        guild = discord.Object(id=GUILD_ID)
        self.tree.copy_global_to(guild=guild)
        await self.tree.sync(guild=guild)
        print(f"✅ Slash commands synced in guild: {GUILD_ID}")

    async def on_ready(self):
        print(f'✅ Logged in as {self.user}')


    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.author == bot.user:
            return   
        
        if any(word in message.content.lower() for word in kata_kasar):
            await message.delete()  
            await message.channel.send(f"{message.author.mention}, Ketikan dijaga BLOK!")

        if message.content.startswith('$hello'):
            await message.channel.send(f'Halo {message.author.mention} apa kabar')

        if message.content.startswith('$baik'):
            await message.channel.send(f'Semoga {message.author.mention} selalu diberi kesehatan oleh Tuhan Yang Maha Kuasa')

        if message.content.startswith('$sombong lu byan'):
            await message.channel.send(f'Apalah')

        if message.content.startswith('$roblox'):
            await message.channel.send(f'Gas mabar')

        if message.content.startswith('$hero favorit'):
            await message.channel.send(f'Harith') 

        if message.content.startswith('$parah lu byan'):
            await message.channel.send(f'Apalah si {message.author.mention}')

        if message.content.startswith('$abyan'):
            await message.channel.send(f'Ingat {message.author.mention} awal bukanlah akhir')

        if message.content.startswith('$abyan'):
            await message.channel.send(f'Ingat {message.author.mention} awal bukanlah akhir')

        if message.content.startswith('$ariz'):
            await message.channel.send(f'Login emel @Everyone')

        if message.content.startswith('$aryadi'):
            await message.channel.send(f'{message.author.mention} Serlok tak parani')

        if message.content.startswith('$johta'):
            await message.channel.send(f'Cepatkan Tobat {message.author.mention}')

        if message.content.startswith('$helmy'):
            await message.channel.send(f'{message.author.mention} Gagal coba lagi {message.author.mention} Gagal coba lagi... @Everyone GAGALL COBA LAGI')

        if message.content.startswith('$jesen'):
            await message.channel.send(f'Gacha Apa Hari ini ? @Everyone')

        if message.content.startswith('$boni'):
            await message.channel.send(f'{message.author.mention} mau liat Lance atau Ling?')

        if message.content.startswith('$ferdi'):
            await message.channel.send(f'Tunggu menit 7 {message.author.mention} aku akan kembali')

        if message.content.startswith('$giparen'):
            await message.channel.send(f'Lu marah? {message.author.mention}')

        if message.content.startswith('$el'):
            await message.channel.send(f'Cukup jangan main genshin lagi @Everyone')

        if message.content.startswith('$sahur'):
            await message.channel.send(f'Tung Tung Tung Sahur @Everyone')

        if message.content.startswith('$wwz'):
            await message.channel.send(f'Ingfo Mabar @Everyone')

        if message.content.startswith('$valorant'):
            await message.channel.send(f'@Everyone Ingfo Perkopilorant')

        if message.content.startswith('$roblox'):
            await message.channel.send(f'ingfokan perobloxan @Everyone')

        if message.content.startswith('$last war'):
            await message.channel.send(f'Inilah gem terbaik, selamat {message.author.mention} anda telah mencapai titik tertinggi pergamingan duniawi terutama game Mobile. {message.author.mention} berbahagialah anda sudah termasuk 1% orang yang berkesempatan untuk memainkan game terbaik di dunia ini. Jangan lupa kalo di toiet main apa? @Everyone LAST WAR LAH !!!')

        if message.content.startswith('$validasi'):
            await message.channel.send(f'{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}{message.author.mention}') 

        if message.content.startswith('$meowtler'):
            await message.channel.send(f'DAS WAR EIN BEFEHL! DER ANGRIFF STEINER WAR EIN BEFEHL !!!') 
       
        if message.content.startswith('$meowtob'):
            await message.channel.send(f'Tob tobi tob tob tobi tob tob tobi tob tob tobaliy') 

        if message.content.startswith('$meowcina'):
            await message.channel.send(f'将大局逆转吧!')

        if message.content.startswith('$azril'):
            await message.channel.send(f"""
        Andriana:Aduh gantengnya😋 
        <@{1132523045588828161}>:najis bisa dipercepat gak🤨
        Andriana:Sabar yak <@{1132523045588828161}> aku lagi cari posisi yang nyaman nih buat cukur bulu bulu you😊
        <@{1132523045588828161}>:Om jagan om jangan om
        Andriana:Muuuuuach😘 
        <@{1132523045588828161}>:Bauk arang tekok kaunam😡
        Andriana:Kau ni anak mana sih <@{1132523045588828161}> kok lucu bener yah😊, mau ndak ngerasain rudal aku🥰
        <@{1132523045588828161}>:Tohapok kau wak, Jangan begitu lah bang nanti orang gak mau gunting sini lagi. kapok anak orang 
        digitukan bah
        <@{584349766520012800}>:Andre masih lama kah? 
        Andriana:Sebentar loh ya, ada customer ganteng nih
        <@{584349766520012800}>:Oh, ok ndre
        Andriana:Pukimak kau ye namaku bukan Andre tapi Andriana😡


                                         """)       

        if message.content.startswith('$mikel'):
            await message.channel.send(f'<@{485431664110075905}> Pakar jomok')

        if message.content.startswith('$imanuel'):
            await message.channel.send(f'<@{584349766520012800}> <@{584349766520012800}> <@{584349766520012800}> <@{584349766520012800}> <@{584349766520012800}> CUKUP IMANUEL!')        
                
    
                     

            
    async def on_reaction_add(self, reaction, user):
        if user != self.user:
            await reaction.message.channel.send('wkwkwkwk')


client = MyClient()

    
# FFMPEG Options
FFMPEG_OPTIONS = {
    'options': '-vn',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}

#Bagian setel musik
def search_youtube(query):
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0]
            return info['url']
        except Exception as e:
            print(f"Error: {e}")
            return None

@client.tree.command(name="join", description="Bot masuk ke voice channel")
async def join(interaction: discord.Interaction):
    if interaction.user.voice:
        channel = interaction.user.voice.channel
        if interaction.guild.voice_client is None:
            await channel.connect()
            await interaction.response.send_message(f"✅ Bergabung ke {channel}")
        else:
            await interaction.response.send_message("❌ Bot sudah ada di voice channel!")
    else:
        await interaction.response.send_message("❌ Kamu harus berada di voice channel dulu!")

@client.tree.command(name="play", description="Putar musik dari YouTube")
@app_commands.describe(query="Judul atau URL YouTube")
async def play(interaction: discord.Interaction, query: str):
    await interaction.response.defer()  # Mencegah interaksi kadaluarsa

    if interaction.guild.voice_client is None:
        await interaction.followup.send("❌ Bot belum join ke voice channel. Gunakan `/join` terlebih dahulu.")
        return

    url = search_youtube(query)
    if url is None:
        await interaction.followup.send("❌ Gagal mencari lagu!")
        return

    voice_client = interaction.guild.voice_client

    def after_playing(error):
        if error is None and client.loop_mode:
            ffmpeg_options = {
                'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                'options': '-vn'
            }
            voice_client.play(discord.FFmpegPCMAudio(client.current_song, **ffmpeg_options), after=after_playing)

    if not voice_client.is_playing():
        ffmpeg_options = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }
        client.current_song = url
        voice_client.play(discord.FFmpegPCMAudio(url, **ffmpeg_options), after=after_playing)
        await interaction.followup.send(f"🎶 Memutar: {query}")
    else:
        await interaction.followup.send("❌ Bot sedang memutar musik lain. Gunakan `/stop` terlebih dahulu.")


@client.tree.command(name="loop", description="Aktifkan/nonaktifkan mode loop")
async def loop(interaction: discord.Interaction):
    client.loop_mode = not client.loop_mode
    status = "AKTIF" if client.loop_mode else "NONAKTIF"
    await interaction.response.send_message(f"🔁 Mode loop: {status}")

@client.tree.command(name="stop", description="Hentikan musik yang sedang diputar")
async def stop(interaction: discord.Interaction):
    voice_client = interaction.guild.voice_client
    if voice_client and voice_client.is_playing():
        client.loop_mode = False
        voice_client.stop()
        await interaction.response.send_message("⏹ Musik dihentikan.")
    else:
        await interaction.response.send_message("❌ Tidak ada musik yang sedang diputar.")

@client.tree.command(name="leave", description="Bot keluar dari voice channel")
async def leave(interaction: discord.Interaction):
    if interaction.guild.voice_client:
        client.loop_mode = False
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("👋 Keluar dari voice channel.")
    else:
        await interaction.response.send_message("❌ Bot tidak ada di voice channel!")


# Slash Command (/)
@client.tree.command(name="hello", description="Say hello")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Halo bro")

@client.tree.command(name="mabar", description="Ajak mabar")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Ayo kita mabar bro")

@client.tree.command(name="ucup", description="sapa ucup")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("Ucup sigma")

@client.tree.command(name="imanuel", description="menghentikan imanuel")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("CUKUP IMANUEL")

@client.tree.command(name="kucai", description="anak kucai")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message("TOHAPOK KAU ANAK KUCAI")

@client.tree.command(name="help", description="Show all available commands")
async def help_command(interaction: discord.Interaction):
    help_text = (
         "**🎵 Music Commands:**\n"
        "`/join` - Join your voice channel\n"
        "`/play [query]` - Play music from YouTube\n"
        "`/pause` - Pause the current song\n"
        "`/resume` - Resume the paused song\n"
        "`/skip` - Skip to the next song\n"
        "`/queue` - Show the current queue\n"
        "`/loop` - Toggle loop mode\n"
        "`/stop` - Stop playing and clear queue\n"
        "`/clear` - Clear the queue\n"
        "`/leave` - Leave the voice channel\n\n"
        "**💬 Chat Commands:**\n"
        "`$hello` - Say hello\n"
        "`$baik` - Menyampaikan harapan baik\n"
        "`$sombong lu byan` - Respon untuk byan\n"
        "`$roblox` - Gas mabar\n"
        "`$hero favorit` - Jawab hero favorit\n"
        "`$parah lu byan` - Respon untuk byan\n"
        "`$abyan` - Motivasi tentang awal dan akhir\n"
        "`$ariz` - Login emel\n"
        "`$aryadi` - Serlok\n"
        "`$johta` - Cepatkan tobat\n"
        "`$helmy` - Gagal coba lagi\n"
        "`$jesen` - Gacha hari ini\n"
        "`$boni` - Lance atau Ling\n"
        "`$ferdi` - Menunggu menit 7\n"
        "`$giparen` - Lu marah?\n"
        "`$el` - Stop main genshin\n"
        "`$sahur` - Ingfo sahur\n"
        "`$wwz` - Ingfo mabar WWZ\n"
        "`$valorant` - Ingfo perkopilorant\n"
        "`$last war` - Pujian game terbaik\n"
        "`$validasi` - Spamming validasi\n"
        "`$meowtler` - Hitler reference\n"
        "`$meowtob` - Tobi tob\n"
        "`$meowcina` - Kalimat Cina\n"
        "`$mikel` - mikel???\n"
        "`$imanuel` - menghentikan aksi imanuel\n"
        "`$azril` - dialog tukang cukur\n"
    )
    await interaction.response.send_message(help_text)


@client.tree.command(name="brainrot", description="Kata-kata")
async def say_hello(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(Brainrot))


@client.tree.command(name="gambar_brainrot", description="gambar-gambar lucu")
async def brainrot_image(interaction: discord.Interaction):
    gambar_terpilih = random.choice(Brainrot_gambar)  

    if os.path.exists(gambar_terpilih): 
        file = discord.File(gambar_terpilih)  
        await interaction.response.send_message(file=file)
    else:
        await interaction.response.send_message("❌ Gambar tidak ditemukan.")


@client.tree.command(name="meme", description="meme random")
async def meme(interaction: discord.Interaction):
    try:
        response = requests.get("https://meme-api.com/gimme")
        data = response.json()

        if "url" in data:
            await interaction.response.send_message(data["url"])  
        else:
            await interaction.response.send_message("❌ Gagal mengambil meme.")

    except Exception as e:
        await interaction.response.send_message(f"❌ Terjadi kesalahan: {e}")        




# Tanda kalau bot sudah aktif
@client.event
async def on_ready():
    print(f'✅ Bot telah login sebagai {client.user}')


client.run('TOKEN')