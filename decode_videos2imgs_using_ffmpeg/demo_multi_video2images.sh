#! /bin/bash
echo "hello"
ini_j=0
end_j=48
for ((j=$ini_j; j<$end_j; j++))
  do
  {
    echo $j
    python ./decode_videos2images.py $end_j $j
  }&
  done
