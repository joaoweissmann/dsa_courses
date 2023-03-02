
def carFueling(d, m, n, stops):
    nRefs = 0
    currM = m
    currD = 0
    count = 0
    stops.append(d)
    n += 1
    while (count < n):
        # consigo chegar na próxima parada com tanque cheio?
        #print ("nRefs:", nRefs)
        #print ("currM:", currM)
        #print ("currD:", currD)
        #print ("count:", count)
        #print ("stop distance:", stops[count])
        if (stops[count] - currD) <= m:
            # preciso reabastecer?
            if (stops[count] - currD) > currM:
                # reabastecer 
                nRefs += 1
                currM = m - (stops[count] - currD)
                currD += (stops[count] - currD)
                count += 1
            else:
                # não precisa reabastecer
                currM -= (stops[count] - currD)
                currD += (stops[count] - currD)
                count += 1
        else:
            return -1
    return nRefs

def main():
    d = int(input())
    m = int(input())
    n = int(input())
    stops = []
    line = input()
    for el in line.split():
        stops.append(int(el))
    #print ("d:", d)
    #print ("m:", m)
    #print ("n:", n)
    #print ("stops:", stops)
    nRefs = carFueling(d, m, n, stops)
    print(nRefs)

if __name__ == "__main__":
    main()

