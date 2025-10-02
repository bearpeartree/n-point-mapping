def main():
    gene1 = input("Enter first gene: ")
    gene2 = input ("Enter second gene: ")
    gene3 = input("Enter third gene: ")

    filename = input("Enter filename: ")


    proccessed = process_raw_gametes("inputs/" + filename)
    dist_gene12, dist_gene13, dist_gene23 = gene_mapping(proccessed, gene1, gene2, gene3)

    print_results(gene1, gene2, dist_gene12)
    print_results(gene2, gene3, dist_gene23)
    print_results(gene1, gene3, dist_gene13)



def process_raw_gametes(filename):
    gametes = {}
    with open(filename) as file:
        for  line in file:
            current = line.rstrip("\n").split(" ")
            gametes[current[0]] = int(current[1])
    return gametes


def gene_mapping(gametes, gene1, gene2, gene3):
    sum_recom_gene12 = 0
    sum_recom_gene13 = 0
    sum_recom_gene23 = 0

    total_gametes = 0
    for gamete in gametes:
        total_gametes += gametes[gamete]


    for gamete in gametes:
        result = check_current_gamete(gene1, gene2, gene3, gamete)
        if result[0] == "recombinental":
            sum_recom_gene12 += gametes[gamete]
        if result[1] == "recombinental":
            sum_recom_gene23 += gametes[gamete]
        if result[2] == "recombinental":
            sum_recom_gene13 += gametes[gamete]
    
    distance_gene12 = calc_distance(sum_recom_gene12, total_gametes)
    distance_gene13 = calc_distance(sum_recom_gene13, total_gametes)
    distance_gene23 = calc_distance(sum_recom_gene23, total_gametes)

    return distance_gene12, distance_gene23, distance_gene13
    

def calc_distance(sum_recombs, total):
    return (sum_recombs/total)*100
    

def print_results(gene1, gene2, distance):
    print("Distance between Gene " + gene1 + " and " + gene2 + " : " + str(distance))


def check_current_gamete(gene1, gene2, gene3, current_gamete):

    gene_combo_12 = check_recomb(current_gamete, gene1, gene2)
    gene_combo_13 = check_recomb(current_gamete, gene1, gene3)
    gene_combo_23 = check_recomb(current_gamete, gene2, gene3)

    return (gene_combo_12, gene_combo_13, gene_combo_23)


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