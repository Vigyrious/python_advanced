try:
    with open("text.txt","r") as f:
        print(f"File found")

except FileNotFoundError:
    print("File not found")