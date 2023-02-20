import disnake #Импорт модуля для бота
import os #Импорт модуля для ENV
import colorama #Визуальный модуль для консоли (необязателен)
from colorama import init
from colorama import Fore,Back,Style
init()
from disnake.ext import commands
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]

# Устанавливаем префикс для бота "/", отключаем стартовую команду "help", обращаемся к модулю disnake
bot = commands.Bot(command_prefix="/", help_command=None, intents=disnake.Intents.all(), test_guilds=[943813231808512000])

# Оповещение о готовности бота
@bot.event
async def on_ready():
	print(Fore.RED+Back.BLACK+ f"Бот {bot.user} Готов к работе!")

# Выдача роли при подключении участника через id роли
@bot.event
async def on_member_join(member):
	role = disnake.utils.get(member.guild.roles, id = 1032841402855465001)
	channel = member.guild.system_channel
	embed = disnake.Embed(
		title="Новый участник на сервере",
		description=f"{member.name}#{member.discriminator}",
		color=0xffffff
	)
	await member.add_roles(role)
	await channel.send(embed=embed)

#Эвент для ошибок
@bot.event
async def on_command_error(ctx,error):
	print(error)

	if isinstance(error,commands.MissingPermissions):
		await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды!")
	elif isinstance(error,commands.UserInputError):
		await ctx.send(embed=disnake.Embed(description=f"Правильное использование команды:'{ctx.prefix}{ctx.command.name}'({ctx.command.brief})\nНапример: {ctx.prefix}{ctx.command.usage}"))


#Текстовое сообщение about
@bot.slash_command(description="Я расскажу немного о себе.")
async def about(ctx:disnake.AppCmdInter):
	await ctx.send(f"Привет {ctx.author.mention}, меня зовут Козетта.\nМой разработчик неуч, поэтому я пока ничего не умею, подожди немного и я обязательно чему-нибудь научусь.")


# Kick с сервера
@bot.slash_command(description="Выгнать пользователя с сервера.")
@commands.has_permissions(kick_members=True,administrator=True)
async def kick(ctx, member:disnake.Member,*, reason="Нарушение правил сервера!"):
	await ctx.send(f"Высшие силы {ctx.author.mention} исключили пользователя {member.mention}", delete_after=30)
	await member.kick(reason=reason)

# Ban на сервере
@bot.slash_command(description="Забанить пользователя на сервере.")
@commands.has_permissions(ban_members=True,administrator=True)
async def ban(ctx, member:disnake.Member,*, reason="Нарушение правил сервера!"):
	await ctx.send(f"Высшие силы {ctx.author.mention} исключили пользователя {member.mention}", delete_after=30)
	await member.ban(reason=reason)


# Clear очистка чата (Базовое значение 10) (Ошибка с отложенным сообщением "Deferring")
@bot.slash_command(description="Удаляет определённой кол-во сообщений. По умолчанию: 10")
@commands.has_permissions(administrator=True)
async def clear(ctx, amount:int=10):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f"{ctx.author.mention} Удалил {amount} сообщений.", delete_after=15)

# Запуск бота по токену (не уверен, что правильно)
bot.run(BOT_TOKEN)