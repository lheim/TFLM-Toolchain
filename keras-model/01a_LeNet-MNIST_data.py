
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1).astype('float32')
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1).astype('float32')
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
x_train_normalized = x_train / 255
x_test_normalized = x_test / 255
# zero padding accross the 'images', 2,2 accross the x-axis, 2,2 accross the y-axis
x_train_normalized = np.pad(x_train_normalized, ((0,0),(2,2),(2,2),(0,0)), 'constant')
x_test_normalized = np.pad(x_test_normalized, ((0,0),(2,2),(2,2),(0,0)), 'constant')

INPUT_LENGTH = x_test_normalized[1].flatten().shape[0]
OUTPUT_LENGTH = y_test[1].flatten().shape[0]
print(f"The input length is {INPUT_LENGTH} and the output length {OUTPUT_LENGTH}")
