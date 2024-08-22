# Physics Master

Physics Master is a model finetuned from [unsloth/llama-3-8b-Instruct-bnb-4bit](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) and [ArtifactAI/arxiv-physics-instruct-tune-30k](https://huggingface.co/datasets/ArtifactAI/arxiv-physics-instruct-tune-30k). Here is the python code. The model is open source on [Hugging Face](https://huggingface.co/gallen881/Llama-3-8B-Physics_Master-GGUF).

## How to use?

### Run model on local computer

1. Clone this repo.
    ```
    git clone https://github.com/gallen881/Physics_Master.git
    ```
2. Move to `Physics_Master`
    ```
    cd Physics_Master
    ```
3. Install dependencies.
    ```
    pip install -r requirements.txt
    ```
3. Run `chat.py`.
    ```
    python chat.py
    ```

### Run model on Colab

https://colab.research.google.com/github/gallen881/Physics_Master/blob/master/chat.ipynb

## Additional Function

If want to use WolframAlpha, follow these steps:

1. If don't have a WolframAlpha account, go [here](https://developer.wolframalpha.com/) and create one.
2. Go [here](https://developer.wolframalpha.com/access) and click **Get an App ID**.
3. Enter **Name** and **Description**, then select **Full Results API**.
4. Click **Submit**, then copy the **App ID**.
5. Run `set_keys.py`, then enter your App ID.
    ```
    python set_keys.py
    ```

# 物理大師

物理大師是基於 [unsloth/llama-3-8b-Instruct-bnb-4bit](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) 和 [ArtifactAI/arxiv-physics-instruct-tune-30k](https://huggingface.co/datasets/ArtifactAI/arxiv-physics-instruct-tune-30k) 微調的模型。這裡存放 Python 腳本。模型開源於 [Hugging Face](https://huggingface.co/gallen881/Llama-3-8B-Physics_Master-GGUF)。

## 如何使用？

### 在本地電腦運行

1. clone 這個 repo
    ```
    git clone https://github.com/gallen881/Physics_Master.git
    ```
2. 移動目錄到 `Physics_Master`
    ```
    cd Physics_Master
    ```
3. 安裝依賴
    ```
    pip install -r requirements.txt
    ```
3. 運行 `chat.py`
    ```
    python chat.py
    ```

### 在 colab 上運行

https://colab.research.google.com/github/gallen881/Physics_Master/blob/master/chat.ipynb

## 額外功能

如果想使用 WolframAlpha 的功能，依照以下步驟：

1. 如果沒有 WolframAlpha 帳號，前往[這裡](https://developer.wolframalpha.com/)註冊。
2. 前往[這裡](https://developer.wolframalpha.com/access) 然後點擊 **Get an App ID**。
3. 輸入 **Name** 和 **Description** 然後選擇 **Full Results API**。
4. 點擊 **Submit** 然後複製 **App ID**。
5. 執行 `set_keys.py` 然後輸入你的 App ID。
    ```
    python set_keys.py
    ```