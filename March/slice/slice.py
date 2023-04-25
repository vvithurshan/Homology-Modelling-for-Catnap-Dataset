with open("Virus_aligned_removed.fasta", "r") as f:
	for line in f:
		if line[0] == ">":
			continue
		if "KVV" not in line:
			print(line)