# name: File path of the pgm image file
# Output is a 2D list of integers
import math
def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

# img is the 2D list of integers
# file is the output file path
def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)


def avg(image):
	height=len(image[0])
	width=len(image)

	x = [[0 for i in range(height)] for j in range(width)]
	for i in range(width):
		for j in range(height):
			if i==0 or j==0 or i==width-1 or j==height-1:
				x[i][j] = image[i][j]
			else:
				t = (image[i - 1][j - 1] + image[i - 1][j] + image[i - 1][j + 1] + image[i][j - 1] + image[i][j] + image[i][j + 1] + image[i + 1][j - 1] + image[i + 1][j] + image[i + 1][j + 1]) // 9
				x[i][j] = t

	return x



########## Function Calls ##########
x = readpgm('test.pgm') # test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')
y= avg(x)
writepgm(y,"average.pgm")
# x is the image to output and test_o.pgm is the image output in the same working directory
###################################




def edge(image):
	height = len(image[0])
	width = len(image)

	x = [[0 for i in range(height+2)] for j in range(width+2)]
	for i in range(1,width+1):
		for j in range(1,height+1):
			x[i][j]=image[i-1][j-1]

	y=[[0 for i in range(height)] for j in range(width)]
	for i in range(1,width+1):
		for j in range(1,height+1):
			hdif = (x[i - 1][j - 1] - x[i - 1][j + 1]) + 2 * (x[i][j - 1] - x[i][j + 1]) + (x[i + 1][j - 1] - x[i + 1][j + 1])
			vdif = (x[i - 1][j - 1] - x[i + 1][j - 1]) + 2 * (x[i - 1][j] - x[i + 1][j]) + (x[i - 1][j + 1] - x[i + 1][j + 1])
			grad = int(math.sqrt(hdif * hdif + vdif * vdif))
			y[i-1][j-1] = grad
	t = max(map(max, y))
	for i in range(width):
		for j in range(height):
			y[i][j] = int(y[i][j] * (255 / t))

	return y


########## Function Calls ##########
x = readpgm('test.pgm') # test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')
z=edge(x)
writepgm(z,"edge.pgm")
# x is the image to output and test_o.pgm is the image output in the same working directory
###################################

def minenergy(img):
	height = len(img[0])
	width = len(img)

	image=edge(img)
	x = [[0 for i in range(height)] for j in range(width)]
	for i in range(1, width):
		for j in range( height):
			if i==0:
				x[0][j]=image[0][j]
			else:
				if j==0:
					t = min([image[i - 1][j], image[i - 1][j + 1]])
				if j==height-1:
					t = min([image[i - 1][j - 1], image[i - 1][j]])
				else:
					t = min([image[i-1][j-1],image[i-1][j], image[i-1][j+1]])
				x[i][j]= image[i][j]+ t


	path=[[-1 for i in range(height)] for j in range(width)]
	mini=min(x[width-1])
	l=[]

	i=width-1
	for j in range(0,height):
		if x[i][j]==mini:
			path[i][j]=0
			l.append(j)

	i=width-2

	for j in (l):
		i=width-2
		while i>=0:
			if j == 0:
				t = min([x[i][j], x[i][j + 1]])
			if j == height - 1:
				t = min([x[i][j - 1], x[i][j]])
			else:
				t = min([x[i][j - 1], x[i][j], x[i][j + 1]])

			if t == x[i][j - 1]:
				path[i][j - 1] = 0
				j = j - 1
			if t == x[i][j]:
				path[i][j] = 0
				j = j
			else:
				path[i][j + 1] = 0
				j = j + 1
			i=i-1
	for i in range (width):
		for j in range(height):
			if path[i][j]==0:
				img[i][j]=255
	return img




########## Function Calls ##########
x = readpgm('test.pgm') # test.pgm is the image present in the same working directory
writepgm(x, 'test_o.pgm')
w=minenergy(x)
writepgm(w,"minenergy.pgm")
# x is the image to output and test_o.pgm is the image output in the same working directory
###################################













