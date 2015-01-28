#
# Define the blender rig API
# This is an abstract base class

class RigAPI:

	def getAPIVersion(self):
		return None

	def isAlive(self):
		return None

	# Emotion and Gesture commands ==========================
	def availableEmotionStates(self):
		return None

	def getEmotionStates(self):
		return None

	def setEmotionState(self, emotion):
		return None

	def availableGestures(self):
		return None

	# Gestures --------------------------------------
	def getGestures(self):
		return None

	def setGesture(self, name, repeat=1, speed=1, magnitude=0.5):
		return None

	def stopGesture(self, gestureID, smoothing):
		return None

	# Eye look-at targets ==========================
	# The coordinate system used is head-relative, in 'engineering'
	# coordinates: 'x' is forward, 'y' to the left, and 'z' up.
	# Distances are measured in meters.  Origin of the coordinate
	# system is somewhere (where?) in the middle of the head.
	def setFaceTarget(self, location):
		return None

	def setGazeTarget(self, location):
		return None

	def setVisemes(self, vis):
		return None

	# ========== info dump for ROS
	# Get Head rotation quaternion in XYZ format data structure.
	# Pitch: X (positive down, negative up)?
	# Yaw: Z (negative right to positive left)
	def getHeadData(self):

	# Get Eye rotation angles:
	# Pitch: down(negative) to up(positive)
	# Yaw: left (negative) to right(positive)
	def getEyesData(self):
		return None

	def getFaceData(self):
		return None
