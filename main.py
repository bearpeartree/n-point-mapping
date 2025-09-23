def main():
    print(process_raw_gametes("Examples/gametes_example_1.txt"))


# (gamete, count)
def process_raw_gametes(filename):
    gametes = []
    with open(filename) as file:
        for  line in file:
            current = line.rstrip("\n").split(" ")
            gametes.append((current[0], int(current[1])))
    return gametes

if __name__ == "__main__":
    main()