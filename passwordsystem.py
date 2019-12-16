
import time
ad='ramil'
sifre='111'
while(True):
    AD=input('adinizi daxil edin: ')
    Sifre=input('sifreni daxil edin : ')
    if ((AD==ad) and (Sifre==sifre)):
        print('duzur',ad)
        break
    elif((AD!=ad) and (Sifre==sifre)):
        print('adiniz sehvdir')
    elif((AD ==ad) and (Sifre !=sifre)):
        print('sifre sehvdir')
        print('sifrenzi isteyirsinizse deyisdirin'(A/B))
        cavab = input('davam yoxsa A secimi: ')        
        if (cavab=='A'):
            yeni_parol=input('daxil et')
            yeni_parol=sifre
            print('gozleyin')
            time.sleep(2)
            print('gozleyin..')
            time.sleep(2)
            print('gozleyin...')
    else:
        print('go out',AD)
