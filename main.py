from PIL import Image

image = Image.open("monro.jpg")

red, green, blue = image.split()

red=Image.open("red_monro.jpg")
width,height=red.size
red2=red.crop((100,0,width,height))
red3=red.crop((50,0,width-50,height))
red_monro_image = Image.blend(red2, red3, alpha= 0.5)


blue=Image.open("blue_monro.jpg")
width,height=red.size
blue2=blue.crop((0,0,width-100,height))
blue3=blue.crop((50,0,width-50,height))
blue_monro_image = Image.blend(blue2, blue3, alpha= 0.5)

green=Image.open("green_monro.jpg")
green_monro_image=green.crop((50,0,width-50,height))

red_r=Image.open("red_monro_image.jpg")
green_g=Image.open("green_monro_image.jpg")
blue_b=Image.open("blue_monro_image.jpg")

monro_image2=Image.merge("RGB",(red_r,green_g,blue_b))

image_i=Image.open("monro_image2.jpg")
image_i.thumbnail((80,80))
image_i.save("monro_avatar.jpg")
