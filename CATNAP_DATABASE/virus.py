
def validate(S):
    AA = ""
    for i in S:
        if ord(i) >= 65 and ord(i) <= 90 and i != 'O':
            AA += i
    return AA        

with open('virseqs_aa.fasta', 'r') as f:
    seq_dict = {}
    current_id = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            seq_dict[current_id] = ""
        else:
            seq_dict[current_id] += line

for i in seq_dict:
    seq_dict[i] = validate(seq_dict[i])
#print(seq_dict['01_AE.CH.x.ZENV32_0111_5.KU600816'])

with open("Virus_aligned_removed.fasta", "w") as f:
    for i in seq_dict:
        head = ">"+i
        f.write(head)
        f.write("\n")
        f.write(seq_dict[i])
        f.write("\n")
    	


