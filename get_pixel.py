import cv2 # Import biblioteca OpenCV


'''
Basic method
img = cv2.imread('challenge_strider.png')
rows, columns, channels = img.shape
count = 0

for i in xrange(0,rows):
	for j in xrange(0, columns):
		if ((img[i,j][0] == 0) and (img[i,j][1] == 0) and (img[i,j][2] == 255)):
			print i,j
			count = count + 1
print "Total de Quadros Vermelho:", count
'''

class Challenge_Strider(object):
	"""docstring for Challenge_Strider"""
	def __init__(self):

		self._r = 255
		self._g = 0
		self._b = 0
		self._count = 0

	def load_image(self):
		self._image = cv2.imread('challenge_strider.png')


	def get_proprety_img(self):
		"""
		Returns all image properties 
			
		Returns:
			int: matrix size(rows,columns) and channels
		"""
		rows, columns, channels = self._image.shape
		return rows,columns,channels



	def red_pixel(self):
		"""
		Returns the total of red dots in the image

		Returns:
			int: the value of the counter
		
		Note:
			self._image is an array that contains the RGB values of each pixel.
			The position [0] corresponds to the value b (blue)
			The position [1] corresponds to the value g (gree)
			The position [2] corresponds to the value r (red)
			Every time finding the default 0 0 255 means that it found a red pixel
		"""		

		rows,columns,channels = self.get_proprety_img() 

		for i in xrange(0,rows):
			for j in xrange(0, columns):

				if ((self._image[i,j][0] == self._b) and (self._image[i,j][1] == self._g) and (self._image[i,j][2] == self._r)): # 
					self._count = self._count + 1
		
		return self._count	


def main():
	obj = Challenge_Strider()
	obj.load_image()
	total =  obj.red_pixel()

	print "Total de pontos vermelhos:", total


if __name__ == '__main__':
	main()