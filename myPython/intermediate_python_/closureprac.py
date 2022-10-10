

def outer_function():
    message = "Hello World!"

    def inner_function():
        return (message)

    return inner_function



call_function = outer_function()  # == inner funtion

print(call_function.__closure__)
# output: (<cell at 0x104e31330: str object at 0x104ddc1b0>,)
