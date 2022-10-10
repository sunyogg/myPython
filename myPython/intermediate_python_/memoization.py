import time

ef_cache = {}
def expensive_func(num):
    if num in ef_cache:
        return ef_cache[num]

    print("Computing {}...".format(num))
    time.sleep(1)
    result = num * num
    ef_cache[num] = result
    return result

s = expensive_func(3)
print(s)

a = expensive_func(5)
print(a)

s = expensive_func(3)
print(s)

a = expensive_func(5)
print(a)