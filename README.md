
# VisualGLM-6B

## Windows环境部署

 准备独立的python环境
```bash
> cmd
> cd D:\devtools\PythonVenv
> python3 -m venv visualglm6b
> D:\devtools\PythonVenv\visualglm6b\Scripts\activate.bat
> set http_proxy=192.168.2.199:58591
> set https_proxy=192.168.2.199:58591
```

部署推理环境

```bash
> pip install -r requirements.txt
> pip install gradio
> pip install pyreadline3
> pip install sentencepiece
> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
> pip install transformers==4.33.2
```

python环境切换
```bash
> cmd
> D:\devtools\PythonVenv\visualglm6b\Scripts\activate.bat
```


## 部署工具

### 命令行 Demo

```shell
> set MODEL_PATH=E:\THUDM\visualglm-6b
> python example/sayhello.py
```

code from

[https://github.com/THUDM/VisualGLM-6B]