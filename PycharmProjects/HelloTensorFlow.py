import tensorflow as tf

# hello = tf.constant('Hello, TensorFlow!')
# sess = tf.Session()
# print(sess.run(hello))
#
# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
# node3 = tf.add(node1, node2)
#
# print("node1: ", node1, "node2: ", node2)
# print("node3: ", node3)
#
# sess = tf.Session()
# print("sess.run(node1, node2):", sess.run([node1, node2]))
# print("sess.run(node3):",sess.run(node3))
#
# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# c = tf.placeholder(tf.float32)
# adder_node = a + b + c
# # 실행 단위
# sess = tf.Session()
# # 그 다음 sess.run 다음에 ---
# # Session(), sess.run은 실행시 기본
# print(sess.run(adder_node, feed_dict={a: 3, b: 4.5, c: 2.5}))
# print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4], c: [7, 3]}))

x_data = [[1, 2]]

X = tf.placeholder(tf.float32, shape=[None, 2])

# random_normal = w값을 초기화
# [2, 1] = shape 크기 선언
W = tf.Variable(tf.random_normal([2, 1]), name='weight')
# node가 1개라서 bias shape가 1이다
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    prediction = sess.run(hypothesis, feed_dict={X: x_data})
    print(prediction)

