# kiwiManager.py
# Bot_token.env

#required import file
import os
from os.path import join, dirname
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio
import datetime
import time

#container variable
a = 0; #pointer


#Special Condition(shifting schedule array)
day = datetime.datetime.today().weekday()
if (day == 1 or day == 3):
    schedule = ["08:00:00","09:15:00","10:30:00","11:45:00","13:30:00"]
    print("case 2") #for debugging purposes
else: 
    schedule = ["08:00:00","09:15:00","10:30:00","11:45:00"]
    print("case 1") #for debugging purposes
    
# clocking function
async def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = (current_time.strftime("%H:%M:%S"))
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            for e in range(8):
                print("ping")
            break
           
            
async def actual_time(a):
    set_alarm_timer = schedule[a]
    await alarm(set_alarm_timer)


# package reference setting
dotenv_path = join(dirname(__file__), 'Bot_token.env') #change the string to match your own .env file
load_dotenv(dotenv_path)

TOKEN=os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
client = discord.Client()

#bots and command    
bot = commands.Bot(command_prefix='?')

@bot.command(name='start')
async def nine_nine(ctx):
    msg = "Absensi"
    for a in range(len(schedule)) :
        await ctx.send("starting...")
        await actual_time(a)
        for i in range(8):
            await ctx.send("@everyone");
            await asyncio.sleep(3)
       
    
bot.run(TOKEN) #donot remove this

