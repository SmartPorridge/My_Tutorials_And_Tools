#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 15:41
# @Author  : Smart Porridge
# @File    : decode_videos2images.py
# @Software: PyCharm
# @Desc    : decode_videos2images 
import os,glob
from time import time
import argparse

def generate_frames(video_root, decoded_images_root,video_part,ffmpeg_bin_root, split_num, now_split):

	video_part_path = video_root + video_part
	decoded_images_path = '{}{}/'.format(decoded_images_root,video_part)
	video_list = glob.glob(os.path.join(video_part_path,'*.mp4'))
	print("There are {} videos in {}".format(len(video_list),video_part_path))

	video_list.sort()
	stride = len(video_list) / split_num

	start = stride * now_split
	end = stride * (now_split + 1)
	if split_num == (now_split+1):
		end = len(video_list)
	video_list = video_list[start:end]
	print('Now processing {}-{} videos, total {} videos.'.format(str(start),str(end),len(video_list)))
	print('Decoded images are saved to : {}'.format(decoded_images_path))


	for i, video_path in enumerate(video_list):
		video_name = video_path.strip().split("/")[-1]
		decoded_video_path = decoded_images_path + video_name

		if not os.path.exists(decoded_video_path):
			os.makedirs(decoded_video_path)

		print('--------------------------')
		print("Processing {}-{} videos in total {} videos").format(start,end,len(video_list))
		print("Now processing {} , {}".format(str(i),video_name))

		#无损解图片
		command = "{}ffmpeg -i {} -q:v 1 {}/image_%5d.jpg".format(ffmpeg_bin_root, video_path, decoded_video_path)
		print(command)
		os.system(command)

		with open("{}{}_{}.txt".format(video_root,video_part,str(now_split)),'a+') as f:
			f.write(video_path.strip() + '\n')

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--split_num',help='split to how many parts',default = 3)
	parser.add_argument('--now_split',help='which part to process now',default = 0)
	args = parser.parse_args()

	split_num = int(args.split_num)
	now_split = int(args.now_split)

	video_root = "kinetics/video/"
	video_part = 'train/train_part3' #处理数据集哪一个文件夹下的视频 : val train/train_part1 train/train_part2 train/train_part3
	decoded_images_root = "kinetics/img/"
	ffmpeg_bin_root = "ffmpeg/ffmpeg_build/bin/"

	generate_frames(video_root, decoded_images_root, video_part, ffmpeg_bin_root, split_num,now_split)
	print "all done"

if __name__ == "__main__":
	main()
