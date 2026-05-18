from llama_cpp import Llama



def main():
    # ggml-org/gemma-4-26B-A4B-it-GGUF
    # Give a simple hello world example with gemma4 ggml-org/gemma-4-26B-A4B-it-GGUF
    model_path = "ggml-org/gemma-4-26B-A4B-it-GGUF"
    llm = Llama(model_path=model_path)
    prompt = "What is the capital of France?"
    response = llm(prompt)
    print(response)

if __name__ == '__main__':
    main()