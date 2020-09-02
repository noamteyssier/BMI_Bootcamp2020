from my_pkg import Seq

obj = Seq('sequence.fa')
print(obj.id)
print(obj.dna_seq)
print(obj.transcribe())
print(obj.translate())
