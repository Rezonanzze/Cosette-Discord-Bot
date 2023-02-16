import disnake
from disnake.ext import commands

# Устанавливаем префикс для бота, отключаем стартовую команду "help", обращаемся к библеотеке disnake
bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

# Оповещение о готовности бота
@bot.event
async def on_ready():
	print(f"Bot {bot.user} is ready to work!")

# Слеш команда для теста
@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
	await interaction.send("Комманда выполнена! RTMC")

# Встававить токен бота	
bot.run("Token")