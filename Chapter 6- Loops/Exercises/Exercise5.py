sandwich_orders = [
    'pastrami','chicken sandwich', 'pastrami','beef sandwich', 'cheese sandwich', 'pastrami'
    ]
done_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    sandwiches = sandwich_orders.pop()
    print(f"I'm working on your {sandwiches} sandwich.")
    done_sandwiches.append(sandwiches)

print("\n")
for sandwich in done_sandwiches:
    print(f"I made a {sandwich} sandwich.")    
