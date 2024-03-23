import discord
import random
import os
import requests

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #mobs
    if message.content.startswith('random_mob'): 
        mobs_images = [
            #passive mobs
            'https://minecraft.wiki/images/AllayFace.png?f466a',
            'https://minecraft.wiki/images/thumb/Lucy_Axolotl_JE2_BE1.png/480px-Lucy_Axolotl_JE2_BE1.png?90400',
            'https://minecraft.wiki/images/Bat_JE4_BE3.gif?db68c',
            'https://minecraft.wiki/images/thumb/Camel_JE1_BE2.png/480px-Camel_JE1_BE2.png?b76b7',
            'https://minecraft.wiki/images/thumb/Tuxedo_Cat_JE2_BE2.png/480px-Tuxedo_Cat_JE2_BE2.png?311fe',
            'https://minecraft.wiki/images/Chicken_JE2_BE2.png?30245',
            'https://minecraft.wiki/images/CodBody.png?3e0b1',
            'https://minecraft.wiki/images/thumb/Cow_JE5_BE2.png/480px-Cow_JE5_BE2.png?1068b',
            'https://minecraft.wiki/images/thumb/Donkey.png/480px-Donkey.png?9e2a1',
            'https://minecraft.wiki/images/FrogFace.png?2d191',
            'https://minecraft.wiki/images/Glow_Squid_JE1.gif?dcad8',
            'https://minecraft.wiki/images/thumb/White_Horse.png/480px-White_Horse.png?0cc9a',
            'https://minecraft.wiki/images/thumb/Red_Mooshroom_JE4.png/480px-Red_Mooshroom_JE4.png?ccd98',
            'https://minecraft.wiki/images/thumb/Mule.png/480px-Mule.png?3c1f0',
            'https://minecraft.wiki/images/thumb/Ocelot.png/480px-Ocelot.png?7d798',
            'https://minecraft.wiki/images/thumb/Red_Parrot.png/480px-Red_Parrot.png?90904',
            'https://minecraft.wiki/images/thumb/Pig_JE3_BE2.png/480px-Pig_JE3_BE2.png?a2e09',
            'https://minecraft.wiki/images/Pufferfish_small.gif?f12fb',
            'https://minecraft.wiki/images/PufferfishFace.png?aa40a',
            'https://minecraft.wiki/images/thumb/Brown_Rabbit_JE2_BE2.png/480px-Brown_Rabbit_JE2_BE2.png?bc661',
            'https://minecraft.wiki/images/SalmonBody.png?731bc',
            'https://minecraft.wiki/images/thumb/White_Sheep_JE3_BE6.png/480px-White_Sheep_JE3_BE6.png?6a7ae',
            'https://minecraft.wiki/images/thumb/Skeleton_Horse.png/480px-Skeleton_Horse.png?5e42a',
            'https://minecraft.wiki/images/Sniffer_sniffsniff.gif?36ccd',
            'https://minecraft.wiki/images/thumb/Sheared_Snow_Golem_JE2_BE2.png/150px-Sheared_Snow_Golem_JE2_BE2.png?3a1ea',
            'https://minecraft.wiki/images/thumb/Snow_Golem.png/480px-Snow_Golem.png?23125',
            'https://minecraft.wiki/images/Squid.gif?8a4c4',
            'https://minecraft.wiki/images/Strider_JE2_BE2.gif?f8244',
            'https://minecraft.wiki/images/thumb/Tadpole_swimming.gif/150px-Tadpole_swimming.gif?8087f',
            'https://minecraft.wiki/images/Clownfish.png?1b6b5',
            'https://minecraft.wiki/images/thumb/Turtle.png/480px-Turtle.png?373f9',
            'https://minecraft.wiki/images/thumb/Plains_Villager_Base_JE2.png/480px-Plains_Villager_Base_JE2.png?a2fcc',
            'https://minecraft.wiki/images/Wandering_Trader.png?62e9e',
            #mob neutrali
            'https://minecraft.wiki/images/BeeFace.png?7220c',
            'https://minecraft.wiki/images/thumb/Cave_Spider_JE2_BE2.png/480px-Cave_Spider_JE2_BE2.png?fd667',
            'https://minecraft.wiki/images/thumb/Dolphin.gif/215px-Dolphin.gif?3f0f5',
            'https://minecraft.wiki/images/Drowned.png?2454e',
            'https://minecraft.wiki/images/thumb/Enderman.png/480px-Enderman.png?b99b5',
            'https://minecraft.wiki/images/thumb/Fox.png/150px-Fox.png?ebd36',
            'https://minecraft.wiki/images/thumb/Snow_Fox.png/150px-Snow_Fox.png?97a92',
            'https://minecraft.wiki/images/thumb/Goat_JE1_BE1.png/480px-Goat_JE1_BE1.png?17d44',
            'https://minecraft.wiki/images/thumb/Iron_Golem_JE2_BE2.png/480px-Iron_Golem_JE2_BE2.png?2cd73',
            'https://minecraft.wiki/images/thumb/Creamy_Llama.png/150px-Creamy_Llama.png?45d8c',
            'https://minecraft.wiki/images/thumb/Brown_Trader_Llama.png/150px-Brown_Trader_Llama.png?b7db4',
            'https://minecraft.wiki/images/thumb/Panda_Rolling.gif/200px-Panda_Rolling.gif?c0013',
            'https://minecraft.wiki/images/thumb/Piglin.png/480px-Piglin.png?a498e',
            'https://minecraft.wiki/images/thumb/Polar_Bear.png/480px-Polar_Bear.png?29c45',
            'https://minecraft.wiki/images/thumb/Spider_JE4_BE3.png/480px-Spider_JE4_BE3.png?dcc35',
            'https://minecraft.wiki/images/thumb/Wolf_JE2_BE2.png/480px-Wolf_JE2_BE2.png?ee46e',
            'https://minecraft.wiki/images/thumb/Zombified_Piglin_BE6.png/480px-Zombified_Piglin_BE6.png?1a419',
            #Hostile mobs
            'https://minecraft.wiki/images/Blaze.gif?29f6f',
            'https://minecraft.wiki/images/Creeper_JE2_BE1.png?8fb28',
            'https://minecraft.wiki/images/thumb/Elder_Guardian.gif/260px-Elder_Guardian.gif?99f67',
            'https://minecraft.wiki/images/Endermite.gif?920c2',
            'https://minecraft.wiki/images/thumb/Evoker_Summoning_Vexes.png/480px-Evoker_Summoning_Vexes.png?15d33',
            'https://minecraft.wiki/images/Ghast_JE2_BE2.gif?b2699',
            'https://minecraft.wiki/images/thumb/Guardian.gif/150px-Guardian.gif?19e5a',
            'https://minecraft.wiki/images/thumb/Hoglin_JE3.png/480px-Hoglin_JE3.png?65eaa',
            'https://minecraft.wiki/images/Husk_JE2_BE2.png?a6767',
            'https://minecraft.wiki/images/thumb/Magma_Cube.png/480px-Magma_Cube.png?b4389',
            'https://minecraft.wiki/images/Phantom_JE2.gif?ed906',
            'https://minecraft.wiki/images/Piglin_Brute.png?5d4a0',
            'https://minecraft.wiki/images/thumb/Pillager_JE3.png/480px-Pillager_JE3.png?22662',
            'https://minecraft.wiki/images/thumb/Ravager_JE1.png/480px-Ravager_JE1.png?55aae',
            'https://minecraft.wiki/images/Shulker.png?02a87',
            'https://minecraft.wiki/images/thumb/Silverfish_JE1_BE1.gif/480px-Silverfish_JE1_BE1.gif?d40a7',
            'https://minecraft.wiki/images/thumb/Lefthandedskeleton.png/480px-Lefthandedskeleton.png?04422',
            'https://minecraft.wiki/images/thumb/Slime_JE3_BE2.png/480px-Slime_JE3_BE2.png?5b6a7',
            'https://minecraft.wiki/images/thumb/Stray_JE2_BE4.png/480px-Stray_JE2_BE4.png?ef82d',
            'https://minecraft.wiki/images/Vex_JE4.gif?da166',
            'https://minecraft.wiki/images/thumb/Vindicator_JE4.png/480px-Vindicator_JE4.png?d619d',
            'https://minecraft.wiki/images/Warden.gif?d0f99',
            'https://minecraft.wiki/images/thumb/Witch.png/480px-Witch.png?aeb30',
            'https://minecraft.wiki/images/thumb/Wither_Skeleton_JE4_BE3.png/480px-Wither_Skeleton_JE4_BE3.png?9c107',
            'https://minecraft.wiki/images/thumb/Zoglin.png/480px-Zoglin.png?6fd4b',
            'https://minecraft.wiki/images/thumb/Zombie_Targeting.png/480px-Zombie_Targeting.png?a66fd',
            'https://minecraft.wiki/images/thumb/Plains_Zombie_Villager_Base.png/480px-Plains_Zombie_Villager_Base.png?7882a',
            #Boss mobs
            'https://minecraft.wiki/images/Ender_Dragon.gif?fb9ba',
            'https://minecraft.wiki/images/thumb/Wither_JE2_BE2.png/150px-Wither_JE2_BE2.png?60b11',
            'https://minecraft.wiki/images/thumb/Blue_Wither.png/150px-Blue_Wither.png?3014f',
            #Unused mobs
            'https://minecraft.wiki/images/Zombie_JE3_BE2.png?20ae3',
            'https://minecraft.wiki/images/thumb/Zombie_Horse_Revision_3.png/480px-Zombie_Horse_Revision_3.png?72536',
            'https://minecraft.wiki/images/thumb/Killer_Bunny_JE5.png/230px-Killer_Bunny_JE5.png?c74c9',
            'https://minecraft.wiki/images/thumb/Illusioner_Casting.png/480px-Illusioner_Casting.png?2f926'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)

    elif message.content.startswith('random_passive_mob'):
        mobs_images = [
            #passive mobs
            'https://minecraft.wiki/images/AllayFace.png?f466a',
            'https://minecraft.wiki/images/thumb/Lucy_Axolotl_JE2_BE1.png/480px-Lucy_Axolotl_JE2_BE1.png?90400',
            'https://minecraft.wiki/images/Bat_JE4_BE3.gif?db68c',
            'https://minecraft.wiki/images/thumb/Camel_JE1_BE2.png/480px-Camel_JE1_BE2.png?b76b7',
            'https://minecraft.wiki/images/thumb/Tuxedo_Cat_JE2_BE2.png/480px-Tuxedo_Cat_JE2_BE2.png?311fe',
            'https://minecraft.wiki/images/Chicken_JE2_BE2.png?30245',
            'https://minecraft.wiki/images/CodBody.png?3e0b1',
            'https://minecraft.wiki/images/thumb/Cow_JE5_BE2.png/480px-Cow_JE5_BE2.png?1068b',
            'https://minecraft.wiki/images/thumb/Donkey.png/480px-Donkey.png?9e2a1',
            'https://minecraft.wiki/images/FrogFace.png?2d191',
            'https://minecraft.wiki/images/Glow_Squid_JE1.gif?dcad8',
            'https://minecraft.wiki/images/thumb/White_Horse.png/480px-White_Horse.png?0cc9a',
            'https://minecraft.wiki/images/thumb/Red_Mooshroom_JE4.png/480px-Red_Mooshroom_JE4.png?ccd98',
            'https://minecraft.wiki/images/thumb/Mule.png/480px-Mule.png?3c1f0',
            'https://minecraft.wiki/images/thumb/Ocelot.png/480px-Ocelot.png?7d798',
            'https://minecraft.wiki/images/thumb/Red_Parrot.png/480px-Red_Parrot.png?90904',
            'https://minecraft.wiki/images/thumb/Pig_JE3_BE2.png/480px-Pig_JE3_BE2.png?a2e09',
            'https://minecraft.wiki/images/Pufferfish_small.gif?f12fb',
            'https://minecraft.wiki/images/PufferfishFace.png?aa40a',
            'https://minecraft.wiki/images/thumb/Brown_Rabbit_JE2_BE2.png/480px-Brown_Rabbit_JE2_BE2.png?bc661',
            'https://minecraft.wiki/images/SalmonBody.png?731bc',
            'https://minecraft.wiki/images/thumb/White_Sheep_JE3_BE6.png/480px-White_Sheep_JE3_BE6.png?6a7ae',
            'https://minecraft.wiki/images/thumb/Skeleton_Horse.png/480px-Skeleton_Horse.png?5e42a',
            'https://minecraft.wiki/images/Sniffer_sniffsniff.gif?36ccd',
            'https://minecraft.wiki/images/thumb/Sheared_Snow_Golem_JE2_BE2.png/150px-Sheared_Snow_Golem_JE2_BE2.png?3a1ea',
            'https://minecraft.wiki/images/thumb/Snow_Golem.png/480px-Snow_Golem.png?23125',
            'https://minecraft.wiki/images/Squid.gif?8a4c4',
            'https://minecraft.wiki/images/Strider_JE2_BE2.gif?f8244',
            'https://minecraft.wiki/images/thumb/Tadpole_swimming.gif/150px-Tadpole_swimming.gif?8087f',
            'https://minecraft.wiki/images/Clownfish.png?1b6b5',
            'https://minecraft.wiki/images/thumb/Turtle.png/480px-Turtle.png?373f9',
            'https://minecraft.wiki/images/thumb/Plains_Villager_Base_JE2.png/480px-Plains_Villager_Base_JE2.png?a2fcc',
            'https://minecraft.wiki/images/Wandering_Trader.png?62e9e'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)
    
    elif message.content.startswith('random_neutral_mob'):
        mobs_images = [
            #neutral mob
            'https://minecraft.wiki/images/BeeFace.png?7220c',
            'https://minecraft.wiki/images/thumb/Cave_Spider_JE2_BE2.png/480px-Cave_Spider_JE2_BE2.png?fd667',
            'https://minecraft.wiki/images/thumb/Dolphin.gif/215px-Dolphin.gif?3f0f5',
            'https://minecraft.wiki/images/Drowned.png?2454e',
            'https://minecraft.wiki/images/thumb/Enderman.png/480px-Enderman.png?b99b5',
            'https://minecraft.wiki/images/thumb/Fox.png/150px-Fox.png?ebd36',
            'https://minecraft.wiki/images/thumb/Snow_Fox.png/150px-Snow_Fox.png?97a92',
            'https://minecraft.wiki/images/thumb/Goat_JE1_BE1.png/480px-Goat_JE1_BE1.png?17d44',
            'https://minecraft.wiki/images/thumb/Iron_Golem_JE2_BE2.png/480px-Iron_Golem_JE2_BE2.png?2cd73',
            'https://minecraft.wiki/images/thumb/Creamy_Llama.png/150px-Creamy_Llama.png?45d8c',
            'https://minecraft.wiki/images/thumb/Brown_Trader_Llama.png/150px-Brown_Trader_Llama.png?b7db4',
            'https://minecraft.wiki/images/thumb/Panda_Rolling.gif/200px-Panda_Rolling.gif?c0013',
            'https://minecraft.wiki/images/thumb/Piglin.png/480px-Piglin.png?a498e',
            'https://minecraft.wiki/images/thumb/Polar_Bear.png/480px-Polar_Bear.png?29c45',
            'https://minecraft.wiki/images/thumb/Spider_JE4_BE3.png/480px-Spider_JE4_BE3.png?dcc35',
            'https://minecraft.wiki/images/thumb/Wolf_JE2_BE2.png/480px-Wolf_JE2_BE2.png?ee46e',
            'https://minecraft.wiki/images/thumb/Zombified_Piglin_BE6.png/480px-Zombified_Piglin_BE6.png?1a419'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)

    elif message.content.startswith('random_hostile_mob'):
        mobs_images = [
            #hostile mobs
            'https://minecraft.wiki/images/Blaze.gif?29f6f',
            'https://minecraft.wiki/images/Creeper_JE2_BE1.png?8fb28',
            'https://minecraft.wiki/images/thumb/Elder_Guardian.gif/260px-Elder_Guardian.gif?99f67',
            'https://minecraft.wiki/images/Endermite.gif?920c2',
            'https://minecraft.wiki/images/thumb/Evoker_Summoning_Vexes.png/480px-Evoker_Summoning_Vexes.png?15d33',
            'https://minecraft.wiki/images/Ghast_JE2_BE2.gif?b2699',
            'https://minecraft.wiki/images/thumb/Guardian.gif/150px-Guardian.gif?19e5a',
            'https://minecraft.wiki/images/thumb/Hoglin_JE3.png/480px-Hoglin_JE3.png?65eaa',
            'https://minecraft.wiki/images/Husk_JE2_BE2.png?a6767',
            'https://minecraft.wiki/images/thumb/Magma_Cube.png/480px-Magma_Cube.png?b4389',
            'https://minecraft.wiki/images/Phantom_JE2.gif?ed906',
            'https://minecraft.wiki/images/Piglin_Brute.png?5d4a0',
            'https://minecraft.wiki/images/thumb/Pillager_JE3.png/480px-Pillager_JE3.png?22662',
            'https://minecraft.wiki/images/thumb/Ravager_JE1.png/480px-Ravager_JE1.png?55aae',
            'https://minecraft.wiki/images/Shulker.png?02a87',
            'https://minecraft.wiki/images/thumb/Silverfish_JE1_BE1.gif/480px-Silverfish_JE1_BE1.gif?d40a7',
            'https://minecraft.wiki/images/thumb/Lefthandedskeleton.png/480px-Lefthandedskeleton.png?04422',
            'https://minecraft.wiki/images/thumb/Slime_JE3_BE2.png/480px-Slime_JE3_BE2.png?5b6a7',
            'https://minecraft.wiki/images/thumb/Stray_JE2_BE4.png/480px-Stray_JE2_BE4.png?ef82d',
            'https://minecraft.wiki/images/Vex_JE4.gif?da166',
            'https://minecraft.wiki/images/thumb/Vindicator_JE4.png/480px-Vindicator_JE4.png?d619d',
            'https://minecraft.wiki/images/Warden.gif?d0f99',
            'https://minecraft.wiki/images/thumb/Witch.png/480px-Witch.png?aeb30',
            'https://minecraft.wiki/images/thumb/Wither_Skeleton_JE4_BE3.png/480px-Wither_Skeleton_JE4_BE3.png?9c107',
            'https://minecraft.wiki/images/thumb/Zoglin.png/480px-Zoglin.png?6fd4b',
            'https://minecraft.wiki/images/thumb/Zombie_Targeting.png/480px-Zombie_Targeting.png?a66fd',
            'https://minecraft.wiki/images/thumb/Plains_Zombie_Villager_Base.png/480px-Plains_Zombie_Villager_Base.png?7882a'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)

    elif message.content.startswith('random_boss_mob'):
        mobs_images = [
            'https://minecraft.wiki/images/Ender_Dragon.gif?fb9ba',
            'https://minecraft.wiki/images/thumb/Wither_JE2_BE2.png/150px-Wither_JE2_BE2.png?60b11',
            'https://minecraft.wiki/images/thumb/Blue_Wither.png/150px-Blue_Wither.png?3014f'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)

    elif message.content.startswith('random_unused_mob'):
        mobs_images = [
            'https://minecraft.wiki/images/Zombie_JE3_BE2.png?20ae3',
            'https://minecraft.wiki/images/thumb/Zombie_Horse_Revision_3.png/480px-Zombie_Horse_Revision_3.png?72536',
            'https://minecraft.wiki/images/thumb/Killer_Bunny_JE5.png/230px-Killer_Bunny_JE5.png?c74c9',
            'https://minecraft.wiki/images/thumb/Illusioner_Casting.png/480px-Illusioner_Casting.png?2f926'
        ]
        random_mob_image = random.choice(mobs_images)
        await message.channel.send(random_mob_image)

TOKEN = 'bot_token_here'

client.run(TOKEN)
