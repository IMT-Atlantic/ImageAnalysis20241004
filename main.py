# main.py

import sys
import os

# 添加当前目录到sys.path中，以便可以导入脚本中的模块
current_directory = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_directory)

from NorImage import resize_to_match
from DistillCut import apply_mask

def main():
    # 设置文件路径
    input_image_path = 'raw.png'
    target_image_path = 'target.png'
    resized_target_image_path = 'resized_target.png'
    output_image_path = 'Treated.png'

    # 调用函数进行缩放
    resize_to_match(input_image_path, resized_target_image_path, target_image_path)

    # 调用函数使用 alpha 通道裁剪
    apply_mask(input_image_path, target_image_path, output_image_path)

if __name__ == "__main__":
    main()