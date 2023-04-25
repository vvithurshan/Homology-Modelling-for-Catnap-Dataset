with open('heavy_seqs_aa.fasta', 'r') as f:
    seq_dict = {}
    current_id = ""
    for line in f:
        line = line.strip()
        if line.startswith(">"):
            current_id = line[1:]
            under_score = current_id.find("_")
            current_id = current_id[:under_score]
            seq_dict[current_id] = ""
        else:
            seq_dict[current_id] += line
AB_list = []          
for key in seq_dict:
    AB_list.append(key)
print(len(AB_list))
print(AB_list)


