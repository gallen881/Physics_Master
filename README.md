# Physics Master

Physics Master is a model finetuned from [unsloth/llama-3-8b-Instruct-bnb-4bit](https://huggingface.co/unsloth/llama-3-8b-Instruct-bnb-4bit) and [ArtifactAI/arxiv-physics-instruct-tune-30k](https://huggingface.co/datasets/ArtifactAI/arxiv-physics-instruct-tune-30k). Here is the python code. The model is open source on [Hugging Face](https://huggingface.co/gallen881/Llama-3-8B-Physics_Master-GGUF).

# How to use?

1. Clone this repo.
    ```
    git clone https://github.com/gallen881/Physics_Master.git
    ```
2. Move to `Physics_Master`
    ```
    cd Physics_Master
    ```
3. Run `chat.py`.
    ```
    python chat.py
    ```

# Additional Function

If want to use WolframAlpha, follow these steps:

1. If don't have a WolframAlpha account, go [here](https://developer.wolframalpha.com/) and create one.
2. Go [here](https://developer.wolframalpha.com/access) and click **Get an App ID**.
3. Enter **Name** and **Description**, then select **Short Answers API**
4. Click **Submit**, then copy the **App ID**.
5. Run `set_keys.py`, then enter your App ID.
    ```
    python set_keys.py
    ```