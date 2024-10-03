import cv2
import numpy as np
from PIL import Image

def extract_alpha_mask(source_image):
    """
    根据图像的alpha通道生成掩码。
    """
    alpha_channel = source_image[:, :, 3]
    # 生成二值化的掩码
    mask = np.where(alpha_channel > 0, 255, 0).astype(np.uint8)
    return mask

def apply_mask(source_image_path, target_image_path, output_path):
    """
    根据源图像的Alpha通道，对目标图像进行裁切
    """
    # 读取源图像
    source_image = Image.open(source_image_path).convert("RGBA")
    source_np = np.array(source_image)

    # 读取目标图像
    target_image = Image.open(target_image_path).convert("RGBA")
    target_np = np.array(target_image)

    # 确保源图像尺寸与目标图像尺寸匹配
    source_image_resized = source_image.resize((target_image.width, target_image.height), Image.Resampling.LANCZOS)
    source_np_resized = np.array(source_image_resized)

    # 提取源图像alpha通道生成掩码
    mask = extract_alpha_mask(source_np_resized)

    # 重新调整目标图像的掩码尺寸
    mask_resized = cv2.resize(mask, (target_np.shape[1], target_np.shape[0]), interpolation=cv2.INTER_NEAREST)

    # 扩展单通道掩码至四通道
    mask_4_channel = np.stack([mask_resized] * 4, axis=-1)

    # 使用掩码裁剪目标图像
    masked_target_np = np.where(mask_4_channel == 255, target_np, 0)

    # 转换并保存结果图像
    masked_target_image = Image.fromarray(np.uint8(masked_target_np))
    masked_target_image.save(output_path)

# 使用函数
apply_mask('raw.png', 'resized_target.png', 'Treated.png')