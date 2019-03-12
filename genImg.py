from PIL import Image, ImageDraw, ImageFont
import sys
from tokenizer import Tokenize


'''

::Hashtags for Posting Image::

#quotes #quotestoliveby #quotestagram #quotesoftheday #quotesdaily #quotesaboutlife
#quotestags #quotesgram #quotesofinstagram #quotesandsayings #quotesforlife #QuotesForYou
#quoteslife #quotesaboutlifequotesandsayings #quotesvn #quotesoflife #quoteslove #quotess
#quotesaboutlove #quotesofig #QuotesToInspire #quotesforhim #quotesforher #quotes4you
#quotestag #quoteslover #quotesbyme #quotespage #QuotesToRemember #quotesForDays

'''
            
def genImg(quote="Sample Quote", theme="l", imgNum="1"):

    '''
    Pass a quote and theme code to generate an image that is then saved in memory.
    '''
    quoteSegments = []
    wordCount = 1
    segment = ''

    for i in range(0, len(quote)):
        wordCount += 1
        segment += quote[i] + ' '
        if(wordCount % 3 == 0):
            quoteSegments.append(segment)
            segment = ''
        else:
            if (len(quote) - i - 1) < 3:
                for j in range(i, len(quote)):
                    try:
                        segment += quote[j+1] + ' '
                    except:
                        pass
                quoteSegments.append(segment)
                break
            else:
                continue 
    
    print(quoteSegments)



    # theme = ['text', 'bg']

    lightTheme = ['#2c3e50', '#ecf0f1']
    darkTheme = [(249, 202, 36), '#222222']

    if (theme == 'l'):
        imgTheme = lightTheme

    elif (theme == 'd'):
        imgTheme = darkTheme

    else:
        raise "Invalid Theme Parameters"

    ## Quote writing module
    font = ImageFont.truetype("suranna.ttf", 70)

    img = Image.new('RGB', (1600, 2000), color=imgTheme[1])

    draw = ImageDraw.Draw(img)

    for i in range(0, len(quoteSegments)):
        draw.text((400, 600 + i * 75), quoteSegments[i], imgTheme[0], font=font)
    

    font = ImageFont.truetype("barcode.ttf", 150)

    draw.text((400, 400), "ppurpy", imgTheme[0], font=font)

    img.save("pro_img/bg_pro_" + imgNum + ".jpg")

f =  open('quotes.txt', 'r', encoding='utf8')
i = 0
for line in f:
    tokens = Tokenize.tokenize(line)
    genImg(tokens, 'd', imgNum=str(i))
    i += 1

sys.exit()