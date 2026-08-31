answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip()
normalized = answer.lower().replace("-", " ")

if normalized == "42" or normalized == "forty two":
    print("Yes")
else:
    print("No")
