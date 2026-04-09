from ultralytics import YOLO

def main():
    # 1. Model seçimi (YOLOv8 nano modeli başlangıç için idealdir)
    model = YOLO('yolov8n.pt')

    # 2. Eğitimi başlat
    # data: Veri setinin yolunu içeren yaml dosyası
    # epochs: Eğitim tur sayısı
    # imgsz: Resim boyutu (genelde 640x640)
    # device: CPU üzerinden eğitildiği için belirtmeye gerek yok ama 'cpu' yazılabilir
    model.train(
        data='data.yaml', 
        epochs=150, 
        imgsz=640, 
        batch=16, 
        name='oyuncak_araba_egitimi'
    )

    print("Eğitim başarıyla tamamlandı!")

if __name__ == '__main__':
    main()