YOLOv8 ile Nesne Algılama: Oyuncak Araba Tanıma Projesi
Tokat Gaziosmanpaşa Üniversitesi | Bilgisayar Programcılığı
Hazırlayan: Mervenur Alak

Projenin Amacı ve Kapsamı
Bu proje, derin öğrenme algoritmalarının mikro ölçekli nesneler üzerindeki tanıma performansını ölçmek amacıyla kurgulanmıştır. Güncel nesne tespit mimarisi olan YOLOv8 kullanılarak; statik görseller, video kayıtları ve canlı kamera akışları üzerinde oyuncak arabaların anlık tespiti ve sınıflandırılması hedeflenmiştir.

Veri Hazırlığı ve Mühendisliği
Segmentasyon: Model, oyuncak araba sınıfına odaklanmış; farklı marka, model ve renklerdeki araç varyasyonlarını kapsayacak şekilde eğitilmiştir.

Veri Seti Mimarisi: Çeşitli ortam ve ışık koşullarında çekilen görseller, LabelImg aracı ile hassas bir şekilde etiketlenmiştir. "Bounding Box" (Sınırlayıcı Kutu) yöntemiyle nesne sınırları milimetrik olarak belirlenmiştir.

Optimizasyon: Veri seti, modelin gerçek performansını yansıtması amacıyla Eğitim (Train) ve Doğrulama (Val) setlerine ayrılmıştır.

Model Mimarisi ve Teknik Altyapı
Projede, mobil cihazlarda ve standart bilgisayarlarda bile yüksek hızda çalışabilen YOLOv8n (Nano) modeli tercih edilmiştir. Mevcut model üzerine, projeye özel toplanan veri setiyle Transfer Learning (Transfer Öğrenme) metodu uygulanmıştır. Donanım kısıtlamalarına rağmen, CPU üzerinde optimize edilmiş bir eğitim süreci yönetilmiştir.

Eğitim Stratejisi ve Başarı Metrikleri
Eğitim Parametreleri: Model, 150 epoch (eğitim turu) boyunca eğitilmiştir. Her turda hata payı (Loss) minimize edilerek en kararlı ağırlıklar (best.pt) elde edilmiştir.

Analitik Sonuçlar: Yapılan performans analizlerinde modelimiz, akademik başarı sınırı olan %85’i geride bırakarak %98.7 mAP (mean Average Precision) skoruna ulaşmıştır.

Karmaşıklık Matrisi (Confusion Matrix): Modelin arka plan gürültüsü ile gerçek nesneleri ayırt etme başarısı %100 olarak kaydedilmiş, yanlış pozitif (hatalı tanıma) oranı minimize edilmiştir.

Fonksiyonel Yazılım Bileşenleri
Sistem, uçtan uca bir boru hattı (pipeline) olarak tasarlanmıştır:

Otomatik Eğitim Scripti (egitim.py): Modelin eğitim parametrelerini, veri yollarını ve epoch sayısını yöneten Python tabanlı çekirdek kod.

Tahmin Modülü (Inference): Kaydedilmiş ağırlıklar üzerinden; fotoğraf (img1), video ve canlı yayın üzerinde saniyeler içinde analiz yapabilen modül.

İzole Ortam Yönetimi: Proje, sistem karmaşasını önlemek adına Conda tabanlı yolo_proje sanal ortamında stabilize edilmiştir.

Proje Dizin Yapısı
runs/detect/train/: Eğitime dair tüm bilimsel grafikler, kayıp eğrileri ve doğrulama görselleri.

best.pt: Projenin kalbi olan, en yüksek başarımlı ağırlık dosyası.

data.yaml: Veri seti konfigürasyonu ve sınıf tanımlamaları.

egitim.py: Modelin eğitim sürecini başlatan ve yöneten kaynak kod dosyası.
