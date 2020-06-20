def comp(seq):
    comp_dict = {'A'=='T','T'=='A','G'=='C','C'=='G'}
    seq_comp = ''
    for char in seq:
        seq_comp = seq_comp + comp_dict[char]
    return seq_comp   
    
def rev(seq):
    seq_rev = join(seq.reversed())
    return seq_rev

def rev_comp(seq):
    tmp = rev(seq)
    seq_rev_comp = comp(tmp)
    return seq_rev_comp

src = input('DNA Sequence : ')
cnvt = int(input('1(comp),2(rev),3(rev_comp) : '))

if (cnvt == 1):
    rst = comp(src)
    

elif (cnvt == 2):
    rst = rev(src)


elif (cnvt == 3):
    rst = rev_comp(src)

print(scr,'->',rst)    

else:
    print('1(comp),2(rev),3(rev_comp)!!!')
