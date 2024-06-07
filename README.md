# End-to-end-Medical-Chatbot-using-Llama-2

# How to run?
clone the repository 
```bash
Project repot : https://github.com/Abdoul1996/End-to-end-Medical-Chatbot-using-Llama-2
```
### STEP 01- Create a conda environment after opening the repository 

```bash
conda create -n mchatbot python=3.8 -y 
```
```bash
conda activate mchatbot 
```

### STEP 02 Install the requirement
```bash
pip install -r requirement.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows: 
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxx"
OPENAI_API_KEY ="xxxxxxxxxxxxxxx"
```

## Download the Llama 2 Model: 

llama-2-7b-chat.ggmlv3.q4_0.bin

## From https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML



