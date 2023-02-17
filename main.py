# Подключение визуального модуля
from colorama import init
from colorama import Fore,Back,Style
init()
# Подключение модуля для бота DISCORD
import disnake
from disnake.ext import commands



# Устанавливаем префикс для бота "!", отключаем стартовую команду "help", обращаемся к модулю disnake
bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all())

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

# Kick с сервера
@bot.command()
@commands.has_permissions(kick_members=True,administrator=True)
async def kick(ctx, member:disnake.Member,*, reason="Нарушение правил сервера!"):
	await ctx.send(f"Высшие силы {ctx.author.mention} исключили пользователя {member.mention}", delete_after=300)
	await member.kick(reason=reason)
	await ctx.message.delete()

# Ban на сервере
@bot.command()
@commands.has_permissions(kick_members=True,administrator=True)
async def ban(ctx, member:disnake.Member,*, reason="Нарушение правил сервера!"):
	await ctx.send(f"Высшие силы {ctx.author.mention} исключили пользователя {member.mention}", delete_after=300)
	await member.ban(reason=reason)
	await ctx.message.delete()

# Запуск бота по токену
bot.run("Token")