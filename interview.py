def find_genes_brute_force(dna):
    genes = ['ACT', 'AGT', 'CGT']

    if not check_if_all_genes_are_present(genes, dna, 0, len(dna)):
        return ''

    best_so_far = len(dna)
    best_start = 0
    best_end = 0

    for start in range(len(dna)):
        for end in range(start + 1, len(dna), 1):
            if check_if_all_genes_are_present(genes, dna, start, end):
                if (end - start) < best_so_far:
                    best_so_far = end - start
                    best_start = start
                    best_end = end

    return dna[best_start:best_end]


def check_if_all_genes_are_present(genes, sample_input, start, end):
    return all(gene in sample_input[start:end] for gene in genes)


if __name__ == '__main__':
    print(find_genes('ACTACGTTTAGTAACTCGTCT'))

