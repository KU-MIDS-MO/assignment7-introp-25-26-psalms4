#Write a function:
#build_pipeline(operation_names)
#where operation_names is a list of strings.
#The function must return a new function that applies a sequence of operations to a single input value,in the given order.
#Each string in operation_names represents an operation
#If an unknown operation name is encountered, an error must be raised.
#Calling the returned function should apply all operations sequentially and return the final result.

def build_pipeline(operation_names):
    operations = {
        "add": lambda x: x + 4,
        "sub": lambda x: x - 2,
        "double": lambda x: 2 * x,
        "triple": lambda x: 3 * x,
        "square": lambda x : x ** 2,
        
        }
    pipeline_ops = []
    
    for name in operation_names:
        try:
            pipeline_ops.append(operations[name])
        except KeyError:
            raise KeyError(f"Unknown operations: {name}")
            
    def pipeline(x):
        for op in pipeline_ops:
            x = op(x)
        return x
    return pipeline
    
   
        
    
