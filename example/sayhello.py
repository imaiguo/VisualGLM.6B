
import os

from transformers import AutoTokenizer, AutoModel

MODEL_PATH = os.environ.get('MODEL_PATH', 'THUDM/visualglm-6b')

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
model = AutoModel.from_pretrained(MODEL_PATH, trust_remote_code=True).quantize(4).half().cuda()

image_path = "../examples/1.jpeg"

response, history = model.chat(tokenizer, image_path, "描述这张图片。", history=[])
print(response)

response, history = model.chat(tokenizer, image_path, "这张图片可能是在什么场所拍摄的？", history=history)
print(response)