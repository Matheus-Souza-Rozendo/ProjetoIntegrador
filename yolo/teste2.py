import cv2

#carregando as classes de objeto
class_names =[]
with open("coco.names","r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Carregar a imagem
image = cv2.imread('foto1.jpeg')

net = cv2.dnn.readNet("yolov4-tiny.weights","yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)

model.setInputParams(size=(416,416),scale=1/255)

(classes, score, box) = model.detect(image,0.1,0.2)

for (classid, score, box) in zip(classes, score, box):
    color = (0,255,255)
    
    label = f"{class_names[classid]} : {score}"

    cv2.rectangle(image,box,color)

    cv2.putText(image,label,(box[0],box[1]-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)

cv2.imshow('Pessoas Detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

