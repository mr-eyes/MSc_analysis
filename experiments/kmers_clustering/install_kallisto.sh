git clone https://github.com/pachterlab/kallisto.git
git clone https://github.com/samtools/htslib.git
sed -i -e 's/#define MAX_KMER_SIZE 32/#define MAX_KMER_SIZE 128/g' ./kallisto/src/Kmer.hpp
cd htslib
autoheader
autoconf
./configure
make
cd ../
rm -rf -f kallisto/build
rm -rf kallisto/ext/htslib
mv  htslib kallisto/ext/
mkdir kallisto/build
cd kallisto/build
cmake ..
make
