import json
import random as random
from discord.ext import commands
import requests

# ini class Basic
# nanti di help ada kategori "Basic"
class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # command ping
    @commands.command()
    async def ping(self, context):
        res = [
            "OK peko~",
            "Konpeko~",
            "ogey~"
        ]
        await context.send(random.choice(res) + " " + context.message.author.mention)

    # command kiss
    @commands.command()
    async def kiss(self, context):
        mentions = context.message.mentions
        msg = ""
        if not mentions:
            msg += context.message.author.mention + "... is kissing themselves?"
        else:
            msg += context.message.author.mention + " has kissed "
            for mention in mentions:
                msg += f" {mention.mention}"

        gif = await search_gifs('anime kiss')
        
        await context.send(content=msg+"\n"+gif)

    # command set chatbot channel
    @commands.command()
    async def chatbot(self, context):
        rcms = context.message.raw_channel_mentions
        msg = "";
        if not rcms:
            msg += context.message.author.mention + " no channel mentioned"
        else:
            msg += context.message.author.mention + " "
            for rcm in rcms:
                msg += f" {rcm.rcms}"

        await context.send(content=msg)


async def search_gifs(query):
    apikey = "3MYUQWVPOFEL"
    lmt = 50
    search_term = query

    gifs = []

    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top = json.loads(r.content)
        for res in top["results"]:
            gifs.append(res["url"])
        
        gif = random.choice(gifs)

        return gif
    else:
        top_8gifs = None



def setup(bot):
    bot.add_cog(Basic(bot))
