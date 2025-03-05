import os.path
from copy import deepcopy
global pojmovi
global pozitivni
global negativni
global skup
global m,n
global resenja
global unique_matrices
global matricakorisnika
class Node:
    def __init__(self, val, level, id):
        self.val = val
        self.id=id
        self.level=level
        self.children = []

def newNode(key, level,id):
    temp = Node(key,level,id)
    return temp

def preorder(root):
    pre=[]
    nodes = []
    nodes.append(root)
    while (len(nodes)):
        curr = nodes[0]
        nodes.pop(0)
        pre.append(curr)
        for i in range(len(curr.children) - 1, -1, -1):
            nodes.insert(0, curr.children[i])
    return pre

def ispisistablo(root):
    pre=preorder(root)
    makslevel=max([x.level for x in pre])
    print('NIVO 0:\n')
    print('CVOR {0}:\n'.format(root.id))
    ispiscvora(root)
    lev=1
    while(lev<=makslevel):
        i=0
        for j in range(len(pre)):
            if pre[j].level==lev-1:
                i=j
                break
        print('NIVO {0}:\n'.format(lev))
        print('DECA CVORA {0}:\n'.format(pre[i].id))
        for j in range(len(pre)):
            if pre[j].level==lev:
                i=j
                break
        while(i<len(pre)):
            if pre[i].level<lev:
                print('DECA CVORA {0}:\n'.format(pre[i].id))
            elif pre[i].level==lev:
                print('CVOR {0}:\n'.format(pre[i].id))
                ispiscvora(pre[i])
            i+=1
        lev+=1
    print()

def brojmatriceuresenjima(matrica):
    global resenja
    br=0
    for i in resenja:
        if i==matrica:
            br+=1
    return br

def listresenje(node):
    if '-' not in node.val:
        return True
    else:
        return False

def putdoresenja(i):
    leveli=[]
    path=[]
    pre=preorder(root)
    for j in range(len(pre)):
        leveli.append(pre[j].level)
    for j in range(len(pre)):
        if pre[j].val==i:
            k=0
            while(k<=pre[j].level):
                max_k=0
                for m in range(0, j+1):
                    if leveli[m]==k:
                        max_k=m
                path.append(pre[max_k])
                k+=1
            break
    return path

def ispisiputdoresenja(path):
    for i in path:
        ispisimatricu(i.val)
        print("\n")

def ispisiresenje():
    obradaresenja()
    global unique_matrices
    if obradaresenja()==True:
        print('Resenja su:\n')
        for i in unique_matrices:
            ispisimatricu(i)
            print('Do ovog resenja se dolazi na {} nacina\n'.format(brojmatriceuresenjima(i)))
            print('Put do ovog resenja je:\n')
            putanja=putdoresenja(i)
            ispisiputdoresenja(putanja)
    else:
        print('Nema resenja!')

def ispisimatricu(matrica):
    for i in matrica:
        for j in range(len(i)):
            if i[j]=='-':
                print(i[j], end="\t\t")
            else:
                print(i[j], end='\t')

        print()
def ispiscvora(cvor):
    for i in cvor.val:
        for j in range(len(i)):
            if i[j]=='-':
                print(i[j], end="\t\t")
            else:
                print(i[j], end='\t')
        print()


def promeninegativne():
    global negativni, pozitivni, pojmovi
    for i in range(len(pojmovi)):
        for j in range(len(pojmovi[i])):
            for k in range(len(pozitivni)):
                if pojmovi[i][j] == pozitivni[k][0]:
                    grupa=i
                    for m in pojmovi[i]:
                        if m!=pojmovi[i][j]:
                            negativni.append([pozitivni[k][1],m])
                if pojmovi[i][j] == pozitivni[k][1]:
                    grupa=i
                    for m in pojmovi[i]:
                        if m!=pojmovi[i][j]:
                            negativni.append([pozitivni[k][0],m])


def validno(cvor):
    global pozitivni, negativni
    for i in range(1,len(cvor.val)):
        for j in range(len(cvor.val[i])):
            for k in range(0,len(cvor.val)):
                if i!=k and cvor.val[k][j]!='-' and cvor.val[i][j]!='-':
                    if [cvor.val[k][j],cvor.val[i][j]] in negativni:
                        return False
    return True
def broj(matrica):
    brojac=0
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if matrica[i][j]!='-':
                brojac+=1
    return brojac-n

