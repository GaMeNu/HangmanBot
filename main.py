import discord
import discord.ext.commands as commands
import ext_Hangman

bot = commands.Bot(intents=discord.Intents.all(), command_prefix='!')
tree = bot.tree


@bot.event
async def on_ready():
    global bot
    if bot.get_cog("Hangman") is None:
        await ext_Hangman.setup(bot)


@bot.event
async def on_message(msg: discord.Message):
    global AUTHOR_ID, tree
    if msg.content == '/sync_cmds' and msg.author.id == AUTHOR_ID:
        await msg.reply('Syncing...', delete_after=3)
        await tree.sync()
        await msg.reply('Synced!', delete_after=3)
