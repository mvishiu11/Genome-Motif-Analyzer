import pytest
from gma.genome import Genome

def test_load_genome():
    genome = Genome("test.fasta")
    genome.load_genome()
    assert len(genome.genome_sequence) > 0

def test_find_motif():
    genome = Genome("test.fasta")
    genome.load_genome()
    positions = genome.find_motif("ATG")
    assert isinstance(positions, list)
    assert len(positions) > 0

def test_count_motif():
    genome = Genome("test.fasta")
    genome.load_genome()
    genome.find_motif("ATG")
    count = genome.count_motif("ATG")
    assert count > 0
