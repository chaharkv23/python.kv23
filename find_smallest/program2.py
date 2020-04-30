def Find_Smallest():
    s = input()
    with open(s, 'r') as f:
        l = len(f.readline())
        f.seek(0)
        smallest = f.readline()
        f.seek(0)
        for i in f:
            if(len(i) < l):
                l = len(i)
                smallest = i
        print(smallest)
Find_Smallest()