import tensorflow as tf

SAVED_MODELS_PATH = 'saved_models/meetjs'

# Model parameters
W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)
# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()

saver = tf.train.Saver([W, b])

sess = tf.Session()
sess.run(init) # reset values to wrong
for step in range(1000):
    sess.run(train, {x: x_train, y: y_train})
    if step % 100 == 0:
      # Append the step number to the checkpoint name:
      saver.save(sess, SAVED_MODELS_PATH, global_step=step)

# evaluate training accuracy
curr_W, curr_b, curr_loss  = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s" % (curr_W, curr_b, curr_loss))
