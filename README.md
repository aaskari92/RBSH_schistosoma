# Introduction


This GitHub repository includes the scripts used for establishing the reciprocal best hit relationship 
between *Schistosoma mansoni* and *Caenorhabditis elegans*. The requirements include Foldseek, Pandas, Numpy, Matplotlib, and Seaborn.

For the mentioned analysis, first, run 
```
bash prepare_tars.sh
```
to download the structures and prepare them for the downstream analysis.

Foldseek can be run using the `run_foldseek.sh` script.

The pLDDTs for each tar file can be extracted using the following commands:
```
python extract_pldd_from_tar.py Sman.tar
python extract_pldd_from_tar.py Cel.tar
```