def kreirajstablo(root):
    stack=[]
    global resenja
    resenja=[]
    matrica1=deepcopy(root.val)
    trenutni=newNode(matrica1,0,0)
    root=trenutni
    matrica=deepcopy(matrica1)
    stack.append(trenutni)
    br=0
    while(stack!=[]):
        trenutni=stack.pop(0)
        for i in range(1,len(pojmovi)):
            for j in range(len(pojmovi[i])):
                for k in range(n):
                    if matrica[i][k]=='-' and pojmovi[i][j] not in matrica[i]:
                        matrica[i][k]=pojmovi[i][j]
                        br+=1
                        cvor=newNode(matrica,broj(matrica),br)
                        if validno(cvor):
                            if broj(matrica)==n*(m-1):
                                resenja.append(cvor.val)
                            #print(cvor.val)
                            trenutni.children.append(cvor)
                            stack.append(cvor)
                        else:
                            br-=1
                        matrica=deepcopy(trenutni.val)
    return root

def obradaresenja():
    global resenja
    global unique_matrices
    unique_matrices = []
    # Loop over the original list and compare each matrix element-wise with all the other matrices
    for i in range(len(resenja)):
        is_duplicate = False
        for j in range(i + 1, len(resenja)):
            if resenja[i] == resenja[j]:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_matrices.append(resenja[i])
    if unique_matrices==[]:
        return False
    else:
        return True

def proveri():
    global unique_matrices
    global matricakorisnika
    for k in unique_matrices:
        br = broj(matricakorisnika)+n
        for i in range(len(matricakorisnika)):
            for j in range(len(matricakorisnika[i])):
                if matricakorisnika[i][j]!='-' and matricakorisnika[i][j]==k[i][j]:
                    br-=1
        if br==0:
            return True
    return False

def unesiumatricukorisnika(a):
    global matricakorisnika
    for i in range(m):
        for j in range(n):
            if a[0]==matricakorisnika[i][j]:
                for x in range(1,len(pojmovi)):
                    if a[1] in pojmovi[x]:
                        matricakorisnika[x][j]=a[1]
def dosadaispravno():
    upareniglobal=[]
    upareni=[]
    global negativni
    global matricakorisnika
    for i in range(n):
        for j in range(m):
            if matricakorisnika[j][i]!='-':
                upareni.append(matricakorisnika[j][i])
        upareniglobal.append(upareni)
        upareni=[]
    for i in upareniglobal:
        if len(i)>1:
            for k in negativni:
                if k[0] in i and k[1] in i:
                    return False

    return True
def najverovatnijeresenje():
    global matricakorisnika, unique_matrices
    najm=None
    bristih=0
    bristihtr=0
    for k in unique_matrices:
        for i in range(1,len(matricakorisnika)):
            for j in range(len(matricakorisnika[i])):
                if matricakorisnika[i][j]==k[i][j]:
                    bristihtr+=1
        if(bristihtr>bristih):
            bristih=bristihtr
            najm=k
            bristihtr=0
    return najm

def pomocprijatelja():
    global matricakorisnika
    global unique_matrices
    k=najverovatnijeresenje()
    if k==None:
        pre = preorder(root)
        makslevel = max([x.level for x in pre])
        for i in pre:
            if i.level==makslevel:
                k=i
                break
        for i in range(1,len(matricakorisnika)):
            for j in range(len(matricakorisnika[i])):
                if k.val[i][j]!='-' and matricakorisnika[i][j]!=k.val[i][j]:
                    matricakorisnika[i][j]=k.val[i][j]
                    return None
    else:
        for i in range(1,len(matricakorisnika)):
            for j in range(len(matricakorisnika[i])):
                if matricakorisnika[i][j]!=k[i][j]:
                    matricakorisnika[i][j]=k[i][j]
                    return None

def meni2():
    b=0
    print('--------------MENI----------------')
    a = input('Unesite pojmove koje zelite da uparite:\n')
    a = a.split('+')
    unesiumatricukorisnika(a)
    ispisimatricu(matricakorisnika)
    pre = preorder(root)
    makslevel = max([x.level for x in pre])
    while (b != 5):
        br=broj(matricakorisnika)
        if br==makslevel:
            if makslevel==n*(m-1) and matricakorisnika in unique_matrices:
                print('Cestitamo dosli ste do resenja!\nKraj igre.\n')
                exit()
            elif makslevel<n*(m-1):
                print('Nema resenja! Dosli ste do kraja igre.\n')
                exit()
        b=input('Izaberite jednu od opcija:\n1.novi potez\n2.provera ispravnosti uparenih pojmova\n3.provera da li trenutno stanje vodi do resenja\n'
                '4.pomoc\n5.igra nema resenja\n6.kraj igre\n')
        b=int(b)
        if b==1:
            print('--------------MENI----------------')
            a = input('Unesite pojmove koje zelite da uparite:\n')
            a = a.split('+')
            unesiumatricukorisnika(a)
            ispisimatricu(matricakorisnika)
        elif b==2:
            if dosadaispravno()==True:
                print('Pojmovi su ispravno upareni!\n')
            else:
                print('Pojmovi nisu ispravno upareni!\n')
        elif b==3:
            if proveri()==True:
                print('Na dobrom ste putu!\n')
            else:
                print('Niste na dobrom putu!\n')
        elif b==4:
            pomocprijatelja()
            ispisimatricu(matricakorisnika)
        elif b==5:
            if makslevel<n*(m-1):
                print('Cestitamo, vas odgovor je tacan!\n')
            else:
                print('Vas odgovor je netacan. Kraj igre.\n')
            exit()
        elif b==6:
            print('Kraj igre!\n')
            exit()
        else:
            print('Neispravna opcija!\n')
            exit()

