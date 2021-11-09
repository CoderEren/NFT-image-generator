from PIL import Image
from IPython.display import display
import random
import json
import sys

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())

print("This is stage 1")
background = ["brown", "gold", "green", "lime", "orange", "pink", "red", "silver", "turquoise", "yellow"]
background_weights = [15, 5, 10, 10, 10, 10, 10, 10, 10, 10]

clothes = ["shirt", "shirt2", "suit", "sweatshirt", "tshirt2"]
clothes_weights = [30, 30, 10, 10, 20]

glasses = ["glasses", "no-glasses"]
glasses_weights = [50, 50]

hairstyles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
hairstyles_weights = [10, 10,10,10,10,10,10,10,10,10]

extras = ["beard1", "beard2", "beard3", "no-beard", "moustache1", "moustache2", "moustache3", "moustache4", "moustache5", "no-moustache"]
extras_weights = [10,10,10,10,10,10,10,10,10,10]

print("This is stage 2")

background_files = {
    "brown": "brown",
    "gold": "gold",
    "green": "green",
    "lime": "lime",
    "orange": "orange",
    "pink": "pink",
    "red": "red",
    "silver": "silver",
    "turquoise": "turquoise",
    "yellow": "yellow"
}

clothes_files = {
    "shirt": "shirt",
    "shirt2": "shirt2",
    "suit": "suit",
    "sweatshirt": "sweatshirt",
    "tshirt2": "tshirt2"
}

glasses_files = {
    "glasses": "glasses",
    "no-glasses": "no-glasses" 
}

hairstyles_files = {
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "10"
}

extras_files = {
    "beard1": "beard1",
    "beard2": "beard2",
    "beard3": "beard3",
    "no-beard": "no-beard",
    "moustache1": "moustache1",
    "moustache2": "moustache2",
    "moustache3": "moustache3",
    "moustache4": "moustache4",
    "moustache5": "moustache5",
    "no-moustache": "no-moustache"
}

print("This is stage 3")

TOTAL_IMAGES = 1000
all_images = [] 

def create_new_image():

    new_image = {} 

    # For each trait category, select a random trait based on the weightings 
    new_image["background"] = random.choices(background, background_weights)[0]
    new_image["clothes"] = random.choices(clothes, clothes_weights)[0]
    new_image["glasses"] = random.choices(glasses, glasses_weights)[0]
    new_image["hairstyles"] = random.choices(hairstyles, hairstyles_weights)[0]
    new_image["extras"] = random.choices(extras, extras_weights)[0]

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

print("This is stage 4")

# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)

print("This is stage 5")

#Check if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))

print("This is stage 6")

#Add token ID to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1

print(all_images)

print("This is stage 7")

#Get traits count
background_count = {}
for item in background:
    background_count[item] = 0

clothes_count = {}
for item in clothes:
    clothes_count[item] = 0

glasses_count = {}
for item in glasses:
    glasses_count[item] = 0

hairstyles_count = {}
for item in hairstyles:
    hairstyles_count[item] = 0

extras_count = {}
for item in extras:
    extras_count[item] = 0

for image in all_images:
    background_count[image["background"]] += 1
    clothes_count[image["clothes"]] += 1
    glasses_count[image["glasses"]] += 1
    hairstyles_count[image["hairstyles"]] += 1
    extras_count[image["extras"]] += 1

print(background_count)
print(clothes_count)
print(glasses_count)
print(hairstyles_count)
print(extras_count)

print("This is stage 8")

#Generate metadata for all traits
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=4)

print("This is stage 9")
#Generate images
for item in all_images:

    im1 = Image.open(f'./trait-layers/backgrounds/{background_files[item["background"]]}.jpg').convert('RGBA')
    im2 = Image.open(f'./trait-layers/clothes/{clothes_files[item["clothes"]]}.png').convert('RGBA')
    im3 = Image.open(f'./trait-layers/glasses/{glasses_files[item["glasses"]]}.png').convert('RGBA')
    im4 = Image.open(f'./trait-layers/hairstyles/{hairstyles_files[item["hairstyles"]]}.png').convert('RGBA')
    im5 = Image.open(f'./trait-layers/extras/{extras_files[item["extras"]]}.png').convert('RGBA')

    #Create each composite
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3)
    com3 = Image.alpha_composite(com2, im4)
    com4 = Image.alpha_composite(com3, im5)

    #Convert to RGB
    rgb_im = com4.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./images/" + file_name)

print("This is stage 10")
#Generate metadata for each image
f = open('./metadata/all-traits.json',) 
data = json.load(f)

IMAGES_BASE_URI = ""
PROJECT_NAME = "Weird Avatars"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("background", i["background"]))
    token["attributes"].append(getAttribute("clothes", i["clothes"]))
    token["attributes"].append(getAttribute("glasses", i["glasses"]))
    token["attributes"].append(getAttribute("hairstyles", i["hairstyles"]))
    token["attributes"].append(getAttribute("extras", i["extras"]))

    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=4)
f.close()
