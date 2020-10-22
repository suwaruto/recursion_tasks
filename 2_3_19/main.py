def Combinations(Set = set()):
    if not Set: return {frozenset()}
    res = {frozenset([element for element in Set])}
    for item in Set:
       res.add(frozenset([element for element in Set - {item}])) 
       res |= Combinations(Set - {item})
    return res

def main():
    s = {1, 2, 3}
    t = {frozenset(s)}
    print(Combinations(s))

if __name__ == "__main__": main()
