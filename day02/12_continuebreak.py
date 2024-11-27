for i in range(1,101):
    if i%2==0:
        continue
    print(f"i={i}")

for j in range(1,101):
    if j%2==0:
        break
    print(f"j={j}")