### Auto donwload metegenome data from NCBI

#### Get SRR_Acc_list.txt from NCBI
1. Search project information in NCBI
![step1](pic/step1.JPG)
2. Show 200 per page in the bottom of the summary
![step2](pic/step2.JPG)
3. Back to the top and click 'Send results to Run selector'
![step3](pic/step3.JPG)
4. Select the box in red arrow and click Accession List in green arrow
![step4](pic/step4.JPG)

#### Download database
1. download auto_down.py and put the SRR_Acc_List.txt in one directory
2. open a console and run ```python auto_down.py```
3. All database in the project will be downloaded and the costing time is related to the size of database.

#### Proxies
If you do not use proxy, you can delelte the proxies in auto_down.py