global negativni, pozitivni, pojmovi,matricakorisnika
a=input('Izaberite da li podatke o igri zelite da unesete preko standardnog ulaza ili iz datoteke:\n1.stdin\n2.datoteka\n')
a=int(a)
if a==1:
    m=input('Unesite broj vrsta:\n')
    m=int(m)
    n=input('Unesite broj kolona:\n')
    n=int(n)
    print('Unesite vrste:')
    pojmovi=[]
    negativni=[]
    pozitivni=[]
    for i in range(m):
        vrsta=input()
        vrsta=vrsta.split(',')
        pojmovi.append(vrsta)
    while(True):
        uslov=input('Unesite uslov:\n')
        if not uslov:
            break
        if '-' in uslov:
            uslov=uslov.split('-')
            negativni.append(uslov)
        elif '+' in uslov:
            uslov=uslov.split('+')
            pozitivni.append(uslov)
    print("POCETNO STANJE IGRE:\n")
    nova = pojmovi[0]
    matricastanja = []
    matricastanja.append(nova)
    for i in range(1, m):
        nova = []
        for j in range(n):
            nova.append('-')
        matricastanja.append(nova)
    promeninegativne()
    root = newNode(matricastanja, 0,0)
    ispiscvora(root)
    root = kreirajstablo(root)
    obradaresenja()
    print()
    a = 0
    matricakorisnika = []
    nova = pojmovi[0]
    matricakorisnika.append(nova)
    for i in range(1, m):
        nova = []
        for j in range(n):
            nova.append('-')
        matricakorisnika.append(nova)

    while a != 4:
        a = input('Da biste zapoceli igru izaberite jednu od ponudjenih opcija:\n'
                  '1.ispis celog stabla po nivoima\n2.ispis razlicitih resenja i puteva do njih\n3.pocetak igre\n4.kraj igre\n')
        a = int(a)
        if a == 1:
            ispisistablo(root)
        elif a == 2:
            ispisiresenje()
        elif a == 3:
            meni2()
        else:
            print("Kraj igre.")

elif a==2:
    try:
        ulazna="sof.txt"
        if not os.path.exists(ulazna):
            raise Exception('DAT_GRESKA')
    except Exception as e:
        print(e, end='')
    else:
        f=open(ulazna,'r')
        m=f.readline()
        m=int(m)
        n=f.readline()
        n=int(n)
        matricastanja=[]
        pojmovi=[]
        negativni=[]
        pozitivni=[]
        for i in range(0,m):
            line=f.readline()
            line=line.strip()
            pojmovi.append(line.split(','))
        for line in f:
            line=line.strip()
            if '-' in line:
                negativni.append(line.split('-'))
            elif '+' in line:
                pozitivni.append(line.split('+'))
        print("POCETNO STANJE IGRE:\n")
        nova=pojmovi[0]
        matricastanja.append(nova)
        for i in range(1,m):
            nova=[]
            for j in range(n):
                nova.append('-')
            matricastanja.append(nova)
        promeninegativne()
        root=newNode(matricastanja,0,0)
        ispiscvora(root)
        root=kreirajstablo(root)
        obradaresenja()
        print()
        a=0
        matricakorisnika=[]
        nova = pojmovi[0]
        matricakorisnika.append(nova)
        for i in range(1, m):
            nova = []
            for j in range(n):
                nova.append('-')
            matricakorisnika.append(nova)

        while a!=4:
            a=input('Da biste zapoceli igru izaberite jednu od ponudjenih opcija:\n'
                  '1.ispis celog stabla po nivoima\n2.ispis razlicitih resenja i puteva do njih\n3.pocetak igre\n4.kraj igre\n')
            a=int(a)
            if a==1:
                ispisistablo(root)
            elif a==2:
                ispisiresenje()
            elif a==3:
                    meni2()
            else:
                print("Kraj igre.")
