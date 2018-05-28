#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : smart porridge
import os,glob,sys,shutil,cv2
from time import time
import argparse

def generate_frames(video_root, decoded_images_root,video_part,ffmpeg_bin_root, split_num, now_split):

	video_part_path = video_root + video_part
	decoded_images_path = '{}{}/'.format(decoded_images_root,video_part)

	video_list=[]
	for label in os.listdir(video_part_path):
		for video in os.listdir(video_part_path+'/'+label):
			video_list.append(label+'/'+video)
	#video_list = glob.glob(os.path.join(video_part_path,'*/*.mp4'))
	
	#print(video_list)
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
		#video_name = video_path.strip().split("/")[-1]
		#video_label = video_path.strip().split("/")[-2]
		decoded_video_path = decoded_images_path + video_path
		origin_video_path = video_part_path + '/' + video_path
		print(origin_video_path)
		print(decoded_video_path)

		# if not os.path.exists(decoded_video_path):
		# 	os.makedirs(decoded_video_path)

		print('--------------------------')
		print("Processing {}-{} videos in total {} videos").format(start,end,len(video_list))
		print("Now processing {} , {}".format(str(i),video_path))

		#无损解图片
		if not os.path.exists(decoded_video_path):
			os.makedirs(decoded_video_path)
			#command = "{}ffmpeg -i {} -q:v 1 {}/image_%5d.jpg".format(ffmpeg_bin_root, origin_video_path, decoded_video_path)
			command = "{}ffmpeg -i {} -q:v 1 -r 25 {}/image_%5d.jpg".format(ffmpeg_bin_root, origin_video_path, decoded_video_path)
			print(command)
			os.system(command)

		with open("{}{}_{}_BasicAlg.txt".format(video_root,video_part,str(now_split)),'a+') as f:
			f.write(decoded_video_path.strip() + '\n')

def main():
	print("hahhahahaha")
	print(len(sys.argv))
	if len(sys.argv) != 3:
		print("input wrong:csv_file dataset_name")
	split_num = int(sys.argv[1])
	now_split = int(sys.argv[2])
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
	print(split_num)
	print(now_split)

	video_root = "video/"
	decoded_images_root = "img/"
	ffmpeg_bin_root = "ffmpeg_build/bin/"

	video_part = 'test' #处理数据集哪一个文件夹下的视频 :

	generate_frames(video_root, decoded_images_root, video_part, ffmpeg_bin_root, split_num,now_split)
	print("all done")

if __name__ == "__main__":
	main()
