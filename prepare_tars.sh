wget https://ftp.ebi.ac.uk/pub/databases/alphafold/latest/UP000001940_6239_CAEEL_v4.tar
wget https://ftp.ebi.ac.uk/pub/databases/alphafold/latest/UP000008854_6183_SCHMA_v4.tar

mkdir temp
mv UP000001940_6239_CAEEL_v4.tar temp
cd temp
tar -xf UP000001940_6239_CAEEL_v4.tar
rm *.cif.gz
tar -cf ../Cel.tar ./*.pdb.gz
rm *

mv ../UP000008854_6183_SCHMA_v4.tar .
tar -xf UP000008854_6183_SCHMA_v4.tar
rm *.cif.gz
tar -cf ../Sman.tar ./*.pdb.gz
rm *

cd ..
rm -r temp
