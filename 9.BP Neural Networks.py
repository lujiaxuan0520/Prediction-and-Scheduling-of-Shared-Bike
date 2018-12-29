#!/usr/bin/python
# coding=utf-8
import tensorflow as tf
import numpy as np
from sklearn.preprocessing import scale
import csv


# neuron_size为输入神经元的列表，第一个元素为输入层元素的个数,最后一个为输出层元素
class Bpnn:
    def __init__(self, neuron_size, learning_rate):
        self.input_holder = tf.placeholder(tf.float32, [None, neuron_size[0]])
        self.output_holder = tf.placeholder(tf.float32, [None, neuron_size[-1]])
        self.weight = {}
        self.bias = {}
        self.layers = {}
        for i in range(len(neuron_size) - 1):
            # 第i+1层神经元与前一层输入的各个权重w组成的矩阵
            self.weight[i+1] = tf.Variable(tf.random_normal([neuron_size[i], neuron_size[i+1]]))
        for i in range(len(neuron_size) - 1):
            # 第i+1层每个神经元的偏移量b
            self.bias[i+1] = tf.Variable(tf.random_normal([neuron_size[i+1]]))
        # layers存放第i层wx+b作用relu激活函数后的结果
        self.layers[1] = tf.nn.tanh(tf.add(tf.matmul(self.input_holder, self.weight[1]), self.bias[1]))
        layer_stack = [self.layers[1]]
        for i in range(len(neuron_size) - 1):
            if i != 0 and i != 1:
                # 计算中间层的layers:r(wx+b)
                self.layers[i] = tf.nn.relu(tf.add(tf.matmul(layer_stack[-1], self.weight[i]), self.bias[i]))
                layer_stack.append(self.layers[i])
        # outlayer为预测的输出值
        self.out_layer = tf.add(tf.matmul(layer_stack[-1], self.weight[len(neuron_size) - 1]), self.bias[len(neuron_size) - 1])
        # 损失函数：计算输出的目标值与预测值的偏差
        self.loss = tf.reduce_mean(tf.reduce_sum(tf.square(self.output_holder - self.out_layer), reduction_indices=[1]))
        self.train_step = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(self.loss)
        self.init = tf.global_variables_initializer()
        self.run_config = tf.ConfigProto(device_count={'gpu': 0})
        self.run_config.gpu_options.allow_growth=True
        self.sess = tf.Session(config=self.run_config)
        self.saver = tf.train.Saver()

    def train1(self, _input, _output):
        self.sess.run(self.init)
        for i in range(20000):
            self.sess.run(self.train_step, feed_dict={self.input_holder: _input, self.output_holder: _output})
            if i % 50 == 0:
                print("迭代次数:"+str(i))
                print(self.sess.run(self.loss, feed_dict={self.input_holder: _input, self.output_holder: _output}))
                # print(self.sess.run(self.out_layer, feed_dict={self.input_holder: _input, self.output_holder: _output}))
            '''if self.sess.run(self.loss, feed_dict={self.input_holder: _input, self.output_holder: _output}) < 50:
                self.saver.save(self.sess, "save/model.ckpt")
                break'''
        self.saver.save(self.sess, "save/model.ckpt")

    def predict(self, _input):
        f = open('predict_result.txt', 'w')
        for each_input in _input:
            each_input = each_input.reshape(1, len(each_input))
            f.write(str(self.sess.run(self.out_layer, feed_dict={self.input_holder: each_input})).lstrip('[ ').rstrip(']'))
            f.write('\n')
        f.close()

    def load_nn(self):
        self.saver.restore(self.sess, "save/model.ckpt")



if __name__=='__main__':
    # 训练数据
    input_arr = np.load("input_arr.npy")
    output_arr = np.load("output_arr.npy")

    # 测试数据
    test_input_arr = np.load("test_input_arr.npy")
    test_output_arr = np.load("test_output_arr.npy")

    input_arr = scale(input_arr)
    test_input_arr = scale(test_input_arr)
    model = Bpnn([23, 20, 18, 16, 14, 12, 10, 7, 5, 3, 1], 0.00025)
    #model.load_nn()
    model.train1(test_input_arr, test_output_arr)
    model.predict(test_input_arr)

