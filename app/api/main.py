from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from my_models.preBuiltModels import BinaryTuringMachine
from my_models.preBuiltModels import OperationValidatorNFA

# Initialize the model
turingMachine = BinaryTuringMachine()
nfa = OperationValidatorNFA()

# Input template
class Item(BaseModel):
    cadena: str

app= FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"Hello": "World"}

# Turing Machine Request
@app.post("/TuringMachine/{text}")
async def get_binary_format(item: Item):
    text= item.cadena
    # Iterate along the characters
    output= ""
    for c in text:
        unary_n= "1" * ord(c)
        accepted= int(turingMachine.is_accepted(unary_n))
        binary_str= "not_accepted"
        if accepted:
            binary_str= turingMachine.get_tape()
        # Add binary string to output
        output+= binary_str + " "
    # Remove the last space
    output= output[:-1]
    # Return binary string
    return {"code":200, "output":output}

# NFA Request
@app.post("/NFA/{text}")
async def get_binary_format(item: Item):
    text= item.cadena
    output= "Invalida Operation"
    if nfa.is_accepted(text):
        output= "Valid Operation"

    return {"code":200, "output":output}
