
(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train_normalized = np.random.rand(60000, 24, 24, 1)
x_test = x_test_normalized = np.random.rand(10000, 24, 24, 1)


(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)
INPUT_LENGTH = x_test_normalized[1].flatten().shape[0]
OUTPUT_LENGTH = 10

INPUT_LENGTH = x_test_normalized[1].flatten().shape[0]
OUTPUT_LENGTH = y_test[1].flatten().shape[0]
print(f"The input length is {INPUT_LENGTH} and the output length {OUTPUT_LENGTH}")
