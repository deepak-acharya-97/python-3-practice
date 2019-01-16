def result(mark):
    return mark > 40

result_14IT201=all(result(m) for m in [41,42,51,30,33])
result_14IT201_dash=any(result(m) for m in [41,42,51,30,33])
print(result_14IT201,result_14IT201_dash)