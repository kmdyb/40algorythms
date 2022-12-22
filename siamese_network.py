import random
import numpy as np
import tensorflow as tf


def create_template():
    return tf.keras.models.Sequential([
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.15),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.15),
        tf.keras.layers.Dense(64, activation='relu'),
    ])


def prepare_data(inputs: np.ndarray, labels: np.ndarray):
    classes_numbers = 10
    digital_idx = [np.where(labels == i)[0] for i in range(classes_numbers)]
    pairs = list()
    labels = list()
    n = min([len(digital_idx[d]) for d in range(classes_numbers)]) - 1
    for d in range(classes_numbers):
        for i in range(n):
            z1, z2 = digital_idx[d][i], digital_idx[d][i+1]
            pairs += [[inputs[z1], inputs[z2]]]
            inc = random.randrange(1, classes_numbers)
            dn = (d + inc) % classes_numbers
            z1, z2 = digital_idx[d][i], digital_idx[dn][i]
            pairs += [[inputs[z1], inputs[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels, dtype=np.float32)


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.astype(np.float32)
x_test = x_test.astype(np.float32)
x_train /= 255
x_test /= 255
input_shape = x_train.shape[1:]
train_pairs, tr_labels = prepare_data(x_train, y_train)
test_pairs, test_labels = prepare_data(x_test, y_test)

input_a = tf.keras.layers.Input(shape=input_shape)
encoder1 = base_network(input_a)
input_b = tf.keras.layers.Input(shape=input_shape)
encoder2 = base_network(input_b)

distance = tf.keras.layers.Lambda(lambda embeddings: tf.keras.backend.abs(
    embeddings[0] - embeddings[1]))([encoder1, encoder2])
measure_of_similarity = tf.keras.layers.Dense(1, activation='sigmoid')(distance)

# budowa modelu
model = tf.keras.models.Model([input_a, input_b], measure_of_similarity)
# trenowanie
model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])

model.fit([train_pairs[:, 0], train_pairs[:, 1]], tr_labels,
          batch_size=128, epochs=10, validation_data=([test_pairs[:, 0], test_pairs[:, 1]], test_labels))
