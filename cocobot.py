#!/usr/bin/python3

import discord
import json
from random import randint

client = discord.Client()
prefix = ';'
staff = list()

with open('staff.json', 'r') as f:
    staff = json.load(f)

with open('config.json', 'r') as f:
    config = json.load(f)

staff_state = False
bot_state = True
ovner_state = False

@client.event
async def on_ready():
    print(client.user)
    print(client.user.id)
    print('------READY-------')
@client.event
async def on_message(message):
    global staff
    global staff_state
    global ovner_state
    global bot_state

    if message.content:
        numb = randint(1,9)
        if message.content.startswith('{}cocobot'.format(prefix)) or message.content.startswith('{}kaori'.format(prefix)) and bot_state and not message.author.id == client.user.id:
            if numb == 1:
                msg = 'ERROR OPERATION COMPLETED VITH NO ERRORS'
            elif numb == 2:
                msg = 'ERROR OPERATION COMPLETED VITH NO ERRORS'
            elif numb == 3:
                msg = 'ERROR {} INITIALIZED VITH NO ERRORS'.format(client.user.name)
            elif numb == 4:
                msg = 'ERROR FUNTION EXECUTED CORRECTLY'
            elif numb == 5:
                msg = 'ERROR {} TURNED OFF SUCCESSFULLY'.format(client.user.name)
            elif numb == 6:
                msg = "ERROR {} CAN'T CHANGE IT'S NAME".format(client.user.name)
            elif numb == 7:
                msg = 'ERROR {} GOT BLOCKED'.format(client.user.name)
            elif numb == 8:
                msg = 'ERROR NO ERRORS VERE FOUND!!!'
            elif numb == 9:
                msg = 'ERROR {} IS NOT BROKEN'.format(client.user.name)
            embed = discord.Embed(title=client.user.name, type='bold', description=msg, color=0x0EA8F0)
            await client.send_message(message.channel, embed=embed)

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
    if message.author.id in config['ovner']:
        ovner_state = True
    for role in staff:
        role_ob = discord.utils.get(message.server.roles, id=role)
        if role_ob in message.author.roles:
            staff_state = True


client.run(config['token'])
