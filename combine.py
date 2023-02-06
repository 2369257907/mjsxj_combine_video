import os
import shutil

def move_videos_to_result(src_dir):
    # 创建result目录
    result_dir = os.path.join('result')
    if os.path.exists(result_dir):
        shutil.rmtree(result_dir)
    os.makedirs(result_dir)

    # 遍历一级子目录
    for sub_dir in os.listdir(src_dir):
        sub_dir_path = os.path.join(src_dir, sub_dir)
        if not os.path.isdir(sub_dir_path):
            continue

        # 如果子目录名称的前8位相同
        first_8_chars = sub_dir[:8]
        dest_dir = os.path.join(result_dir, first_8_chars)
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # 复制视频到result目录下
        for video in os.listdir(sub_dir_path):
            if not video.endswith('.mp4'):
                continue
            src_video = os.path.join(sub_dir_path, video)
            dest_video = os.path.join(dest_dir, video)
            shutil.copy(src_video, dest_video)

# 调用函数
src_dir = 'E:\\MIJIA_RECORD_VIDEO'
move_videos_to_result(src_dir)
