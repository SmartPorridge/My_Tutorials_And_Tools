#! /bin/bash
echo "hello world!"
thread_num=24
now_split=0
for ((j=$now_split; j<$thread_num; j++))
  do
  {
    echo $j
    python ./crop_video_black_borders.py $thread_num $j
  }&
  done
