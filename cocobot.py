#!/usr/bin/python3

import discord
import json
from random import randint

client = discord.Client()
prefix = ';'
ovnerID = ['201741426038538242']
staff = list()

with open('staff.json', 'r') as f:
    staff = json.load(f)

staff_state = False
bot_state = True
ovner_state = False

@client.event
async def on_ready():
    print('ready')
@client.event
async def on_message(message):
    global staff
    global staff_state
    global ovnerID
    global ovner_state
    global bot_state
    
    if message.content:
        numb = randint(1,9)
        if message.content.startswith('{}cocobot'.format(prefix)) or message.content.startswith('{}kaori'.format(prefix)) and bot_state and not message.author.id == client.user.id:
            if numb == 1:
                msg = 'ERROR OPERATION COMPLETED VITH NO ERRORS'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
             #   await client.send_message(discord.Object(id='189199638450929664'), 'ERROR OPERATION COMPLETED VITH NO ERRORS')
            if numb == 2:
                msg = 'ERROR OPERATION COMPLETED VITH NO ERRORS'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
             #   await client.send_message(discord.Object(id='189199638450929664'), 'ERROR OPERATION COMPLETED VITH NO ERRORS')
            if numb == 3:
                msg = 'ERROR COCOBOT INITIALIZED VITH NO ERRORS'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
              #  await client.send_message(discord.Object(id='189199638450929664'), 'ERROR COCOBOT INITIALIZED VITH NO ERRORS')
            if numb == 4:
                msg = 'ERROR FUNTION EXECUTED CORRECTLY'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
             #   await client.send_message(discord.Object(id='189199638450929664'), 'ERROR FUNTION EXECUTED CORRECTLY')
            if numb == 5:
                msg = 'ERROR COCOBOT TURNED OFF SUCCESSFULLY'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
              #  await client.send_message(discord.Object(id='189199638450929664'), 'ERROR COCOBOT TURNED OFF SUCCESSFULLY')
            if numb == 6:
                msg = "ERROR COCOBOT CAN'T CHANGE IT'S NAME"
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
             #   await client.send_message(discord.Object(id='189199638450929664'), "ERROR COCOBOT CAN'T CHANGE IT'S NAME")
            if numb == 7:
                msg = 'ERROR COCOBOT GOT BLOCKED'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
               # await client.send_message(discord.Object(id='189199638450929664'), 'ERROR COCOBOT GOT BLOCKED')
            if numb == 8:
                msg = 'ERROR NO ERRORS VERE FOUND!!!'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
               # await client.send_message(discord.Object(id='189199638450929664'), 'ERROR NO ERRORS VERE FOUND!!!')
            if numb == 9:
                msg = 'ERROR COCOBOT IS NOT BROKEN'
                embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
                await client.send_message(message.channel, embed=embed)
                #await client.send_message(discord.Object(id='189199638450929664'), 'ERROR NO ERRORS VERE FOUND!!!')
            
            
              
        # Staff only commands
        if message.content.startswith('{}cocobot'.format(prefix)) and (staff_state or ovner_state):
            staff_state = False
            ovner_state = False
            if message.content.endswith('off') and bot_state:
                bot_state = False
                await client.send_message(message.channel, 'ERROR {} turned off successfully!!'.format(client.user.name))
            if message.content.endswith('on') and not bot_state:
                await client.send_message(message.channel, 'ERROR {} turned on successfully!!'.format(client.user.name))
                bot_state = True
        if message.content.startswith('{}addstaff'.format(prefix)) and ovner_state:
            ovner_state = False
            staff.append(message.role_mentions[0].id)
            with open('staff.json', 'w') as f:
                json.dump(staff, f)
            await client.send_message(message.channel, 'ERROR THE FUNCTION EXECUTED CORRECTLY')


            
    #Authorizes credentials by userID or by Role in a user
    if message.author.id in ovnerID:
        ovner_state = True                
    for role in staff:
        role_ob = discord.utils.get(message.server.roles, id=role)
        if role_ob in message.author.roles:
            staff_state = True
    
        
client.run('MjYzNzMxNjAwODYzMzk1ODUy.C0WSuQ.rs3w2AYR3Wy9xaQL-57NssnF6rs')  
