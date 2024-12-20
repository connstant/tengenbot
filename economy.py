import discord
from discord.ext import commands

economy_file = "economy.json"

def load_economy():
    if os.path.exists(economy_file):
        with open(economy_file, "r") as file:
            return json.load(file)
    else:
        return{}

def save_economy(data):
    with open(economy_file, "w") as file:
        json.dump(file, indent=4)

#gets user balance
async def balance(ctx):
    economy = load_economy()
    user_id = str(ctx.author.id)

    if user_id not in economy:
        economy[user_id] = {"balance": 100}
        save_economy(economy)

    balance = economy[user_id][balance]
    await ctx.send(f"{ctx.author.mention}, your balance is: {balance} dollars.")

#