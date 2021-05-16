
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train_normalized = x_train / 255
x_test_normalized = x_test / 255
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

INPUT_LENGTH = x_test[1].flatten().shape[0]
OUTPUT_LENGTH = y_test[1].flatten().shape[0]
print(f"The input length is {INPUT_LENGTH} and the output length {OUTPUT_LENGTH}")
