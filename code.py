# modelop.slot.0: in-use
# modelop.slot.1: in-use


# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    """
    param: data: dict of he form {"input": x} for some number x
    """
    
    num = data["input"]
    
    yield {
        "reciprocal": 1/num
    }
