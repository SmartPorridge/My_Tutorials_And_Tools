#coding=-UTF8-
#author  : smartporridge
import os,sys
import commands
import argparse

def get_crop_info(video,ffmpeg_bin,video_name):
	#if os.path.exists("dummy.mp4"):
		#os.remove("dummy.mp4")
	#(status, info) = commands.getstatusoutput("{} -i {} -vf cropdetect=24:16:0 dummy_{}.mp4".format(ffmpeg_bin,video,video_name.split('.')[0]))
	(status, info) = commands.getstatusoutput("{} -i {} -vf cropdetect=24:16:0 dummy_{}.mp4".format(ffmpeg_bin,video,video_name.split('.')[0]))
	#cropdetect=limit:round:reset
	# limit = black threshold (default 24)
	# round = output resolution must be divisible to this
	# reset = after how many frames the detection process will start over
	
	print(info)
	os.remove("dummy_{}.mp4".format(video_name.split('.')[0]))
	crop_info = info[info.find("crop=")+5:]
	coor_list = crop_info.split("\n")[0].split(':')
	print(coor_list)
	return coor_list

def crop_video(src_video_list,ffmpeg_bin,video_num,src_root,dst_root,thread_num,thread_index):
	print("thread_index: {}".format(thread_index))
	video_start_num = (video_num/thread_num)*thread_index
	video_end_num = (video_num/thread_num)*(thread_index+1)

    #最后一个线程处理到最后
	if (thread_index == (thread_num-1)):
		video_end_num = video_num

	for j in range(video_start_num, video_end_num):
		print('\n******************\n'+"thread_index:" + str(thread_index) + "\nrange: ["+str(video_start_num) +","+str(video_end_num)+")\n")
		video = src_video_list[j]
		print(video)
		video_src = "{}{}".format(src_root,video)
		video_dst = "{}{}".format(dst_root,video)

		coor_list = get_crop_info(video_src,ffmpeg_bin,video)
		paras="{} -i {} -vf crop={}:{}:{}:{} {}".format(ffmpeg_bin,video_src,int(coor_list[0]),int(coor_list[1]),int(coor_list[2]),int(coor_list[3]),video_dst)
		print(paras)
		(status, info) = commands.getstatusoutput(paras)


def main():
	ffmpeg_bin = "~/ffmpeg/ffmpeg_build/bin/ffmpeg"
	src_root = "video/test/"
	dst_root = "video/test_crop_black_borders/test_crop/"

	src_video_list = os.listdir(src_root)
	src_video_list.sort()
	video_num = len(src_video_list)

	thread_num = int(sys.argv[1])
	now_split = int(sys.argv[2])


	crop_video(src_video_list,ffmpeg_bin,video_num,src_root,dst_root,thread_num,now_split)

	print("all done")
if __name__ == '__main__':
	main()
