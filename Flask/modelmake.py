import tensorflow as tf
import numpy as np
from pandas.io.parsers import read_csv

model=tf.global_variables_initializer()
data=read_csv('final1101.csv', sep=',')
xy=np.array(data, dtype=np.float32)
#print(xy)

x_data = xy[:,1:-1]
y_data = xy[:,[-1]]
X=tf.placeholder(tf.float32, shape=[None,4])
Y=tf.placeholder(tf.float32, shape=[None,1])
W=tf.Variable(tf.random_normal([4,1]), name="weight")
b=tf.Variable(tf.random_normal([1]), name="bias")
hypothesis=tf.matmul(X,W)+b
cost=tf.reduce_mean(tf.square(hypothesis-Y))

optimizer =tf.train.GradientDescentOptimizer(learning_rate=0.000005)
train=optimizer.minimize(cost)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(100001) :
    cost_, hypo_, _=sess.run([cost, hypothesis, train], feed_dict={X:x_data, Y:y_data})
    if step % 500 == 0:
        print("#", step, " 손실비용:", cost_)
        print("- 배추가격: -", hypo_[0])

saver = tf.train.Saver()
save_path = saver.save(sess,"./saved.cpkt")
print("학습된모델을 저장했습니다.")