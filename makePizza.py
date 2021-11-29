import random, datetime, os, io, logging
from random import shuffle
import time
from PIL import Image, ImageEnhance, ImageOps

loc = os.path.dirname(os.path.abspath(__file__))
isDiscord = False
extra = ["This pizza is then burnt to a crisp.",
"This pizza is then deepfried.",
"This pizza has been fitted with RGB lights.",
"This pizza has been flipped.",
"Best served in Australia",
"This pizza is suitable for the whole family.",
"This pizza is gluten free.",
"This recipe has been passed through generations.",
"Best served with one of BartenderBot's drinks.",
"Best served cold.",
"Best served hot.",
"Best served over ice.",
"Best before: {}.".format(datetime.date.fromordinal(random.randint(725000, 740000))),
"@{} has to eat this pizza.".format(chr(random.randint(65, 90))),
"What is this, a pizza for ants?"]
nothing = ['welcome to the void', "There's nothing for you.", 'Check out another pizza.']
andArr = ['and', 'finished off with', 'topped with', 'with some', 'with addition of']
pies = {}
def formatString(ingredients, halves, isDouble):
    s = ""
    x = 0
    adjectives = []
    adjectives_folder = [name for name in os.listdir('./adjectives')]
    for name in adjectives_folder:
        with open(os.path.join('./adjectives/' + name)) as f:
            adjectives.append(f.read() + ' ')
    adjLength = len(adjectives)
    for ingredient in ingredients:
        s1 = ''
        if isDouble[x]:
            s1 += 'double '
        if halves[x] != 'whole':
            s1 += halves[x] + ' '
        if random.random() > 0.9:
            s1 += adjectives[random.randint(0,adjLength - 1)]
        if x == 0:
            s1 = s1.capitalize()
        if s == '' and s1 == '' and ingredient[0] > 'Z' and x == 0:
            s1 += ingredient.capitalize()
        else:
            s1 += ingredient

        if x < len(ingredients) - 2:
            s1 += ', '
        elif x == len(ingredients) - 2:
            s1 += ' ' + random.choice(andArr) + ' '
        else:
            s1 += '.'

        s += s1
        x += 1
    return s

def makePizza(ing1="", ing2="", ing3="", ing4=""):

    return buildPizza(ing1, ing2, ing3, ing4)

def buildPizza(ing1="", ing2="", ing3="", ing4=""):
    ingredientsAmmout = 0
    customIngredients = 0
    custIngs = [ing1, ing2, ing3, ing4]
    for i, ing in enumerate(custIngs):
        valid = validateIngredient(ing)
        if valid == 1:
            ingredientsAmmout += 1
        else:
            custIngs.pop(i)
    folder = './ingredients'
    piefolder = './pies'
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    pie_folders = [name for name in os.listdir(piefolder) if os.path.isdir(os.path.join(piefolder, name))]
    ingredientsDict = {}
    for name in sub_folders:
        try:
            with open(os.path.join(folder + '/' + name, name + '.txt')) as f:
                ingredientContent = f.read()
        except:
            ingredientContent = name
        ingredientsDict[name] = ingredientContent

    if ingredientsAmmout == 0:
        ingredientsAmmout = random.randint(1, 5)
    else:
        customIngredients = 1
    ingredientsIds = list(ingredientsDict)
    for name in pie_folders:
        try:
            with open(os.path.join(piefolder + '/' + name, name + '.txt')) as f:
                pies[name] = f.read()
        except:
            print("")
    ingredients = []
    halves = []
    isDouble = []
    hasDifferentPie = False

    if random.random() > 0.85:
        pieList = list(pies)
        pie = random.choice(pieList)
        pizzaImage = Image.open(os.path.join(piefolder + '/' + pie, pie + '.png'))
        hasDifferentPie = True
    else:
        pizzaImage = Image.open(os.path.join(loc, 'pizza.png'))

    for i in range(ingredientsAmmout):
        if customIngredients == 0:
            if i == 0 and random.random() > 0.995 and not isDiscord:
                ingredientId = 'previous'
                ingredients.append('previous pizza, just a bit smaller')
                halves.append("whole")
                isDouble.append(False)
            else:
                shuffle(ingredientsIds)
                ingredientId = random.choice(ingredientsIds)
                ingredients.append(ingredientsDict[ingredientId])
                ingredientsDict.pop(ingredientId)
                ingredientsIds.pop(ingredientsIds.index(ingredientId))

                halvesValue = random.random()
                doubleValue = random.random()
                if halvesValue < 0.6:
                    halves.append("whole")
                elif halvesValue < 0.8:
                    halves.append("right")
                else:
                    halves.append("left")

                if doubleValue < 0.85:
                    isDouble.append(False)
                else:
                    isDouble.append(True)
        else:
            ingredientId = custIngs[i]
            ingredients.append(ingredientsDict[ingredientId])
            ingredientsDict.pop(ingredientId)
            ingredientsIds.pop(ingredientsIds.index(ingredientId))

            halvesValue = random.random()
            doubleValue = random.random()
            if halvesValue < 0.6:
                halves.append("whole")
            elif halvesValue < 0.8:
                halves.append("right")
            else:
                halves.append("left")

            if doubleValue < 0.85:
                isDouble.append(False)
            else:
                isDouble.append(True)

        pizzaImage = addIngredient(loc, pizzaImage, ingredientId, halves[i], isDouble[i])

    extraS = ""
    if random.random() > 0.85:
        randomChoice = random.randint(0, len(extra) - 1)
        if randomChoice == 0:
            print("")
            pizzaImage = burn(pizzaImage)
        elif randomChoice == 1:
            print("")
            pizzaImage = deepfry(pizzaImage)
        elif randomChoice == 2:
            print("")
            pizzaImage = fitRGBLights(pizzaImage, loc)
        elif randomChoice < 5:
            print("")
            pizzaImage = ImageOps.flip(pizzaImage)
        elif randomChoice == 14:
            print("")
            size = 100, 67
            pizzaImage.thumbnail(size, Image.ANTIALIAS)
        extraS = "\n" + extra[randomChoice]

    buffer = None
    if (not isDiscord):
        pizzaImage.save(os.path.join(loc, 'pizza2.png'))
    else:
        buffer = io.BytesIO()
        pizzaImage.save(buffer, 'png')

    finalString = formatString(ingredients, halves, isDouble) + extraS

    if (hasDifferentPie):
        finalString = finalString + ' The pie is now ' + pies[pie]

    return finalString, buffer

