def main():
    print(process_raw_gametes("Examples/gametes_example_1.txt"))


def process_raw_gametes(filename):
    gametes = {}
    with open(filename) as file:
        for  line in file:
            current = line.rstrip("\n").split(" ")
            gametes[current[0]] = int(current[1])
    return gametes


# TODO
def identify_parent_or_combo(gametes):
    pass


# TODO
def helper_id(gene1, gene2, gene3, current_gamete):
    genes12 = []
    genes13 = []
    genes23 = []

    check_recomb(current_gamete, gene1, gene2)
    check_recomb(current_gamete, gene1, gene3)
    check_recomb(current_gamete, gene2, gene3)



def check_recomb(gamete, first_gene, second_gene):
    splitted_genes = gamete.split("/")
    cp_splitted_genes = splitted_genes.copy()
    recomb = []
    for i in range(0, len(cp_splitted_genes)):
        if '+' in cp_splitted_genes[i]:
            cp_splitted_genes[i] = cp_splitted_genes[i].replace('+','')
        if cp_splitted_genes[i] == first_gene or cp_splitted_genes[i] == second_gene:
            recomb.append(splitted_genes[i])
    
    if ('+' in recomb[0] and '+' in recomb[1]) or '+' not in recomb[0] and '+' not in recomb[1]:
        return "parental"
    else:
        return "recombinental"


if __name__ == "__main__":
    main()