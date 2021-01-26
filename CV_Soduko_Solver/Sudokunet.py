from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
#from keras.layers.normalization import BatchNormalization

class SudokuNet:
	@staticmethod
	def build(width, height, depth, classes):
		model = Sequential()
		inputShape = (height, width, depth)

		model.add(Conv2D(64, (3,3), padding='same', input_shape=inputShape))
		model.add(Activation('relu'))

		model.add(Conv2D(64, (3,3), padding='same'))
		model.add(Activation('relu'))

		model.add(MaxPooling2D(pool_size=(2,2)))
		#model.add(BatchNormalization())
		model.add(Conv2D(128, (3,3), padding='same'))
		model.add(Activation('relu'))

		model.add(MaxPooling2D(pool_size=(2,2)))

		model.add(Flatten())
		#model.add(BatchNormalization())
		model.add(Dense(512))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))

		model.add(Dense(64))
		model.add(Activation('relu'))
		model.add(Dropout(0.5))

		model.add(Dense(classes))
		model.add(Activation('softmax'))

		return model