import tensorflow as tf

# 检查 TensorFlow 是否能够检测到 GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"TensorFlow 检测到 {len(gpus)} 个 GPU：")
    for gpu in gpus:
        print(f"  - {gpu}")
else:
    print("TensorFlow 未检测到 GPU。")
