from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

width,height=red.size
red2=red.crop((100,0,width,height))
red3=red.crop((50,0,width-50,height))
red_monro_image = Image.blend(red2, red3, alpha= 0.5)

width,height=red.size
blue2=blue.crop((0,0,width-100,height))
blue3=blue.crop((50,0,width-50,height))
blue_monro_image = Image.blend(blue2, blue3, alpha= 0.5)

green_monro_image=green.crop((50,0,width-50,height))

monro_image2=Image.merge("RGB",(red,green,blue))
monro_image2.save("monro_image2.jpg")

image.thumbnail((80,80))
image.save("monro_avatar.jpg")
