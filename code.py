# modelop.schema.0: input_schema.avsc
# modelop.slot.1: in-use


# modelop.init
def begin():
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
