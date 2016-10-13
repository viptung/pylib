#coding=utf-8
from common_import import *
from model import LeNet

util.log.init_logger('~/temp/lenet.log');

# 创建Iter的时间越早越好.
batch_size = 100
image_shape = (224, 224)
train_iter, val_iter = get_iter(image_shape = image_shape, batch_size = batch_size, prefetch = 5, num_threads = 8)

net = LeNet()
solver = SGDSolver(
        train_iter = train_iter, 
        batch_size = 100, 
        epochs = 20,
        learning_rate = 0.0001,
        val_iter = val_iter,
        dump_path = '~/temp')
solver.fit(net)
