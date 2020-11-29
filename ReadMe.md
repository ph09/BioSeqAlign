# Biological Sequence Alignment

In this project, we implement global, semi-global, local and k-band sequence alignment using biological sequence alignment algorithms such as - **Needleman-Wunsch**, **Smith-Waterman**, **Hirschberg** and **k-band** algorithms.

## Running the program

```bash
git clone https://github.com/ph09/BioSeqAlign
cd BioSeqAlign
python3 main.py
```

## Options

### alignment

alignment performs an alignment between two rows with the indicated algorithm. The sequences can be entered manually or files can be used. linear is used in case you want to run the program variant that takes up linear space, otherwise, the quadratic space variant runs.
```bash
alignment [global|semiglobal|local|kband] [text_1|file_1] [text_2|file_2] ?linear
```

### match

match shows the current value of match or sets a new value if it comes as a command parameter.
```bash
match ?new_value
```

### mismatch

mismatch shows the current value of mismatch or sets a new value if it comes as a command parameter.
```bash
mismatch ?new_value
```

### gap

gap shows the current value of gap or sets a new value if it comes as a command parameter.
```bash
gap ?new_value
```

### resources

resources shows current memory and time consumption. 
```bash
resources
```

### exit

exits the program
```bash
exit
```
