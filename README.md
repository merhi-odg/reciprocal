# reciprocal

This repo serves a test model for MOC runtime features and functionalities.

## Tests to run using this model

**Batch Scoring Jobs** with inputs:

1. `input_div_by_zero.json`
    - schema checking **enabled**
    - Expect `UserWarning("Bad Input: DivisionByZero Expected!")` (2x)

2. `input_bad_data_types.json`
    - schema checking **disabled**
    - Expect `UserWarning("Bad Input: input data should be a dictionary")` (2x)

3. `input_bad_keys.json`
    - schema checking **disabled**
    - Expect `warnings.warn("Key 'input' missing from input data", category=UserWarning)` (2x)

In each of the cases above, the job should **complete** (`"jobStatus": "COMPLETE"`) with **failure** (`"jobResult": "FAILURE"`)