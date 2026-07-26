# Google Colab

1. Install colab-xterm 
```bash
!pip install colab-xterm
%load_ext colabxterm
%xterm
```

2. Install screen and zstd inside xterm
```bash
apt install screen
apt install zstd
```

3. Open screen
```bash
screen
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
# ctrl A, ctrl D - exit the screen
```

4. Download model
```bash
ollama pull gemma4:e4b
# small one 
# ollama pull qwen3.5:4b
```

5. Ollama run
```bash
ollama run gemma4:e4b --verbose
# ollama run qwen3.5:4b --verbose
```

6. To stop
```bash
ollama stop gemma4:e4b
```
7. some settings
```bash
ollama run qwen3.5:4b "Reply with exactly: hello"
```

# Install gradio 


```python
!pip install --upgrade gradio

import gradio as gr
gr.load_chat("http://localhost:11434/v1/", model="qwen3.5:4b", token="ollama").launch(debug=True)
```


# Work with ollama

```python
!pip install -q ollama gradio
import gradio as gr
from ollama import chat

def reply(message, history):
    messages = []

    for user_msg, assistant_msg in history:
        messages.append({"role": "user", "content": user_msg})
        if assistant_msg:
            messages.append({"role": "assistant", "content": assistant_msg})

    messages.append({"role": "user", "content": message})

    stream = chat(
        model="qwen3.5:4b",
        messages=messages,
        think=False,
        stream=True,
        options={"num_ctx": 2048, "num_predict": 256},
    )

    answer = ""
    for chunk in stream:
        answer += chunk["message"]["content"]
        yield answer

gr.ChatInterface(reply).launch()
```


# Copilot local

## Show models
```bash
curl http://127.0.0.1:1234/v1/models
```

```bash
export COPILOT_PROVIDER_BASE_URL=http://127.0.0.1:1234/v1
export COPILOT_PROVIDER_TYPE=openai
export COPILOT_PROVIDER_API_KEY=lm-studio
export COPILOT_MODEL="qwen2.5-0.5b-instruct-mlx"

copilot
```

# Claude 

```bash
export ANTHROPIC_BASE_URL=http://127.0.0.1:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
export CLAUDE_CODE_ATTRIBUTION_HEADER=0

claude --model llama-3.2-1b-instruct
```


```bash
brew install python@3.12
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install gradio openai openai-gradio
```
