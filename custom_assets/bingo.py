import random
early = ["Reach 10 in any Skill",
"Reach level 5 in all Skills",
"24 Size Backpack"
"Skullkey",
"All Steel Equipment",
"10 Items to Museam",
"20 Itens to Museam",
"Upgrade House",
"Horse",
"Catch 10 different Fish",
"Catch 100 Fish",
"Eat a Stardrop",
"Obtain an ancient fruit",
"1+ Giant Crops",
"Collect 2000 Starpoints on the Fair",
"Win the Fishing Contest"
"First Place in the Fair Showcase",
"Dance with someone in the Flower Dance",
"Clean your Farm"
"Buy 5 different Hats",
"Tapping a Mushroom Tree",
"Own a Pig",
"Own 4 Chicken",
"Own 2 Ducks",
"Own 3 Goats",
"Ship 20 Wild Horseradish",
"Ship 20 Daffodil",
"Ship 20 Leeks",
"Ship 20 Dandelions",
"Ship 20 Spring Onions",
"Ship 20 Salmonberries",
"Ship 20 Spice Berries",
"Ship 20 Sweet peas",
"Ship 20 Fiddlehead Ferns",
"Ship 20 Wild Plums",
"Ship 20 Hazelnuts",
"Ship 20 Blackberries",
"Ship 20 Winter Roots",
"Ship 20 Crystal Fruits",
"Ship 20 Snow Yams",
"Ship 20 Crocus",
"Ship 20 Holly",
"Ship 20 Nautilus Shells",
"Ship 20 Coral",
"Ship 20 Sea Urchins",
"Ship 20 Clams",
"Ship 20 Mussels",
"Ship 20 Oysters",
"Ship 20 Red Mushrooms",
"Ship 20 Purple Mushrooms",
"Ship 20 Chanterelles",
"Ship 20 Common Mushrooms",
"Ship 20 Morels",
"Catch 5 Pufferfish",
"Catch 5 Sturgeon",
"Catch 5 Lingcod",
"Catch 5 Octopus",
"Catch 5 Scorpion Carp",
"Catch 10 Rainbow Trout",
"Catch 10 Catfish",
"Catch 10 Red Snapper",
"Catch 10 Red Mullet",
"Catch 10 Perch",
"Catch 15 Carp",
"Catch 15 Smallmouth Bass",
"Reach level 25 in mines",
"Reach level 50 in mines",
"Reach level 75 in mines",
"Reach level 100 in mines",
"Collect all 8 Rarecrows",
"Cook 10 different recipes",
"Craft 15 different items",
"Refill Energy in Spa",
"Mayor’s “Shorts”",
"Robin’s Axe",
"Linus Basket",
"Ship 25 Melon",
"Ship 25 Cauliflower",
"Ship 25 Pumpkin",
"Have 8 animals"]
late = [
    "Complete Community Center",
"Ship 300 of *Crop",
"Ship 300 of *Crop",
"Ship 300 of *Crop",
"Gold Axe",
"Gold Pickaxe",
"Gold Watercan",
"Gold Hoe",
"36 Size Backpack",
"30 Items to Museam",
"Catch a Legendary Fish",
"Upgrade House Twice",
"Understand the Dwarf",
"Galaxy Sword",
"Own every animal (Horse excluded)",
"Get Married"
]
post = [
    "Own all Fruit Trees",
"Ship 15 of Each Crop",
"Iridium Rod",
"Get all Stardrops",
"Get to Ginger Island",
"Get into the Wallnut room and Get Perfection."
]

random.shuffle(early)
random.shuffle(late)
random.shuffle(post)


final = []

for i in range(0,11):
    final.append(early[i])
for i in range(0,9):
    final.append(late[i])
for i in range(0,4):
    final.append(post[i])
random.shuffle(final)
print(final)