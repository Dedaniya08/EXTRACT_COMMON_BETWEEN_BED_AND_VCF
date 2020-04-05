# EXTRACT_COMMON_BETWEEN_BED_AND_VCF


This package can be used to extract the SNPs from VCF from a particular region in the BED file 

or the mentioned start and stop position in the BED file. This package also can be used to 

extract the gene SNPs from the VCFfile.



# Inside the Folder.

The folder consist of a script commonsnpvcf.py which is the main script, additional to that it 

has a sample VCF file and a bed file as an example.


  - commonsnpvcf.py
  - sample_bed_file.bed
  - sample_VCF.vcf
  - Readme.txt
  


# How to run the script.

This is a simple way to go, make sure you keep all the files in a single folder your VCF file as 

well as the bed file.

```
python ./commonsnpvcf.py sample_VCF.vcf sample_bed_file.bed Output_table;

```

The first argument after the commonsnpvcf.py is VCF file from which you want to extract the SNP  
either the gene region or the start and stop region. 


The second argument after the VCF file is BED file, which has the start and stop region. From 

which you can extract the SNP. Please the format of the bed file.


And the third argument is the output file name, what you want to label. This file consist of the 

SNP from the VCf file for the desire start and stop in BED file.



## File format


Please look at the sample VCF file and BED file for file format attached with this package.


## Contributing

All comments and any kind of contribution is useful. The best way is to open an issue or make a pull request.
