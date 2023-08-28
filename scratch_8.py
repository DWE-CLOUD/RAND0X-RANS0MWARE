from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
img=Image.open('CC-12.png')
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('arial.ttf', 35)
myFont1 = ImageFont.truetype('arial.ttf', 40)
OTP1="RANXIDHFDOWJ88892992"
zs="0.000001001 BTC"
# text ko add kiya on image .. using myfont1 & 0
I1.text((270, 916), OTP1,font=myFont, fill=(255, 255, 255))
I1.text((1440, 305), zs,font=myFont1, fill=(255, 255, 255))
img.save("CC-12-1.png")