for i in range(1, 200):
    if i % 5 == 2 and i % 6 == 3 and i % 7 == 2:
        print("The jar contains", i, "pieces of candy.")
        break
else:
    print("No solution found within the given range.")