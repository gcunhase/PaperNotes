#
# Script to test CPU vs GPU performance using Tensorflow
#  Also check: https://www.tensorflow.org/tutorials/using_gpu
#
# Author: Gwena Cunha
# Date: Sep 24th 2017
#

import tensorflow as tf
from timeit import default_timer as timer
import math
import numpy as np
    
    
# Check with cpu and gpu
def test_matmul(device_name):
	# Use tf.device to manually assign a device
	# Creates a graph.
	with tf.device(device_name):
		a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
		b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
		c = tf.matmul(a, b)
	# Creates a session with log_device_placement set to True.
	sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
	# Runs the op.
	print(sess.run(c))

def test_powers(device_name):
	# Use tf.device to manually assign a device
	# Creates a graph.
	with tf.device(device_name):
		p = tf.placeholder(tf.float32, None)
		q = tf.placeholder(tf.float32, None)
		r = tf.placeholder(tf.float32, None)
		s = tf.placeholder(tf.float32, None)
		#inp = tf.placeholder(tf.float32)
		y = tf.sqrt(p ** 2 + q ** 3 + r ** 4 + s ** 5)#math.sqrt(p ** 2 + q ** 3 + r ** 4 + s ** 5) #tf.py_func(powers, [inp], tf.float32)
	# Creates a session with log_device_placement set to True.
	with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:
		n = 5000000
		p1 = np.random.rand(n)
		q1 = np.random.random(n)
		r1 = np.random.random(n)
		s1 = np.random.random(n)
		# Runs the op.
		result = sess.run(y, feed_dict={p: p1, q: q1, r: r1, s: s1})
		print(result)



if __name__ == "__main__":

	start = timer()
	test_powers(device_name = '/cpu:0')
	end_cpu = timer()-start
	
	start = timer()
	test_powers(device_name = '/gpu:0')
	end_gpu = timer()-start
	print("CPU ran for:  "+str(end_cpu)+" seconds - "+"GPU ran for:  "+str(end_gpu))

