# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
import argparse
import fnmatch
import glob
import json
import os
import shutil
import subprocess
import uuid

from joblib import delayed
from joblib import Parallel
import pandas as pd

file_src = 'video_list.txt'
folder_path = 'video/train_340/'
output_path = 'train_112/'


# file_src = '/vallist.txt'
# folder_path = 'YOUR_DATASET_FOLDER/val/'
# output_path = 'YOUR_DATASET_FOLDER/val_256/'

ffmpeg_bin_root = "ffmpeg_build/bin/"

# file_list = []

file_list = glob.glob(os.path.join(folder_path, "*/*mp4"))

# f = open(file_src, 'r')

# for line in f:
#     rows = line.split()
#     fname = rows[0]
#     file_list.append(fname)

# f.close()


def downscale_clip(inname, outname):

    status = False
    inname = '"%s"' % inname
    outname = '"%s"' % outname

    print inname
    print outname
    # command = "ffmpeg  -loglevel panic -i {} -filter:v scale=\"trunc(oh*a/2)*2:256\" -q:v 1 -c:a copy {}".format(inname, outname)

    # command = "{}ffmpeg  -loglevel panic -i {} -filter:v scale=\"trunc(oh*a/2)*2:340\" -q:v 1 -c:a copy {}".format(ffmpeg_bin_root, inname, outname)
    command = "{}ffmpeg  -loglevel panic -i {} -filter:v scale=\"trunc(oh*a/2)*2:112\" -q:v 1 -c:a copy {}".format(ffmpeg_bin_root, inname, outname)

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        return status, err.output

    status = os.path.exists(outname)
    return status, 'Downscaled'


def downscale_clip_wrapper(row):

    nameset  = row.strip().split('/')
    videoname = nameset[-1]
    # classname = nameset[-2]

    # videoname = rows.strip()

    # output_folder = output_path + classname
    output_folder = output_path
    if os.path.isdir(output_folder + nameset[-2]) is False:
        try:
            os.makedirs(output_folder + nameset[-2])
        except:
            print(output_folder + nameset[-2])

    # inname = folder_path + classname + '/' + videoname
    # outname = output_path + classname + '/' +videoname

    # inname = folder_path + '/' + videoname
    inname = row
    # outname = output_path + '/' + videoname
    outname = output_path + nameset[-2] + "/" + videoname

    # if not os.path.exists(outname):
    #     outname_2nd = output_path + '/' + videoname
    #     print outname
    #     shutil.copy(inname, outname_2nd)
    downscaled, log = downscale_clip(inname, outname)
    return downscaled


status_lst = Parallel(n_jobs=32)(delayed(downscale_clip_wrapper)(row) for row in file_list)

# for row in file_list:
#     downscale_clip_wrapper(row)
