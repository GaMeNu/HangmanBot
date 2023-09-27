import discord
import discord.ext.commands as commands


class Hangman(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @staticmethod
    def setup(bot: commands.Bot):
        hangman_cog = Hangman(bot)
        await bot.add_cog(hangman_cog)
        return hangman_cog

def setup(bot: commands.Bot):
    """
    Set up the Hangman cog
    :param bot: bot to add the cog to
    :return: the added cog
    """
    return Hangman.setup(bot)