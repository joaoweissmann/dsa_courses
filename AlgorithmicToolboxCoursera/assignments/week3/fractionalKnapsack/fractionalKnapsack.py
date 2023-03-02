
def fractionalKnapsack(n, w, items):
    items.sort(key = lambda x: x[2], reverse=True)
    fitness = 0
    wUse = 0
    for el in items:
        if int(wUse) >= w:
            break
        else:
            alpha = min(el[1], w - wUse)
            fitness += alpha * el[2]
            wUse += alpha
    return fitness

def main():
    line = input()
    n = int(line.split()[0])
    w = int(line.split()[1])
    items = []
    for i in range(n):
        line = input()
        ci = int(line.split()[0])
        wi = int(line.split()[1])
        items.append([ci, wi, ci/wi])
    fitness = fractionalKnapsack(n, w, items)
    print(round(fitness, 4))

if __name__ == "__main__":
    main()

