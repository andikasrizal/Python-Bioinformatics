<!-- Banner Header -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff6b6b,100:1e3c72&height=220&section=header&text=Python%20Bioinformatics&fontSize=36&fontColor=ffffff&animation=fadeIn" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue.svg?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Library-Biopython-green.svg?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Course-Undergraduate-orange.svg?style=for-the-badge" />
</p>

<p align="center">
  <b>Exploring biological data programmatically with Python & Biopython</b>
</p>

---

## 🧬 Python Bioinformatics – Academic Practice Repository

This repository contains **Python and Biopython programs** developed as part of my
**first-semester undergraduate coursework** for the subject
**Introduction to Biological Data / Biological Systems**.

The focus of this repository is on **fundamental bioinformatics tasks**
implemented using Python, with an emphasis on **biological sequence analysis,
data handling, and visualization**.

---

## 📘 Academic Context

* **Course**: Introduction to Biological Data / Biological Systems
* **Level**: Undergraduate (First Semester)
* **Purpose**: To gain hands-on experience in applying programming concepts
  to biological sequence data and basic bioinformatics workflows.

---

## 🧬 Topics Covered

### 🔹 Biological Sequence Analysis (Python)

* Reverse complement of DNA sequences
* DNA → RNA transcription
* RNA → Protein translation
* Counting individual nucleotides (A, T, G, C)
* Percentage composition of nucleotides
* Processing sequences from input files

### 🔹 Biopython

* Sequence manipulation using Biopython
* Reading biological sequences from files
* Performing transcription and translation using Biopython utilities
* Counting number of sequences in an input file
* Nucleotide frequency analysis across multiple sequences

### 🔹 Data Handling & Analysis

* Reading sequence data from text and FASTA files
* Working with tabular data using **pandas**
* Organizing biological data for downstream analysis

### 🔹 Visualization

* Line plots for biological data
* Scatter plots for sequence-related analysis
* Basic visualization using **Matplotlib**

---

## 🛠️ Tools & Libraries Used

* **Python 3**
* **Biopython**
* **pandas**
* **NumPy**
* **Matplotlib**
* **RDKIT**

---

## 📁 Repository Structure

The full directory structure is shown below:

```
Python-BioInformatics/
├── sequences/
│   ├── manual-transcription.py
│   ├── transcription-biopython.py
│   ├── fasta-to-dna-mrna-protein-sequences.py
│   ├── fasta-to-protein-sequence.py
│   ├── file-translation-to-stop-at-codon.py
│   ├── stop-at-logic-for-translation.py
│   ├── central-dogma-of-biology.py
│   ├── translation-to-stop-at-codon.py
│   ├── manual-translation.py
│   ├── purine-pirimidine-translation.py
│
├── complements/
│   ├── complement-and-reverse_complement.py
│   ├── complement-reverse_complement.py
│   ├── complement-reverse_complement-from-sequence.py
│
├── statistics/
│   ├── length-of-sequence.py
│   ├── nucleotide-count-from-file.py
│   ├── nucleotide-count-and-length-of-sequence.py
│   ├── nucleotide-count-from-file-plot.py
│
├── file_handling/
│   ├── sequence-conversions-from-file.py
│   ├── multiple-files-to-sequeces.py
│
├── medical_imaging/
│   ├── displaying-dicom-file.py
│   ├── reading-info-from-dicom-file.py
│
├── cheminformatics/
│   ├── smiles-to-png-with-atom-numbers.py
│   ├── Smiles2image-using-RDKIT.py
│   ├── descriptors-from-smiles.py
│   ├── smiles2png-with-atomnumbers.py
│   ├── smiles-to-pdb-hydrogen.py
│   ├── smiles-to-descriptors-RDKIT.py
│   ├── smiles-to-morganfingerprint.py
│   ├── smile-descriptors-to-aromaticity.py
│   ├── smiles-to-PDB.py
│   ├── descriptors-from-smiles-as-a-file.py
│   ├── descriptors-from-smiles-with-atoms-aromaticity.py
```

---

## 📄 Script Descriptions

### 📂 sequences/

