from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()
red.save("red_monro.jpg")
green.save("green_monro.jpg")
blue.save("blue_monro.jpg")

red=Image.open("red_monro.jpg")
width,height=red.size
red2=red.crop((100,0,width,height))
red2.save("red2.jpg")
red3=red.crop((50,0,width-50,height))
red3.save("red3.jpg")
red_monro_image = Image.blend(red2, red3, alpha= 0.5)
red_monro_image.save ("red_monro_image.jpg")

blue=Image.open("blue_monro.jpg")
width,height=red.size
blue2=blue.crop((0,0,width-100,height))
blue2.save("blue2.jpg")
blue3=blue.crop((50,0,width-50,height))
blue2.save("blue2.jpg")
blue_monro_image = Image.blend(blue2, blue3, alpha= 0.5)
blue_monro_image.save("blue_monro_image.jpg")

green=Image.open("green_monro.jpg")
green_monro_image=green.crop((50,0,width-50,height))
green_monro_image.save("green_monro_image.jpg")

red_r=Image.open("red_monro_image.jpg")
green_g=Image.open("green_monro_image.jpg")
blue_b=Image.open("blue_monro_image.jpg")

monro_image2=Image.merge("RGB",(red_r,green_g,blue_b))
monro_image2.save("monro_image2.jpg")

image_i=Image.open("monro_image2.jpg")
image_i.thumbnail((80,80))
image_i.save("monro_avatar.jpg")
