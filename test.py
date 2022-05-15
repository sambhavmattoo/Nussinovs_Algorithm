String = "AUGCGCGGGAUCGUCGAGAU"

nm = [[0 for j in range(0, len(String))] for i in range(0, len(String))]

for j in range(1, len(String)):
    for i in range(j - 1, -1, -1):
        if (String[i], String[j]) == ('A', 'U') or (String[i], String[j]) == ('U', 'A') or (String[i], String[j]) == ('G', 'C') or (String[i], String[j]) == ('C', 'G'):
        
            if j - i > 1:
                pop = 0
                for k in range(i+1, j):
                    pop = max(pop,nm[i][k] + nm[k+1][j])
                nm[i][j] = max(nm[i+1][j-1] + 1, nm[i+1][j], nm[i][j-1], pop)
            else:
                nm[i][j] = max(nm[i+1][j-1] + 1, nm[i+1][j], nm[i][j-1])
                
        else:
            
            if j - i > 1:
                pop = 0
                for k in range(i+1, j):
                    pop = max(pop, nm[i][k] + nm[k+1][j])
                nm[i][j] = max(nm[i+1][j-1], nm[i+1][j], nm[i][j-1], pop)
            else:
                nm[i][j] = max(nm[i+1][j-1], nm[i+1][j], nm[i][j-1])
    

for i in range(0, len(String)):
    print(nm[i])