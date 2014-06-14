
class Shape(object):
	locX = 0
	locY = 0
	rgba = [0,0,0,1]
	radius  = 1

	def __init__(self, locX, locY,rgba,radius):
		self.locX = locX
		self.locY = locY
		self.rgba = rgba
		self.radius = radius

def fnGetShapes():
	shape = Shape(10,10,[0,0,0,1],1)

if __name__ == "__main__":
	fnGetShapes()