import streamlit as st
from gma.genome import Genome

st.title("Genome Motif Analyzer")

uploaded_file = st.file_uploader("Choose a FASTA file")
motif = st.text_input("Enter motif to search")
mismatches = st.slider("Allowed mismatches", 0, 5, 0)

if uploaded_file and motif:
    genome = Genome(uploaded_file)
    genome.load_genome()
    positions = genome.find_motif(motif, max_mismatches=mismatches)
    
    st.write(f"Motif '{motif}' found at positions: {positions}")
    
    if st.button("Visualize"):
        image_path = genome.visualize_motif(motif)
        if image_path:
            st.image(image_path, caption=f"Motif '{motif}' positions plot", use_column_width=True)
