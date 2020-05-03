class Codon:
    def __init__(self, amino_acid, codons):
        self.codons = codons
        self.amino_acid = amino_acid


Ala = Codon('Ala', ['GCG', 'GCA', 'GCC', 'GCT'])
Cys = Codon('Cys', ['TGC', 'TGT'])
Asp = Codon('Asp', ['GAC', 'GAT'])
Glt = Codon('Glt', ['GAG', 'GAA'])
Phe = Codon('Phe', ['TTC', 'TTT'])
Gly = Codon('Gly', ['GGG', 'GGA', 'GGC', 'GGT'])
His = Codon('His', ['CAC', 'CAT'])
Ile = Codon('Ile', ['ATA', 'ATC', 'ATT'])
Lys = Codon('Lys', ['AAG', 'AAA'])
Leu1 = Codon('Leu1', ['TTG', 'TTA'])
Leu2 = Codon('Leu2', ['CTG', 'CTA', 'CTC', 'CTT'])
Met = Codon('Met', ['ATG']) # 起始密码子
Asn = Codon('Asn', ['AAC', 'AAT'])
Pro = Codon('Pro', ['CCG', 'CCA', 'CCC', 'CCT'])
Gln = Codon('Gln', ['CAG', 'CAA'])
Arg1 = Codon('Arg1', ['CCG', 'CGA'])
Arg2 = Codon('Arg2', ['CGC', 'CGT', 'AGG', 'AGA'])
Ser1 = Codon('Ser', ['AGC', 'AGT'])
Ser2 = Codon('Ser', ['TCG', 'TCA', 'TCC', 'TCT'])
Thr = Codon('Thr', ['ACG', 'ACA', 'ACC', 'ACT'])
Val = Codon('Val', ['GTG', 'GTA', 'GTC', 'GTT'])
Trp = Codon('Trp', ['TGG'])
Tyr = Codon('Tyr', ['TAC', 'TAT'])
codons = [Ala, Cys, Asp, Glt, Phe, Gly, His, Ile, Lys, Leu1, Leu2, Met, Asn, Pro, Gln, Arg1, Arg2, Ser1, Ser2, Thr, Val, Trp, Tyr]

# codons = np.array([['Ala', 'GCG', 'GCA', 'GCC', 'GCT'],
#                    ['Cys', 'TGC', 'TGT'],
#                    ['Asp', 'GAC', 'GAT'],
#                    ['GlT', 'GAG', 'GAA'],
#                    ['Phe', 'TTC', 'TTT'],
#                    ['Gly', 'GGG', 'GGA', 'GGC', 'GGT'],
#                    ['His', 'CAC', 'CAT'],
#                    ['Ile', 'ATA', 'ATC', 'ATT'],
#                    ['Lys', 'AAG', 'AAA'],
#                    ['LeT', 'TTG', 'TTA', 'CTG', 'CTA', 'CTC', 'CTT'],
#                    ['Met', 'ATG'],
#                    ['Asn', 'AAC', 'AAT'],
#                    ['Pro', 'CCG', 'CCA', 'CCC', 'CCT'],
#                    ['Gln', 'CAG', 'CAA'],
#                    ['Arg', 'CCG', 'CGA', 'CGC', 'CGT', 'AGG', 'AGA'],
#                    ['Ser', 'TCG', 'TGA', 'TCC', 'TCT', 'AGC', 'AGT'],
#                    ['Thr', 'ACG', 'ACA', 'ACC', 'ACT'],
#                    ['Val', 'GTG', 'GTA', 'GTC', 'GTT'],
#                    ['Trp', 'TGG'],
#                    ['Tyr', 'TAC', 'TAT'],
#                    ['Start', 'ATG', 'ATA', 'ATC', 'ATT'],
#                    ['Stop', 'TAA', 'TAG', 'AGA', 'AGG']])
