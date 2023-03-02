
def moneyChange(x):
    count = 0
    while x > 0:
        if x >= 10:
            count += int(x / 10)
            x = x % 10
        if x >= 5:
            count += int(x / 5)
            x = x % 5
        if x >= 1:
            count += int(x / 1)
            x = x % 1
    return count

def main():
    line = input()
    x = int(line)
    mc = moneyChange(x)
    print(mc)

if __name__ == "__main__":
    main()

