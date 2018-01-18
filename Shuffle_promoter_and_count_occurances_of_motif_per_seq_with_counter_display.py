import sys
import re
import random
from random import shuffle



####already did ctrlF replace on this to get rid of slash n so each line is a transcript
t = open('BUXv1.2_all_gene_names.out.300up.fasta', 'r')
out = open("BUX_300up_test_output_1000_times_shuffle.fa","a")
new_data = ""
count = 0
for line in t:
    count = count + 1
    print (str(count))
    #print line
    if line.startswith(">"):
        name = line
        #out.write(line)
    else:
        seq = line
        for z in range(0,1000):
            f = re.findall("[C|G]TATA[T|A]AA[A|G][C|G]", seq)
            r = re.findall("[C|G][T|C]TT[T|A]TATA[C|G]", seq)
            #print (len(f))
            #print (len(r))
            #print (seq)
            #print (len(f)+len(r))
            #print (random.shuffle(seq))
            lists = list(line.rstrip("\n"))
            shuff = random.shuffle(lists)
            seq = ("".join(lists))
            new_data = new_data + str((len(f)+len(r))) + "\t"
        out.write(new_data +name)
        new_data = ""
        
     
out.close()







