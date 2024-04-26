import os
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
import torch

BASE_EXO = """from __future__ import annotations
from exo import proc, DRAM
from exo.stdlib.scheduling import *

# Algorithm definition
@proc
def generated_operation(
    In: i8[16, 16] @ DRAM,
    Weights: i8[16, 16] @ DRAM,
    Out: i8[16, 16] @ DRAM,
):
    for i in seq(0, 16):
        for j in seq(0, 16):
            for k in seq(0, 16):
                Out[i, j] += In[i, k] * Weights[k, j]

# Now we create a schedule to improve performance!
## first switch to "output stationary"
gemmini = rename(generated_operation, "generated_operation_scheduled")
gemmini = reorder_loops(gemmini, "j k")
gemmini = reorder_loops(gemmini, "i k")

## then """


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

def evaluate_out(total_string: str) -> tuple[bool, int]:
    """Returns tuple (correct_code?, num_of_instructions) """

    with open("out.py", "w") as f:
        f.write(total_string)

    success_table = {"PASS\n":True, "FAIL\n":False}

    out = os.popen("/workspaces/project/evaluate_generated.sh 2>&1").readlines()[0]

    if out not in success_table:
        return False, -1
        raise ValueError(f"Unexpected output: {out}")

    is_success = success_table[out]

    if not is_success:
        return is_success, -1
    
    with open("/workspaces/project/log", 'r') as f:
        num_lines = len(f.readlines())

    return is_success, num_lines
