#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 10:20
# @Author  : Smartporridge Zhou
# @File    : copy_2_models_para_2_one_model.py
# @Software: PyCharm Community Edition
import sys
CAFFE_ROOT= '/home/users/zhoujiqiang/TSN/flownet2/'
sys.path.append(CAFFE_ROOT_TSN+'python')
import caffe
caffe.set_device(0)

SRC_NET_1 = "/home/users/zhoujiqiang/TSN/flownet2/FlowNet2-S/train.prototxt"
SRC_WEIGHTS_1 = "/home/users/zhoujiqiang/TSN/flownet2/FlowNet2-S/FlowNet2-S_weights.caffemodel.h5"

SRC_NET_2 = "./models/ucf101/tsn_bn_inception_flow_train_val.prototxt"
SRC_WEIGHTS_2 = "./models/ucf101_split1_tsn_bn_inception_Flownet_iter_18000.caffemodel"

TGT_NET = './models/ucf101/tsn_flownet2_bn_inception_flow_frozenTSN_norm_flownet_output_train_val.prototxt'
TGT_NET_MODEL = './models/FlowNetxTSN_TSN_with_flowNet_img_18000_weights.caffemodel'

net_1 = caffe.Net(SRC_NET_1, SRC_WEIGHTS_1, caffe.TRAIN)
net_2 = caffe.Net(SRC_NET_2, SRC_WEIGHTS_2, caffe.TRAIN)

target_net = caffe.Net(TGT_NET, caffe.TEST)
#test_net = caffe.Net(TGT_NET_FlowNet2xTSN,Test_FlowNet2xTSN_Weight, caffe.TRAIN)
print('model load successful!!!')


#copy net_1 model layer weights to target net
for name in net_1.params.keys():
    if name in target_net.params.keys():
        for i in xrange(len(target_net.params[name])):
            target_net.params[name][i].data[:] = net_1.params[name][i].data

#copy net_2 model layer weights to target net
for name in net_2.params.keys():
    if name in target_net.params.keys():
        for i in xrange(len(target_net.params[name])):
            target_net.params[name][i].data[:] = net_2.params[name][i].data

target_net.save(TGT_NET_MODEL)
print('all done')
