import os
# from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
# import torch

def generate_out():
    ...

def evaluate_out() -> tuple[bool, int]:
    """Returns tuple (correct_code?, num_of_instructions) """
    success_table = {"PASS\n":True, "FAIL\n":False}

    out = os.popen("/workspaces/project/evaluate_generated.sh").readlines()[0]

    if out not in success_table:
        raise ValueError(f"Unexpected output: {out}")

    is_success = success_table[out]

    if not is_success:
        return is_success, -1
    
    with open("/workspaces/project/log", 'r') as f:
        num_lines = len(f.readlines())

    return is_success, num_lines


def do_codegen7(prompt_text: str):
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen25-7b-mono", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen25-7b-mono")

    input_ids = tokenizer(prompt_text, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=128)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)

def do_codegen1(prompt_text: str, length: int = 128):
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen2-1B")
    model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen2-1B", trust_remote_code=True, revision="main")
    input_ids = tokenizer(prompt_text, return_tensors="pt").input_ids
    generated_ids = model.generate(input_ids, max_length=length)
    return tokenizer.decode(generated_ids[0], skip_special_tokens=True)

def do_codet5p(prompt_text: str, device: str = "cpu") -> tuple:
    tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5p-2b")
    model = AutoModelForSeq2SeqLM.from_pretrained("Salesforce/codet5p-2b",
                                                  torch_dtype=torch.float16,
                                                  trust_remote_code=True)

    encoding = tokenizer("prompt_text", return_tensors="pt").to(device)
    encoding['decoder_input_ids'] = encoding['input_ids'].clone()
    outputs = model.generate(**encoding, max_length=-1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
