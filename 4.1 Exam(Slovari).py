dnk = 'ACTG'
my_dict_rnk ={'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
print(*[my_dict_rnk[key] for key in dnk], sep='')


text = input()
result = {}
spisok = []
for i in text.split():
    result[i] = result.get(i, 0) + 1
    spisok.append(str(result[i]))
print(*spisok)

slovo = 'DANSER'
total = 0
my_dict = {
    1: "AEILNORSTU",
    2: "DG",
    3: "BCMP",
    4: "FHVWY",
    5: "K",
    8: "JX",
    10: "QZ"
}
for key in slovo:
    for j in my_dict:
        if key in my_dict[j]:
            total += j
print(total)
   
        
def build_query_string(params):
    return '&'.join([f'{key}={value}' for key, value in sorted(params.items())])
    
print(build_query_string({'name': 'timur', 'age': 28}))


def merge(value):
    result = {}
    for i in value:
        for key  in i:
            result.setdefault(key, set()).add(i[key])
    return result  



result = {}
dict_operations = {'W': 'write', 'R': 'read', 'X': 'execute'}
for _ in range(int(input())):
    x = input().split()
    result[x[0]] = [dict_operations[i] for i in x[1:]]
               
for _ in range(int(input())):
    x = input().split()
    if  x[0] in result[x[1]]:
        print('OK')
    else:
        print('Access denied')
   
    

result = {}
for _ in range(int(input())):
    name,product, count = input().split()
    result.setdefault(name, {})
    result[name][product] = result[name].get(product, 0)+ int(count)
    
for key, value in sorted(result.items()):
    print(f'{key}:')
    for i in sorted(value):
        print(i, value[i])