def F(x: list,y: int) -> int:
    res = sum(k for k in range(1,y+1) if k not in x)
    return res
print(F([2,5,6],10))