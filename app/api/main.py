from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pre_built_models.TuringMachines import BinaryTuringMachine

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

@app.post("/name/{text}")
async def get_binary_format(text:str):
    # Initialize the model
    model= BinaryTuringMachine()
    # Iterate along the characters
    output= ""
    for c in text:
        unary_n= "1" * ord(c)
        accepted= int(model.is_accepted(unary_n))
        binary_str= "not_accepted"
        if accepted:
            binary_str= model.get_tape()
        # Add binary string to output
        output+= binary_str + " "
    # Remove the last space
    output= output[:-1]
    # Return binary string
    return {"code":200, "output":output}
