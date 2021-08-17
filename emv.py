cost = float(input("ต้นทุน: "))
prof = float(input("จำหน่าย: "))
choice = float(input("เลหลัง: "))
prod = list(map(float,input("อัตราการผลิต: ").split(" ")))
freq = list(map(float,input("ความถี่: ").split(" ")))
arr = [[] for i in range(len(prod))]
profit = []
def emv(n, frequency, arr):
    total = 0
    print("\nEMV {}".format(n + 1))
    freq = []
    for i in range(len(frequency)):
        freq.insert(i,(frequency[i] / sum(frequency)))

    for i in range(len(arr)):
        result_emv = arr[i][n] * freq[i]
        total += result_emv
        print("{}    {}    {} \n".format((arr[i][n]), freq[i], result_emv))
    print("รวม = ", total)
    return total
    

print()
for i in range(len(prod)):
    for j in range(len(prod)):
        if(prod[i] < prod[j]):
            result = ((prod[i] * prof) - (prod[j] * cost)) + ((prod[j] - prod[i]) * choice)
            arr[i].append(result)
            print("| ({} * {}) - ({} * {}) + ({} * {}) = {} ".format(prod[i], prof, prod[j], cost, (prod[j] - prod[i]), choice, result), end="")
        if(prod[i] > prod[j]):
            result = ((prod[j] * prof) - (prod[j] * cost))
            arr[i].append(result)
            print("| {} ".format(result), end="")
        if(prod[i] == prod[j]):
            result = ((prod[i] * prof) - (prod[j] * cost))
            arr[i].append(result)
            print("| {} - {} = {} ".format((prod[i] * prof), (prod[j] * cost), result), end="")
    print("\n")

for i in range(len(prod)):
    profit.append(emv(i, freq, arr))
    
print("\nกำไรที่มากที่สุดคือ : " , max(profit), " ควรเลือก : ", prod[profit.index(max(profit))])







            
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               