from io import StringIO
from Bio import SeqIO
from collections import defaultdict
import matplotlib.pyplot as plt
from gma.utils import hamming_distance
import os

class Genome:
    """A class to represent a genome and perform motif analysis.

    Attributes:
        genome_source (str): File-like object of the genome FASTA file.
        genome_sequence (str): Loaded DNA sequence.
        motif_positions (dict): Dictionary to store motif positions.

    Methods:
        load_genome(): Loads the genome from a FASTA file.
        find_motif(motif: str, max_mismatches: int = 0): Finds motif in the genome.
        count_motif(motif: str): Counts the occurrences of a motif.
        visualize_motif(motif: str): Visualizes the positions of the motif.
    """
    
    def __init__(self, genome_source):
        """Initializes Genome class with a given file-like object or path."""
        self.genome_source = genome_source
        self.genome_sequence = None
        self.genome_name = None
        self.motif_positions = defaultdict(list)

    def load_genome(self) -> None:
        """Loads the genome sequence from a file-like object or path."""
        try:
            if hasattr(self.genome_source, 'read'):
                fasta_content = self.genome_source.read().decode('utf-8')
                fasta_io = StringIO(fasta_content)
                self.genome_sequence = str(SeqIO.read(fasta_io, "fasta").seq)
                self.genome_name = os.path.basename(self.genome_source.name).split(".")[0]
            else:
                with open(self.genome_source, "r") as file:
                    for record in SeqIO.parse(file, "fasta"):
                        self.genome_sequence = str(record.seq)
            
            print(f"Loaded genome. Sequence length: {len(self.genome_sequence)}")
        except Exception as e:
            raise Exception(f"Error loading genome: {str(e)}")

    def find_motif(self, motif: str, max_mismatches: int = 0) -> list:
        """Finds the motif in the genome with optional mismatches.
        
        Args:
            motif (str): The motif to search for.
            max_mismatches (int): Maximum allowed mismatches for approximate matches.
        
        Returns:
            list: List of positions where the motif was found.
        """

        self.motif_positions[motif] = []
        for i in range(len(self.genome_sequence) - len(motif) + 1):
            subseq = self.genome_sequence[i:i+len(motif)]
            if hamming_distance(subseq, motif) <= max_mismatches:
                self.motif_positions[motif].append(i)
        return self.motif_positions[motif]

    def count_motif(self, motif: str) -> int:
        """Counts the occurrences of a motif in the genome.
        
        Args:
            motif (str): The motif to count.
        
        Returns:
            int: Number of occurrences.
        """
        return len(self.motif_positions.get(motif, []))

    def visualize_motif(self, motif: str, output_path: str = None) -> None:
        """Visualizes the motif positions on the genome sequence."""
        positions = self.motif_positions.get(motif, [])
        if not positions:
            print(f"No occurrences of motif '{motif}' found.")
            return
        plt.figure(figsize=(10, 2))
        plt.plot(positions, [1] * len(positions), 'ro')
        plt.yticks([])
        plt.title(f"Motif '{motif}' positions in genome {self.genome_name}")
        plt.xlabel("Position")
        if not output_path:
            output_path = os.path.join("visualizations", f"{self.genome_name}_{motif}_plot.png")
        plt.savefig(output_path)
        plt.close()
        return output_path
