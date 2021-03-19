# modelop.slot.0: in-use
# modelop.slot.1: in-use


# modelop.init
def begin():
    pass

# modelop.score
def action(data):
    yield {
        "reciprocal": 1/data
    }
