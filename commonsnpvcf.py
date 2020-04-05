import numpy as np
import pandas as pd
import sys
import sqlite3
from sqlalchemy import create_engine

Vcf_file = sys.argv[1]
Bed_file = sys.argv[2]
Output_table = sys.argv[3]
engine = create_engine('sqlite:///akshay.db')
conn = sqlite3.connect("akshay.db")
c = conn.cursor()

def create_datatable(Vcf_file):
	for line in open(Vcf_file):
		if line.startswith('#C'):
			global header_columns
			header_columns = line[1:].split()
	table_columns=pd.DataFrame(columns=header_columns)
	print(table_columns)
	table_columns.to_sql(Output_table, engine, if_exists='append')
	

def check_for_common_pos(Bed_chr,Vcf_chr):
	interect_SNP = pd.DataFrame()
	for index_bed,rows_Bed_chr in Bed_chr.iterrows():
		for index_vcf,rows_vcf_chr in Vcf_chr.iterrows():
			if rows_vcf_chr['POS'] >= rows_Bed_chr['start'] and rows_vcf_chr['POS'] <= rows_Bed_chr['stop'] :
				interect_SNP=interect_SNP.append(pd.Series(rows_vcf_chr), ignore_index=True).reindex(columns=header_columns)
	return interect_SNP		

	
def File_format(Bed_file,Vcf_file):	
	Final_Output_file=pd.DataFrame();
	Vcf_file_modified = pd.read_csv(Vcf_file,sep='\t',header=None,comment="#",names = header_columns);
	Bed_file_dataframe = pd.read_csv(Bed_file,sep = "\t", names = ['chr','start','stop']);
	chr_wise=set(Bed_file_dataframe['chr']);
	
	for chr_assending in chr_wise:
		Vcf_chr = Vcf_file_modified[Vcf_file_modified[['CHROM']].eq(chr_assending).any(1)]
		Bed_chr = Bed_file_dataframe[Bed_file_dataframe[['chr']].eq(chr_assending).any(1)]
		
		Final_Output_file=Final_Output_file.append(check_for_common_pos(Bed_chr,Vcf_chr))
	Final_Output_file=Final_Output_file.sort_values(by='CHROM')
	return Final_Output_file

	
create_datatable(Vcf_file);
Inital = pd.read_sql_query('SELECT * FROM Output_table', engine)
print('Inital Relational Database')
print(Inital)
print('')
Final_Output_file = File_format(Bed_file,Vcf_file)
Final_Output_file.to_sql(Output_table, engine, if_exists='append')	
Final = pd.read_sql_query('SELECT * FROM Output_table', engine)
print('Final relational Database after updating table which consist of variants intersect between VCF an bed file')
print(Final)
print('')

