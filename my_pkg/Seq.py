from .map import map as translation_table

class Seq:
	def __init__(self, fasta):
		self.fasta_file = fasta
		
		print('Initializing Seq with ' + self.fasta_file)

		self.id = ""
		self.dna_seq = ""

	def transcribe(self):
		self.rna_seq = "RNA"
		return self.rna_seq

	def translate(self):
		self.pep_seq = "PEPTIDE"
		return self.pep_seq

