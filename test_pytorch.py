import torch
import tensorflow as tf

if torch.cuda.is_available():
    print("PyTorch is available with GPU support.")
else:
    print("PyTorch is available without GPU support.")

print("PyTorch version:", torch.__version__)

print(tf.reduce_sum(tf.random.normal([1000, 1000])))
print(tf.config.list_physical_devices("GPU"))
