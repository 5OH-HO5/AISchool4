# # p.52 2주차
# import matplotlib.pyplot as plt
# import numpy as np
#
# from tensorflow.examples.tutorials.mnist import input_data
#
# mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
#
# # images = 보이는 픽셀데이터
# print(np.shape(mnist.train.images))
# # labels 정답 데이터
# print(np.shape(mnist.train.labels))
# print(np.shape(mnist.test.images))
# print(np.shape(mnist.test.labels))
# # 인덱스 번호
# print(mnist.train.labels[1])
#
# # reshape은 원래 데이터가 일렬로 들어있는데 사람들이 보기 편하게 정의된 사이즈(28*28)로 만들어주는 함수
# plt.imshow(
#     mnist.train.images[1].reshape(28, 28),
#     cmap="Greys",
#     # imterpolation 사이즈 조절
#     interpolation="nearest", )
#
# plt.show()


# p.54 2주차
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# placeholder 값을 담는 그릇
X = tf.placeholder(tf.float32, [None, 784])
# x= 784개
# y= 0~9까지
Y = tf.placeholder(tf.float32, [None, 10])

# weight matrix 는 x가 784이라서 784개의 픽셀이 들어오고 256개의 뉴런으로 설정
W1 = tf.Variable(tf.random_normal([784, 1024]))
# W1에서 256을 설정했기 때문에 256
b1 = tf.Variable(tf.random_normal([1024]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)

W2 = tf.Variable(tf.random_normal([1024, 256]))
# bias도 weight값 따라오기
b2 = tf.Variable(tf.random_normal([256]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)

W3 = tf.Variable(tf.random_normal([256, 10]))
b3 = tf.Variable(tf.random_normal([10]))
hypothesis = tf.matmul(L2, W3) + b3

softmax_result = tf.nn.softmax(hypothesis)

# Loss Function 공식에 그대로 대입한 버전
# cost = 에러
cost = tf.reduce_mean(-tf.reduce_sum(Y * tf.log(hypothesis), axis=1))

# tensorflow용 쉬운버전 // 결과값은 위와 동일
# 얼마나 틀렸는지 담는 변수를 cost라고 했다
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits( logits=hypothesis, labels=Y))

# loss를 줄이는 방식으로
learning_rate = 0.001
# Back-Propagation하는(adagrad 등) optimizer 변수에 담는다
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)

sess = tf.Session()
# 데이터 전체를 한바퀴 도는 것을 epoch이라고 함
# batch size 데이터 하나하나
# lterations 데이터 하나하나 묶음
sess.run(tf.global_variables_initializer())

training_epochs = 15
batch_size = 100

# Accuracy 정확도
max = 0.0
early_stopped = 0
for epoch in range(training_epochs):
    avg_cost = 0
    total_batch = int(mnist.train.num_examples / batch_size)

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        feed_dict = {X: batch_xs, Y: batch_ys}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'training cost =', '{:.9f}'.format(avg_cost))
    correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    test_accuracy = sess.run(accuracy, feed_dict={X: mnist.test.images, Y: mnist.test.labels})
    print('Test Accuracy:', test_accuracy)
    if test_accuracy > max:
        max = test_accuracy
        early_stopped = epoch + 1

print('Learning Finished!')
print('Test Max Accuracy:', max)
print('Early stopped time:', early_stopped)
# Test model and check accuracy