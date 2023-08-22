from PIL import Image

<<<<<<< HEAD
TEST = True
=======
# test_image = "woman_shirt.png"

>>>>>>> d50a28cf3a9444f3f0f724b30ce4e93e614e4ad1
SEPARATE_INTO = 3

if TEST:
	test_image = "shirtpants2.png"


def determine_winner(lis):
	# approximate the most filled-out third by figuring out the pane with the most colored pixels
<<<<<<< HEAD

=======
	# this will probably have to be replaced later down the line
	print("Determining winner...")
>>>>>>> d50a28cf3a9444f3f0f724b30ce4e93e614e4ad1
	new_list = []
	third_len = int(len(lis)/SEPARATE_INTO)
	print(f"Third len: {third_len}")
	for i in range(0,SEPARATE_INTO):
		total = 0
		for y in range(third_len*i,third_len*(i+1)):
			if (lis[y][0] + lis[y][1] + lis[y][2]) > 30:
				total += 1
			
		new_list.append(total)
<<<<<<< HEAD
		print(f"total {i} now: {total}")
	print('lists:')
	print(new_list[0])
	print(new_list[1])
	print(new_list[2])

	winner = new_list.index(max(new_list))

	print(winner)

	return winner+1 #turns 0,1,2 into 1,2,3


if TEST:
	def most_interesting_third(orig):
		ims = {}
		if TEST:
			with Image.open(orig) as im:
				width = im.width
				height = im.height
				print(f"{height}x{width}")
				bs = list(im.getdata())
				# print("BS!")
				# print(bs)
				winner = determine_winner(bs)
				print(f"winner? {winner}")
				third_height = int(height/SEPARATE_INTO)
				cropped = im.crop((0,
					third_height*(winner-1),
					width,
					third_height*winner)) 
				#left,upper,right,lower 
				cropped.show()
				return cropped

else:
	def most_interesting_third(orig):
		print('hello world!')

		

if TEST:
	most_interesting_third(test_image)
=======
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
		

>>>>>>> d50a28cf3a9444f3f0f724b30ce4e93e614e4ad1
