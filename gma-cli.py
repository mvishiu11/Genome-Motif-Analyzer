import argparse
from gma.genome import Genome

def main():
    parser = argparse.ArgumentParser(
        description="Welcome to BioSeq Analyzer - your genome analysis assistant!"
    )
    parser.add_argument("file", help="Path to the genome FASTA file.")
    parser.add_argument("-m", "--motif", help="Motif to search for.", required=True)
    parser.add_argument("-n", "--mismatches", type=int, default=0, help="Allow mismatches in motif search.")
    parser.add_argument("-v", "--visualize", action="store_true", help="Visualize motif positions.")
    parser.add_argument("-o", "--output", help="Output file path to save the visualization (e.g., motif_plot.png).")
    
    args = parser.parse_args()

    genome = Genome(args.file)
    genome.load_genome()

    if args.motif:
        positions = genome.find_motif(args.motif, max_mismatches=args.mismatches)
        print(f"Motif '{args.motif}' with {args.mismatches} mismatches found at positions: {positions}")
        if args.visualize and args.output:
            genome.visualize_motif(args.motif, output_path=args.output)
        elif args.visualize:
            genome.visualize_motif(args.motif)
    else:
        print("Please provide a motif to search for. Use --motif.")

if __name__ == "__main__":
    main()
