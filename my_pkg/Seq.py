from .map import map as translation_table

class Seq:
	## This function should read in a 1-sequence fasta file
	## and then store the Fasta ID and sequence as instance variables
	def __init__(self, fasta):
		self.fasta_file = fasta
		
		print('Initializing Seq with ' + self.fasta_file)

		self.id = ""
		self.dna_seq = ""

	##This function should store the transcribed dna sequence as an instance variable
	## and then return the result
	def transcribe(self):
		self.rna_seq = ""
		return self.rna_seq

	## This function should store the translated peptide as an instance variable
	## and then return the result 
	def translate(self):
		self.pep_seq = ""
		return self.pep_seq
