#Ask the user to enter marker and DNA sequence
DNA_Sequence=input('Enter a DNA Sequence: ')
Pattern=input('Enter the pattern: ')
#split the DNA_Sequence to before and after the index of the pattern
A=DNA_Sequence.split(Pattern)
# The prefix is A[0]
Prefix=A[0]
print('Prefix ',Prefix)
# get the reversed marker and split A[1] based on it
Reversed_Marker=Pattern[::-1]
B=A[1].split(Reversed_Marker)
# the middle = B[0] and the suffix = b[1]
Middle=B[0]
Reversed_Middle=Middle[::-1]
Suffix=B[1]
print ('Marker:',Pattern)
print ('Middle:',Middle)
print ('Reversed Middle:',Reversed_Middle)
print ('Reversed Marker:',Reversed_Marker)
print ('Suffix:',Suffix)
Result=Prefix+Pattern+Reversed_Middle+Reversed_Marker+Suffix
print ('Result:',Result)