```
| File | Description |
|------|-------------|
| manual-transcription.py | Performs DNA → RNA transcription manually by replacing T → U. |
| transcription-biopython.py | Uses Biopython to transcribe DNA sequences into RNA. |
| fasta-to-dna-mrna-protein-sequences.py | Reads FASTA and generates DNA, mRNA, and protein sequences. |
| fasta-to-protein-sequence.py | Converts FASTA DNA sequences directly into protein. |
| file-translation-to-stop-at-codon.py | Translates DNA sequences but stops when encountering a STOP codon. |
| stop-at-logic-for-translation.py | Demonstrates algorithmic logic for STOP-aware translation. |
| central-dogma-of-biology.py | Complete DNA → RNA → Protein transformation. |
| translation-to-stop-at-codon.py | Translates sequences until the first STOP codon. |
| manual-translation.py | Manually maps codons to amino acids without external libraries. |
| purine-pirimidine-translation.py | Identifies purines (A,G) and pyrimidines (C,T,U) in sequences. |
```

### 📂 complements/

```
| File | Description |
|------|-------------|
| complement-and-reverse_complement.py | Generates DNA complement and reverse complement. |
| complement-reverse_complement.py | Alternative method for generating complement strands. |
| complement-reverse_complement-from-sequence.py | Takes a user-provided sequence and returns complement + reverse complement. |
```

### 📂 statistics/

```
| File | Description |
|------|-------------|
| length-of-sequence.py | Calculates length of a nucleotide sequence. |
| nucleotide-count-from-file.py | Reads sequence from file and counts A, T, C, G. |
| nucleotide-count-and-length-of-sequence.py | Outputs both nucleotide frequency and length. |
| nucleotide-count-from-file-plot.py | Generates a plotted visualization of nucleotide counts. |
```

### 📂 file_handling/

```
| File | Description |
|------|-------------|
| sequence-conversions-from-file.py | Reads DNA file and converts it to RNA and protein. |
| multiple-files-to-sequeces.py | Loads multiple sequence files and extracts sequences. |
```

### 📂 medical_imaging/

```
| File | Description |
|------|-------------|
| displaying-dicom-file.py | Displays medical DICOM images. |
| reading-info-from-dicom-file.py | Extracts and prints metadata from DICOM files. |
```

### 📂 cheminformatics/

```
| File | Description |
|------|-------------|
| smiles-to-png-with-atom-numbers.py | Converts SMILES to PNG with atom numbers labeled. |
| Smiles2image-using-RDKIT.py | Generates molecular images using RDKit. |
| descriptors-from-smiles.py | Extracts basic molecular descriptors from SMILES. |
| smiles2png-with-atomnumbers.py | Additional SMILES-to-image tool with atom indices. |
| smiles-to-pdb-hydrogen.py | Converts SMILES to PDB and adds hydrogens. |
| smiles-to-descriptors-RDKIT.py | Generates descriptor values using RDKit utilities. |
| smiles-to-morganfingerprint.py | Produces Morgan (circular) fingerprints. |
| smile-descriptors-to-aromaticity.py | Calculates aromaticity-related descriptors. |
| smiles-to-PDB.py | Converts SMILES to a PDB structure. |
| descriptors-from-smiles-as-a-file.py | Reads multiple SMILES from file and generates descriptors. |
| descriptors-from-smiles-with-atoms-aromaticity.py | Computes descriptors + atom-level aromaticity features. |
```

---

## 🎯 Learning Outcomes

Through this coursework and practice, I developed:

* A strong foundation in biological sequence representation
* Practical experience using Biopython for sequence analysis
* Confidence in handling biological data programmatically
* Basic skills in visualizing biological datasets
* An interdisciplinary understanding of programming applied to life sciences

---

## 📌 Notes

* This repository represents **academic learning and practice**, not a production-level bioinformatics pipeline.
* Code is written with a focus on **clarity and understanding**.
* The repository may be extended in the future with advanced bioinformatics
  or machine learning–based analyses.

---

## 📄 Reference

This work is based on material covered during the course
**Introduction to Biological Data / Biological Systems**.
Reference material is not publicly included to respect academic and copyright boundaries.

---

## 📜 License

This project is licensed under the **MIT License**.

Copyright (c) 2026  
**Krish Singh** ([github.com/wasitkrish](https://github.com/wasitkrish))

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3c72,100:ff6b
