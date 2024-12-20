import random
import discord
import weather
from discord.ext import commands

# Bot setup
help_command = commands.DefaultHelpCommand(
    no_category='Commands'
)

description = "!help for more information"

bot = commands.Bot(command_prefix=commands.when_mentioned_or('!'), case_insensitive=True, intents=discord.Intents.all(),
                   help_command=help_command, description=description)


# bot online confirm message
@bot.event
async def on_ready():
    print("Bot Online!")

# Tengen mentioned?
@bot.event
async def on_message(message):
    #ignores messages the bot says
    if message.author == bot.user:
        return

    if message.content.lower() == 'tengen':
        random_int = random.randrange(1, 5)

        responses = {
            1: "Yes, you called?",
            2: "Well well well, look who it is.",
            3: "Fear not, I am here!",
            4: "I am online!"
        }

        await message.channel.send(responses[random_int])

    await bot.process_commands(message)

# responds hello with ping
@bot.command(name="hello", help="Responds Hello to the user.")
async def hello(user):
    await ctx.send(f"Hello there, {user.author.mention}!")

# random quotes
@bot.command(name="quote", help="Tengen will say a random quote of his.")
async def quote(ctx):
    random_int = random.randrange(1, 11)

    quotes = {
        1: "Who cares if you don't acknowledge me? You little bottom feeder! Did your brain explode or what?",
        2: "Starting now, things are going to get real flashy!",
        3: "First, worship And praise me! We'll discuss that other thing later!",
        4: "Well, Yeah. I'm a flashy, glamorous ladies-Man, so that's a no-brainer.",
        5: "I'm so on fire I could eat 100 bowls of tempura udon! In a flashy way, that is.",
        6: "Let's go home to a hero's welcome, and be flashy about it!",
        7: "You Slacker.",
        8: "Jeez, can't you even show me some bravado?",
        9: "We could be in for an ultra flashy fight to death!",
        10: "I've finished my musical score technique! We're going for the win!"
    }

    await ctx.send(quotes[random_int])

#ping people in voice chat
@bot.command(name="ping", help="Ping everyone that is in voice chat with the user calls the command.")
async def ping_server(ctx):
    voice_channel = ctx.author.voice.channel
    if not voice_channel:
        members = voice_channel.members

        mentions = [member.mention for member in members]

        await ctx.send(f"Pinging everyone in {voice_channel.name}: {', '.join(mentions)}")

    else:
        await ctx.send("You need to be in a voice channel to use this command.")

#roll dice
@bot.command(name="roll", help="Roll dice in the format NdM, e.g., 2d20 to roll 2 20-sided dice.")
async def roll(ctx, dice: str):
    try:
        #parse input
        rolls, sides = map(int, dice.lower().split('d'))
        if rolls <= 0 or sides <= 0:
            raise ValueError("Number of rolls and sides must be positive.")

        if rolls > 100 or sides > 1000:
            await ctx.send("Please keep the rolls or sides reasonable (e.g., max 100 rolls, 1000 sides).")
            return

        #roll dice
        results = []
        for i in range(rolls):
            results.append(random.randint(1,sides))
        total = sum(results)

        #display results
        await ctx.send(f"{ctx.author.mention} rolled {dice}: {results} (Total: {total})")

    #error handling
    except ValueError:
        await ctx.send(
            "Invalid format. Use NdM, where N is the number of dice and M is the number of sides (e.g., 2d20).")

#Economy stuff



#error handling stuff
@bot.event
async def on_command_error(ctx, error):
    # Check for missing arguments
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You're missing some required arguments! Use `!help` to check the correct usage.")

    # Command not found
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send("That command doesn't exist! Use `!help` to see all available commands.")

    # User lacks permissions
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("You don't have the required permissions to use this command.")

    # Bot lacks permissions
    elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send("I don't have the required permissions to perform that action.")

    # Too many arguments provided
    elif isinstance(error, commands.TooManyArguments):
        await ctx.send("You provided too many arguments! Check `!help` for the correct command format.")

    # Command is on cooldown
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown. Try again in {error.retry_after:.2f} seconds.")

    # General command error
    elif isinstance(error, commands.CommandInvokeError):
        await ctx.send("An error occurred while executing the command. Please try again.")
        # Optionally log the full error to the console for debugging
        print(f"CommandInvokeError: {error.original}")

    # Fallback for unhandled errors
    else:
        await ctx.send("Something went wrong. Please try again later.")
        # Optionally log the full error to the console
        print(f"Unhandled error: {error}")

with open("token.txt") as file:
    token = file.read()
bot.run(token)
