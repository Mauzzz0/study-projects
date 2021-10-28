def gematri(sequence):
    sequence = [x.lower() for x in sequence]
    # Если не углубляться в нумерологию, то сортировка по гематрию является ни чем иным, как лексикографическим порядком
    # Поэтому вот ;)
    print(*sorted(sequence), sep="\n")
