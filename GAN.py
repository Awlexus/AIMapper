# https://github.com/tflearn/tflearn/blob/master/examples/images/gan.py

import tensorflow as tf
import tflearn
import numpy as np
import matplotlib.pyplot as plt

z_dim = 100
total_maps = 1000


def discriminator(input_data, reuse=False):
    with tf.variable_scope('Discriminator', reuse=reuse):
        net = tflearn.lstm(input_data, 64, dropout=0.6)
        return tflearn.fully_connected(net, 2, activation='softmax')


def generator(input_data, reuse=False):
    with tf.variable_scope('Generator', reuse=reuse):
        net = tflearn.lstm(input_data, 64, dropout=0.6)
        return tflearn.fully_connected(net, 2, activation='softmax')


# Calculate this when actually loading maps
maxlength = -1

# Build networks
gen_input = tflearn.input_data([None, z_dim], name='Input_noise')
disc_input = tflearn.input_data([None, maxlength], name='disc_input')

gen_sample = generator(gen_input)
disc_real = discriminator(disc_input)
disc_fake = discriminator(gen_sample, reuse=True)

# Define loss
disc_loss = -tf.reduce_mean(tf.log(disc_real) + tf.log(1. - disc_fake))
gen_loss = -tf.reduce_mean(tf.log(disc_fake))

# Build Training Ops for both Generator and Discriminator.
# Each network optimization should only update its own variable, thus we need
# to retrieve each network variables (with get_layer_variables_by_scope) and set
# 'placeholder=None' because we do not need to feed any target.
gen_vars = tflearn.get_layer_variables_by_scope('Generator')
gen_model = tflearn.regression(gen_sample, placeholder=None, optimizer='adam',
                               loss=gen_loss, trainable_vars=gen_vars,
                               batch_size=64, name='target_gen', op_name='GEN')
disc_vars = tflearn.get_layer_variables_by_scope('Discriminator')
disc_model = tflearn.regression(disc_real, placeholder=None, optimizer='adam',
                                loss=disc_loss, trainable_vars=disc_vars,
                                batch_size=64, name='target_disc', op_name='DISC')

# Define GAN model, that output the generated images.
gan = tflearn.DNN(gen_model)

# Training
# Generate noise to feed to the generator
z = np.random.uniform(-1., 1., size=[total_maps, z_dim])
# Start training, feed both noise and real images.
gan.fit(X_inputs={gen_input: z, disc_input: X},
        Y_targets=None,
        n_epoch=100)

# Generate images from noise, using the generator network.
f, a = plt.subplots(2, 10, figsize=(10, 4))
for i in range(10):
    for j in range(2):
        # Noise input.
        z = np.random.uniform(-1., 1., size=[1, z_dim])
        # Generate image from noise. Extend to 3 channels for matplot figure.
        temp = [[ii, ii, ii] for ii in list(gan.predict([z])[0])]
        a[j][i].imshow(np.reshape(temp, (28, 28, 3)))
f.show()
plt.draw()
plt.waitforbuttonpress()
