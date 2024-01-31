
# VisualGLM-6B

可以对图片进行分析并文字输出

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


## Debian环境部署

设置代理环境
```bash
> export http_proxy=192.168.2.199:58591
> export https_proxy=192.168.2.199:58591
```

安装cuda
```bash
> wget https://developer.download.nvidia.com/compute/cuda/12.3.1/local_installers/cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb
> sudo dpkg -i cuda-repo-debian12-12-3-local_12.3.1-545.23.08-1_amd64.deb
> sudo cp /var/cuda-repo-debian12-12-3-local/cuda-*-keyring.gpg /usr/share/keyrings/
> sudo add-apt-repository contrib
> sudo apt-get update
> sudo apt-get -y install cuda-toolkit-12-3
```

设置python虚拟环境
```bash
> sudo apt install python3-venv python3-pip
> mkdir /opt/Data/PythonVenv
> cd /opt/Data/PythonVenv
> python3 -m venv visualglm6b
> source /opt/Data/PythonVenv/visualglm6b/bin/activate
```

部署推理环境
```bash
> pip install -r requirements.txt
> pip install gradio
> pip install pyreadline3
> pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
> pip install -i https://pypi.tuna.tsinghua.edu.cn/simple transformers==4.33.2
```


## 部署工具

### 命令行 Demo

```shell
> set MODEL_PATH=E:\THUDM\visualglm-6b
> export MODEL_PATH=/opt/Data/THUDM/visualglm-6b
> python example/sayhello.py
```

code from

[https://github.com/THUDM/VisualGLM-6B]
