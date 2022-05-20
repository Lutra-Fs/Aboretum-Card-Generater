from PIL import Image, ImageDraw, ImageOps, ImageFont

cardState = ['CASSIA', 'MAPLE', 'CHERRY BLOSSOM',
             'JACARANDA', 'BLUE SPRUCE', 'DOGWOOD']
stateChar = {'CASSIA': 'a', 'MAPLE': 'm', 'CHERRY BLOSSOM': 'c',
             'JACARANDA': 'j', 'BLUE SPRUCE': 'b', 'DOGWOOD': 'd'}
stateColor = {'CASSIA': 'green', 'MAPLE': 'red', 'CHERRY BLOSSOM': 'pink',
              'JACARANDA': 'purple', 'BLUE SPRUCE': 'blue', 'DOGWOOD': 'grey'}
# fnt=ImageFont.truetype(
for card in cardState:
    for i in range(1, 9):
        img = Image.new('RGBA', (55, 69), color='white')
        cardNumberText = ImageDraw.Draw(img)
        (w, h) = cardNumberText.textsize(str(i))
        cardNumberText.text((20-w/2, 10), str(i), fill=stateColor.get(card),anchor='mm',align='center')
        # create a border around the card
        imageSpecies = Image.new('RGBA', (71, 10), color='white')
        cardNumberText.rectangle((0, 0, 55, 70), outline=stateColor.get(card))
        speciesText = ImageDraw.Draw(imageSpecies)
        (w, h) = speciesText.textsize(str(card))
        speciesText.text((0,0), str(card), fill='black',anchor='mm',align='center')
        rotated = imageSpecies.rotate(270,expand=1)
        font = ImageFont.truetype("LipaAgateHigh-Regular.OTF", 15)
        img.paste(rotated, (45,2))
        img.save(stateChar.get(card)+str(i)+'.png')