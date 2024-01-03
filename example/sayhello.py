
import os
import torch

from transformers import AutoTokenizer, AutoModel

DEVICE = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
print(f"DEVICE:{DEVICE}")

MODEL_PATH = os.environ.get('MODEL_PATH', 'THUDM/visualglm-6b')

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)

# AMD, NVIDIA GPU can use Half Precision
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).quantize(8).half().cuda()

# model, model_args = VisualGLMModel.from_pretrained('visualglm-6b', args=argparse.Namespace(fp16=True, skip_init=True))

# CPU, Intel GPU and other GPU can use Float16 Precision Only
# model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).float().eval()

model = model.eval()

image_path = "./examples/1.jpeg"

response, history = model.chat(tokenizer, image_path, "描述这张图片。", history=[])
print("ansower 1:" + response)
print(response)

response, history = model.chat(tokenizer, image_path, "这张图片可能是在什么场所拍摄的？", history=history)
print("ansower 2:" + response)
print(response)