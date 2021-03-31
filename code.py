# modelop.schema.0: input_schema.avsc
# modelop.slot.1: in-use


# modelop.init
def begin(model_def):
    
    print("\nModel Definition keys: \n", flush=True)
    print(model_def.keys(), flush=True)
    
    if 'job' in model_def.keys():
        print(model_def['job'], flush=True)
    
    elif 'deployedModel' in model_def.keys():
        print(model_def['deployedModel'], flush=True)
    
    pass

# modelop.score
def action(data):
    """
    param: data: dict of he form {"input": x} for some number x
    """
    
    print("action input: ", data, flush=True)
    
    num = data["input"]
    
    print("num: ", num, flush=True)
    
    out = {
        "reciprocal": 1/num
    }
    
    print("output: ", out, flush=True)


    yield out
