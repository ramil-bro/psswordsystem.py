Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@ramil-bro 
Learn Git and GitHub without any code!
Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.


1
00ramil-bro/Ramil-
 Code Issues 0 Pull requests 0 Actions Projects 2 Wiki Security Insights Settings
Ramil-/passwordsystem.py
@ramil-bro ramil-bro qaqaw
328e684 3 minutes ago
25 lines (25 sloc)  739 Bytes
  
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
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