def addIngredient(loc, pizzaImage, ingredient, half, isDouble):
    if(ingredient != 'previous'):
        ingredientImg = Image.open(os.path.join(loc, 'ingredients', ingredient, str(ingredient + '_' + half + '.png')))
        pizzaImage = Image.alpha_composite(pizzaImage, ingredientImg)
        if (isDouble):
            ingredientImg = ingredientImg.rotate(random.randint(10, 15) * (1 if random.random() > 0.5 else -1))
            pizzaImage = Image.alpha_composite(pizzaImage, ingredientImg)
    else:
        ingredientImg = Image.open(os.path.join(loc, 'pizza2.png'))
        size = 1463, 954
        ingredientImg.thumbnail(size, Image.ANTIALIAS)
        toPaste = Image.new("RGBA", pizzaImage.size, (0, 0, 0, 0))
        toPaste.paste(ingredientImg, (85, 37), ingredientImg)
        pizzaImage = Image.alpha_composite(pizzaImage, toPaste)

    return pizzaImage

#TODO
def burn(pizzaImage):
    #r, g, b, a = pizzaImage.split()
    pizzaImage = ImageEnhance.Brightness(pizzaImage).enhance(0.1)
    pizzaImage = ImageEnhance.Contrast(pizzaImage).enhance(8)
    return pizzaImage

def deepfry(pizzaImage):
    r, g, b, a = pizzaImage.split()
    pizzaImage = Image.merge('RGB', (r, g, b))
    pizzaImage = ImageOps.posterize(pizzaImage, 2)
    pizzaImage = ImageEnhance.Brightness(pizzaImage).enhance(1.2)
    pizzaImage = ImageEnhance.Contrast(pizzaImage).enhance(2)
    pizzaImage = ImageEnhance.Color(pizzaImage).enhance(2)
    pizzaImage = ImageEnhance.Sharpness(pizzaImage).enhance(100)
    r, g, b = pizzaImage.split()
    pizzaImage = Image.merge('RGBA', (r, g, b, a))
    return pizzaImage

def fitRGBLights(pizzaImage, loc):
    rgbLights = Image.open(os.path.join(loc, 'rgb.png'))
    pizzaImage = Image.alpha_composite(rgbLights, pizzaImage)
    return pizzaImage

def validateIngredient(ingredient):
    ingredientsDict = {}
    folder = './ingredients'
    match = 0
    sub_folders = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    for name in sub_folders:
        try:
            with open(os.path.join(folder + '/' + name, name + '.txt')) as f:
                ingredientContent = f.read()
        except:
            ingredientContent = name
        ingredientsDict[name] = ingredientContent
        if name == ingredient:
            match = 1
    return match


    