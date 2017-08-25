import argparse
from PIL import Image 

def black_and_white(image):
	width, height = image.size
	for x in range(width):
		for y in range(height): 
			temp_r, temp_g, temp_b = image.getpixel((x,y))

			gray = (temp_r + temp_g + temp_b) / 3
			red, green, blue = gray, gray, gray
			sepia_tone = (int(red),int(green),int(blue))
			image.putpixel((x,y), sepia_tone)
	return image	


def sepia(image):
	width, height = image.size
	for x in range(width):
		for y in range(height): 
			temp_r, temp_g, temp_b = image.getpixel((x,y))
			red = (temp_r * .393) + (temp_g * .769) + (temp_b * .189)
			green = (temp_r * .349) + (temp_g * .686) + (temp_b * .168)
			blue = (temp_r * .272) + (temp_g * .534) + (temp_b * .131)
			sepia_tone = (int(red),int(green),int(blue))
			image.putpixel((x,y), sepia_tone)
	return image

def main(*, name,mode,images,save,display):
	print(name,mode,images,save,display)	
	for i, image in enumerate(images):
		try:
			temp_image = Image.open(image)
		except IOError:
			print("{} is not a valid image file.".format(image))

		if mode is None:
			pass
		elif mode == 'sepia':
			temp_image = sepia(temp_image)
		elif mode == 'graytone':
			temp_image = black_and_white(temp_image)

		if save:
			try:
				temp_image.save(name[i] + '.png', 'png')
			except:
				temp_image.save("output" + str(i+1) + '.png')

		if display:
			temp_image.show()

# def main(*args, **kwargs):
# 	for i, image_name in enumerate(kwargs['images']):
# 		try:
# 			temp_image = Image.open(image_name)
# 		except IOError:
# 			print(image_name, " is not a valid image file.")

# 		if kwargs['mode'] is None:
# 			pass
# 		elif kwargs['mode'] == 'sepia':
# 			temp_image = sepia(temp_image)
# 		elif kwargs['mode'] == 'graytone':
# 			temp_image = black_and_white(temp_image)
# 		if kwargs['save']:
# 			try:
# 				temp_image.save(kwargs['name'][i] + '.png' ,'png')
# 			except:
# 				temp_image.save("output" + str(i+1) + '.png')	
# 		if kwargs['display']:
# 			temp_image.show()

# 		temp_image.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Basic Image Manipulation')
	parser.add_argument('images', nargs='*', help='Must take in an image', type=str)
	parser.add_argument('--mode', nargs='?', help='Applies a mode to the image.', choices=['sepia', 'graytone'], type=str)
	parser.add_argument('--save', action='store_true', help='Save image passed in with --name value. Default: output[N].png')
	parser.add_argument('--display', action='store_true', help='Opens a window to display the image.')
	parser.add_argument('--name', nargs='*', type=str, metavar=('output.png', 'outpust2.png'))
	main(**vars(parser.parse_args()))


