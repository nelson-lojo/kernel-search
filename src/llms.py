from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch

class ModelWrapper:

    def __init__(self):
        raise NotImplementedError(f"ModelWrapper is abstract!")

    def get_response(self, prompt: str):
        raise NotImplementedError(f"ModelWrapper cannot produce responses!") 

class CodeGen7(ModelWrapper):

    def __init__(self):
        self.model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen25-7b-mono")
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen25-7b-mono", trust_remote_code=True)

    def get_response(self, prompt: str, length: int = 128):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=length)
        return self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)

class CodeGen1(ModelWrapper):

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen2-1B")
        self.model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen2-1B", trust_remote_code=True, revision="main")

    def get_response(self, prompt: str, length: int = 128):
        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        generated_ids = self.model.generate(input_ids, max_length=length)
        return self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)

class CodeT5p(ModelWrapper):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5p-2b")
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            "Salesforce/codet5p-2b", 
            torch_dtype=torch.float16, 
            trust_remote_code=True
        )
    
    def get_response(self, prompt: str):
        encoding = self.tokenizer("prompt_text", return_tensors="pt")
        encoding['decoder_input_ids'] = encoding['input_ids'].clone()
        outputs = self.model.generate(**encoding, max_length=-1)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
