Input = [(12.121, 'Geeksforgeeks is best'),
         (19212.22, 'India is best'),
         (12.121, 'Cyware is best.'),
         (923232.2323, 'Jiit is best')]
visited = set()
Output = []
for a, b in Input:
    if a not in visited:
        visited.add(a)
        Output.append((a, b))
print(Output)