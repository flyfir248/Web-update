with open('Homo sapiens p53 (p53) gene, exon 8 and partial cds.txt') as fh:
    my_file = fh.read()
    
Name = my_file.split('\n')[0][1:]   # extract the name of sequence
seq = ''.join(my_file.split('\n')[1:])   # extract the sequence itself
print('The name is : {0}'.format(Name))
print('The sequence is: {0}'.format(seq))
