
import discord
import os
import random
from bot.data import cards
from bot.card import Card
from bot.stay_alive import stay_alive

client = discord.Client()


@client.event
async def on_ready():
    print('Successfully logged in as {0.user}!'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello, I am EverydayTarot!'
                                   ' Type in $card to get a one-card reading or $ppf for a three-card, '
                                   'Past, Present and Future reading!')
    elif message.content.startswith('$card'):
        card = get_single_card()
        embed_var = embed(card.name, card.image, card.meaning)
        await message.channel.send(embed=embed_var)
    elif message.content.startswith('$ppf'):
        ppf_cards = ppf_reading()
        past = embed(ppf_cards[0].name + ' - Past', ppf_cards[0].image, ppf_cards[0].meaning)
        present = embed(ppf_cards[1].name + ' - Present', ppf_cards[1].image, ppf_cards[1].meaning)
        future = embed(ppf_cards[2].name + ' - Future', ppf_cards[2].image, ppf_cards[2].meaning)
        await message.channel.send(embed=past)
        await message.channel.send(embed=present)
        await message.channel.send(embed=future)


def embed(name, image, description):
    embed_var = discord.Embed(title=name, description=description)
    embed_var.set_image(url=image)
    return embed_var


def get_single_card():
    py_dict = random.choice(cards)
    reversed = random.randint(0,100) % 2
    if reversed:
      card = Card(py_dict["id"], py_dict["name"]+" - reversed", py_dict["image"], py_dict["reversed"])
    else:
      card = Card(py_dict["id"], py_dict["name"], py_dict["image"], py_dict["meaning"])
    return card


def ppf_reading():
    ppf_cards = []
    while len(ppf_cards) < 3:
        card = get_single_card()
        if card not in ppf_cards:
            ppf_cards.append(card)
    return ppf_cards

stay_alive()
client.run(os.environ['TOKEN'])