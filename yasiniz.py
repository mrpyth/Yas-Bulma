import datetime, sys #datetime ve sys modüllerimizi import ediyoruz.

class KacYasindasin(object): #KacYasindasin adlı bir class oluşturuyoruz. class'ın adını istediğiniz şey yapabilirsiniz
    
    def __init__(self): #Çok uzatmadan direkt __init__ fonksiyonuna şu kodları yazıyoruz.
        
        try:
            bu_yil = datetime.datetime.now() #Bulunduğumuz yılı almak için şu an'ı buluyoruz.
            
            a = int(input("Doğum Tarihin : ")) #Kullanıcıdan doğum tarihini alıyoruz.
            
            if a == 0: #Eğer kullanıcı '0' girerse:
                sys.exit() #programdan çıksın diyoruz.
                
            yas = (bu_yil.year - a) #Burda kaç yaşında olduğunun işlemlerini yapıyoruz.
            
            if bu_yil.year < a: #Burda da eğer kullanıcı gelecekten bir sene girdiyse uyarıyoruz.
                print("Daha gelmemiş bir tarihte doğmuş olamazsın.")
                KacYasindasin()
                
            else: #Eğer geçmişten bir sene girdiyse yaşını bastırıyoruz.
                print("{} yaşındasın.".format(yas))
                
                
        except ValueError: #Kullanıcı sayı yerine harf ya da başka bir işaret girdiyse burdan yakalayıp uyarıyoruz. Ve tekrar yaşını girmesini istiyoruz. 
            print("Doğum Tarihin Bir Sayı Olmalı.")
            KacYasindasin()
            
            
if __name__ == "__main__": #Aynı sayfada kodumuzu çağırıyoruz.
    KacYasindasin()
