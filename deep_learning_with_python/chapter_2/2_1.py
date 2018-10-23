from keras.datasets import mnist

(train_images, train_lables), (test_images, test_labels) = mnist.load_data()

print(train_images.shape)

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

print(train_images.shape)
print(test_images.shape)
