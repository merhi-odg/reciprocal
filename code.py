# modelop.slot.0: in-use
# modelop.slot.1: in-use


import time

# modelop.init
def begin():
    
    print("\nWaiting 15s before erroring out init function\n", flush=True)
    
    time.sleep(15)
    
    print("\nErroring out init on purpose. Model should not get deployed!\n", flush=True)
    print(1/0)
    
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
