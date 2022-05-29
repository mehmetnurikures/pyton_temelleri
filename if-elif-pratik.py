# name=input('Bir isim giriniz: ')
# age=int(input('yaş giriniz: '))
# education=input('eğitim durumu: ')
# #yaş en az 18, eğitim en az lise mezunu olmalıdır.
# if (age>=18) and (education=='lise mezunu' or education=='üniversite mezunu'):
#    print('sinava girebilir')
# else:
#     print('sinava giremez')
name=input('Bir isim giriniz: ')
age=int(input('yaş giriniz: '))
education=input('eğitim durumu: ')
#yaş en az 18, eğitim en az lise mezunu olmalıdır.
if (age>=18):

    if(education=='lise mezunu' or education=='üniversite mezunu'):
      print('sinava girebilir')
    else:
       print('sınava giremez, çünkü eğitimi yeterli değil.')

else:

   print('sinava giremez, çünkü yaşı yeterli değildir.')