# @Desc    : decode_videos2images 
import os,glob
from time import time

video_root = "kinetics/video/"
images_root = "kinetics/img/"
ffmpeg_bin_root = "/home/users//ffmpeg/ffmpeg_build/bin/"

split_num = 3
now_split = 2


def generate_frames(split):
	# video_list = os.listdir(video_root+split)

	video_list = glob.glob(os.path.join(video_root + split, "train_part3/*.mp4"))
	# video_list = glob.glob(os.path.join(video_root + split, "*.mp4"))
	print len(video_list)

	# video_list = open(split+".txt", "r").readlines()
	video_list.sort()
	stride = len(video_list) / split_num


	start = stride * now_split
	end = stride * (now_split + 1)
	if 2 == now_split:
		end = len(video_list)

	video_list = video_list[start:end]

	cnt = 0
	new_video = 0
	for i, video_path in enumerate(video_list):
		new_video_path = video_path.strip().split("/")[-1]

		new_video_path = images_root + split + "/train_part3/" + new_video_path

		# new_video_path = images_root + split + "/" + new_video_path
		
		# if os.path.exists(new_video_path):
		# 	# print new_video_path
		# 	cnt += 1
		# 	img_list = glob.glob(os.path.join(new_video_path, "*.jpg"))
		# 	if 0 != len(img_list):
		# 		continue

		# continue
		new_video += 1

		print "\n\n\n\nprocessing " + video_path +"……………………"
		print i
		# if not os.path.exists(new_video_path):
		# 	print "no this file:", new_video_path
		os.makedirs(new_video_path)
		# # cnt += 1
		# print cnt
		# print new_video

		# continue

		#无损解图片
		command = "{}ffmpeg -i {} -q:v 1 {}/image_%5d.jpg".format(ffmpeg_bin_root, video_path, new_video_path)
		print command
		os.system(command)

		with open("16train2" + str(now_split)+".txt", "a+") as f:
			f.write(video_path.strip() + "\n")

generate_frames("train")
print "done"
