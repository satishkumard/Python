
# ----------------------------------------------------------------------------------------------------------------------
# Name: Satish Dandayudhapani
# Class: 603-02 Found. Software Dev-Python
# File: gene.py
# [H6-4] (gene.py) Write a program that reads a string from the user.  This string represents a DNA molecule as a
# sequence of letters A, C, G, and T, each letter representing a different base. Then determine whether it represents a
# potential gene, if it satisfies the following 4-part codon criteria:
# •	It begins with the start codon ATG.
# •	Its length is a multiple of 3.
# •	It ends with one of the stop codons TAG, TAA, or TGA.
# •	It has no intervening stop codons, anywhere in the codon sequence between the first and last codons.
# Do so by defining a Boolean function is_gene(dna) that returns True when dna is valid DNA and it satisfies each of the
# codon criteria.
# Also define a Boolean function is_valid_DNA(seq) that returns True if each character in seq is one of A, C, G, or T.
# Otherwise return False.
# Then complete your program: use your is_valid_DNA(seq) function to validate the input string seq's contents, printing
# Not valid DNA if it contains any characters other than one of A, C, G, and T. Otherwise, check it via your is_gene()
# function and print Is potential gene if it satisfies the previous 4-part codon criteria, and Is NOT potential gene
# otherwise.
# Finally, if the input string is not valid DNA or violates the 4-part codon criteria, print out some kind of diagnostic
#  information that describes details on why it's not valid.  This information might describe why the contents are
# invalid DNA, such as which bases are illegal and at what sequence position they occur. For the 4-part codon criteria,
# it might be a description such as "Doesn't start with ATG" or "Length isn't a multiple of 3", and so forth. I will
# award up to 1 point of Extra Credit for diagnostic output that is so detailed and nicely formatted.
# ----------------------------------------------------------------------------------------------------------------------


def is_gene(dna):
    """Function to check the given DNA is potential gene by satisfying the codon criteria"""
    return dna[:3] == "ATG" and len(dna) % 3 == 0 and dna[-3:] in ("TAG", "TAA", "TGA") and "TAG" not in dna[3:-3] \
           and "TAA" not in dna[3:-3] and "TGA" not in dna[3:-3]


def is_valid_dna(seq, set):
    """Function to check if it is a valid DNA"""
    for chr in set:
        if chr not in seq:
            return False
    return True


def is_diag(dna):
    """Capturing the reasons for not being a potential gene."""
    result = ["Below are the violations for not being a potential gene: "]
    if dna[:3] != "ATG":
        result.append("The start condon does not begin with ATG.")
    if len(dna) % 3 != 0:
        result.append("The length of molecule is not a multiple of 3.")
    if dna[-3:] not in ("TAG", "TAA", "TGA"):
        result.append("The molecule does not end with one of the stop condon TAG, TAA, or TGA.")
    if "TAG" in dna[3:-3] or "TAA" in dna[3:-3] or "TGA" in dna[3:-3]:
        result.append("It has intervening stop condon between the first and last condon.")
    return result


def main():
    dna = input("Enter the DNA molecule: ")
    set = ["A", "C", "G", "T"]
    if is_valid_dna(dna, set):
        if is_gene(dna):
            print("%s dna is a potential gene." % dna)
        else:
            print("%s dna is NOT a potential gene." % dna)
            print()
    else:
        print()
        print("%s molecule is not a valid DNA." % dna)
        print("%s violates DNA molecule by representing a base other than A, C, G, T." % dna)
        print()

    result = is_diag(dna)
    if len(result) > 1:
        lineNumber = 1
        print(result[0])
        for number in range(1, len(result)):
            print(str(lineNumber) + '. ' + result[number])
            lineNumber += 1


if __name__ == "__main__":
    main()
