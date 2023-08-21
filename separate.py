from PIL import Image

# test_image = "woman_shirt.png"

SEPARATE_INTO = 3

def determine_winner(lis):
	# approximate the most filled-out third by figuring out the pane with the most colored pixels
	# this will probably have to be replaced later down the line
	print("Determining winner...")
	new_list = []
	third_len = int(len(lis)/SEPARATE_INTO)
	print(f"Third len: {third_len}")
	for i in range(0,SEPARATE_INTO):
		total = 0
		for y in range(third_len*i,third_len*(i+1)):
			total += lis[y]
		new_list.append(total)
	for i in range(0,len(new_list)):
		winner = 0
		if (new_list[i] > winner):
			winner = i
	print(f"Winner: {winner}")
	return winner+1 #turns 0,1,2 into 1,2,3


def most_interesting_third(im):
	ims = {}
	print(f"Orig: {im}")
	# with Image.open(orig) as im:
	width = im.width
	height = im.height
	print(f"{height}x{width}")
	bs = im.tobytes()
	winner = determine_winner(bs)

	third_height = int(height/SEPARATE_INTO)
	cropped = im.crop((0,
		third_height*(winner-1),
		width,
		third_height*winner)) 
	#left,upper,right,lower 
	#cropped.show()
	return cropped
		

