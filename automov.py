import os
import shutil as sc

def pnpdfs(x):
    print("x= {},no of items = {}".format(x,len(x)))
    print('\n')

def movac(file,sour,dest):
    sc.move(sour, dest)
    print('file({}) at {} has been moved to {}\n'.format(file,sour,dest))




    

Documents_X='X:\\sricharan_backup\\Documents'
Documents_C='C:\\Users\\Chara\\Documents'
Downloads_x='X:\\sricharan_backup\\Downloads'
Downloads_C='C:\\Users\\Chara\\Downloads'


os.getcwd()
sour = os.chdir('C:\\Users\\Chara\\Downloads')
print(os.getcwd(),'\n')


f=os.listdir()

pdfs=[]

for file in f:
    ispdf=file.endswith('pdf')
    if(ispdf==True):
        pdfs.append(file)

jpdf=[]
pypdf=[]
Npdf=[]
CVpdf=[]
bankpdf=[]

for pdf in pdfs:
    isjpdf='java' in pdf or 'Java' in pdf
    ispypdf='python' in pdf or 'Python' in pdf
    isNpdf='Neural' in pdf or 'AI' in pdf or 'Artificial Intillegence' in pdf
    isCVpdf='cv' in pdf or 'CV' in pdf
    isbankpdf='Bank' in pdf or 'bank' in pdf

    if(isjpdf==True):
        jpdf.append(pdf)
        destj='\\'.join([Documents_X,'java'])
        souj='\\'.join([Downloads_C,pdf])
        movac(pdf,souj,destj)
    if(ispypdf==True):
        pypdf.append(pdf)
        destpy='\\'.join([Documents_X,'Python'])
        soupy='\\'.join([Downloads_C,pdf])
        movac(pdf,soupy,destpy)
    if(isNpdf==True):
        Npdf.append(pdf)
        destN='\\'.join([Documents_X,'ML1'])
        souN='\\'.join([Downloads_C,pdf])
        movac(pdf,souN,destN)
    if(isCVpdf==True):
        CVpdf.append(pdf)
        destcv='\\'.join([Documents_X,'CV_Resumes'])
        soucv='\\'.join([Downloads_C,pdf])
        movac(pdf,soucv,destcv)
    if(isbankpdf==True):
        bankpdf.append(pdf)
        destbank='\\'.join([Documents_X,'BANK'])
        soubank='\\'.join([Downloads_C,pdf])
        movac(pdf,soubank,destbank)

pnpdfs(jpdf)
pnpdfs(pypdf)
pnpdfs(Npdf)
pnpdfs(CVpdf)
pnpdfs(bankpdf)











