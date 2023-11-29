sandwich_orders = ['chicken sandwich', 'beef sandwich', 'cheese sandwich']
done_sandwiches = []

while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I'm working on your {sandwiches} sandwich.")
    done_sandwiches.append(sandwiches)

print("\n")
for sandwich in done_sandwiches:
    print(f"I made a {sandwich} sandwich.")  
