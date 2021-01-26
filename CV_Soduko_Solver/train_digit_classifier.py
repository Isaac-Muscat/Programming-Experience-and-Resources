from Sudokunet import SudokuNet
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.datasets import mnist
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import classification_report
import argparse

INIT_LR = 1e-3
EPOCHS = 10
BS = 64

print("accessing MNIST...")
((X_train, y_train), (X_test, y_test)) = mnist.load_data()

X_train = X_train.reshape((X_train.shape[0], 28, 28, 1))
X_test = X_test.reshape((X_test.shape[0], 28, 28, 1))

X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

le = LabelBinarizer()
y_train = le.fit_transform(y_train)
y_test = le.transform(y_test)

print('Compiling model...')
opt = Adam(lr=INIT_LR)
model = SudokuNet.build(width=28, height=28, depth=1, classes=10)
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

print('training network...')
history = model.fit(X_train, y_train,
	validation_data=(X_test, y_test),
	batch_size=BS,
	epochs=EPOCHS,
	verbose=1)

print('evaluating network...')
predictions = model.predict(X_test)
print(classification_report(
	y_test.argmax(axis=1),
	predictions.argmax(axis=1),
	target_names=[str(x) for x in le.classes_]))

print('serializing digit model...')
model.save('digit_classifier.h5', save_format='h5')