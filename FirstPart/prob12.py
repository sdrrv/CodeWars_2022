def most_frequent(List):
    res = []
    hg = 0
    
    setter = list(set(List))
    for i in setter:
        x = setter.count(i)
        if hg < x:
            hg = x
            res = [i]
        elif hg == x:
            res.append(i)
    return res
    
res = []

ins = input("")
lister = ins.split(",")

most = most_frequent(lister)

for i in lister:
    if i not in most:
        res.append
        
print(most)