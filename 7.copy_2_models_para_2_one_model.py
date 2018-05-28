# -*- coding: utf-8 -*-
# @Author  : Smart P
# @File    : copy_2_models_para_2_one_model.py
# @Desc    : copy_2_models_para_2_one_model
#coding=utf-8
import sys
import cPickle

#CAFFE_ROOT = sys.argv[1]
#LAYER_NAME = sys.argv[2]
#SRC_NET = sys.argv[3]
#SRC_WEIGHTS = sys.argv[4]
#TGT_NET = sys.argv[5]
#TGT_WEIGHTS = sys.argv[6]
CAFFE_ROOT_FlowNet2 = '/home/users/zhoujiqiang/TSN/flownet2/'
CAFFE_ROOT_TSN = '/home/users/zhoujiqiang/TSN/temporal-segment-networks-flownet2-2/lib/caffe-action/'

SRC_NET_FlowNet2 = "/home/users/zhoujiqiang/TSN/flownet2/FlowNet2-S/train.prototxt"
SRC_WEIGHTS_FlowNet2 = "/home/users/zhoujiqiang/TSN/flownet2/FlowNet2-S/FlowNet2-S_weights.caffemodel.h5"
SRC_NET_TSN = "./models/ucf101/tsn_bn_inception_flow_train_val.prototxt"
SRC_WEIGHTS_TSN = "./models/ucf101_split1_tsn_bn_inception_Flownet_iter_18000.caffemodel"
TGT_NET_FlowNet2xTSN = './models/ucf101/tsn_flownet2_bn_inception_flow_frozenTSN_norm_flownet_output_train_val.prototxt'
TGT_FlowNet2xTSN = './models/FlowNetxTSN_TSN_with_flowNet_img_18000_weights.caffemodel'

#Test_FlowNet2xTSN_Weight = 'models/FlowNet2-SxTSN_with_ImageNet_ft_iter18000_frozenTSN/FlowNet2-SxTSN_with_ImageNet_ft_iter18000_frozenTSN_iter_10000.caffemodel'
#保存FlowNet2的模型参数到pkl文件
# def load_model_FlowNet2():
# 	sys.path.append(CAFFE_ROOT_FlowNet2+'python')
# 	#print sys.path
# 	import caffe
# 	net_FlowNet2 = caffe.Net(SRC_NET_FlowNet2, SRC_WEIGHTS_FlowNet2, caffe.TRAIN)
# 	sys.path.remove(CAFFE_ROOT_FlowNet2+'python')
# 	return net_FlowNet2
#
# net_FlowNet2 = load_model_FlowNet2()
# FlowNet2_data = lambda blob:blob.data
# FlowNet2_params = [(k, map(FlowNet2_data, v)) for k, v in net_FlowNet2.params.items()]
# FlowNet2_params1={}
# FlowNet2_params1['params'] = FlowNet2_params
# cPickle.dump(FlowNet2_params1,open('FlowNet2_para.pkl','wb'))

#读取FlowNet2的模型参数的pkl文件
FlowNet2_params1 = cPickle.load(open('FlowNet2_para.pkl'))
for layer in FlowNet2_params1['params']:
    print layer[0]

sys.path.append(CAFFE_ROOT_TSN+'python')
import caffe
caffe.set_device(7)
net_TSN = caffe.Net(SRC_NET_TSN,SRC_WEIGHTS_TSN, caffe.TRAIN)
target_net = caffe.Net(TGT_NET_FlowNet2xTSN, caffe.TEST)
#test_net = caffe.Net(TGT_NET_FlowNet2xTSN,Test_FlowNet2xTSN_Weight, caffe.TRAIN)
print('model load successful!!!')

#copy FlowNet2 model layer weights to target net
for j,layer in enumerate(FlowNet2_params1['params']):
    #print layer[0]
    if layer[0] in target_net.params.keys():
        layer_name = layer[0]
        print layer_name
        if layer_name == 'img0s_aug' or layer_name == 'img1s_aug':
            for i in xrange(len(target_net.params[layer_name])):
                print i
                if i == 1:
                    target_net.params[layer_name][i].data[:] = FlowNet2_params1['params'][j][1][i][:,:,0:192,0:192]
                else:
                    target_net.params[layer_name][i].data[:] = FlowNet2_params1['params'][j][1][i]
        else:
            for i in xrange(len(target_net.params[layer_name])):
                print i
                target_net.params[layer_name][i].data[:] = FlowNet2_params1['params'][j][1][i]

#copy TSN model layer weights to target net
for name in net_TSN.params.keys():
    if name in target_net.params.keys():
        for i in xrange(len(target_net.params[name])):
            target_net.params[name][i].data[:] = net_TSN.params[name][i].data

target_net.save(TGT_FlowNet2xTSN)
print('all done')
