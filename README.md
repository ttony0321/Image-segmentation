# Image-segmentation
image_segmentation teeth
치아 이상유무 탐지 이미지 segmentation

제한된 시간과 gpu할당시간으로 인하여 여러 모델을 실험할 시간이 부족
간편화 되어있고 빠르게 학습 진행가능한 Yolo사용 학습 진행

공모전이 시작하면 인터넷이 제한되는 폐쇄망으로 전환되기떄문에 제한되는 부분이 많음

순서
checking.py -> coco2yolo.py -> totxt.py
### checking.py
````
#Data 형식은 coco dataset하고 유사
#json 안에 표시된 파일명과 사진명이 안맞는 경우가 있어 안맞는 이름들 체크
python checking.py find_error (json_data_path)
````

### coco2yolo.py
````
#기존 coco형식의 데이터를 yolo data방식으로 변환
#원래 바로 txt파일로 변환하려고 했지만 시간도 오래 걸리고 변환중 꺼지는 경우가 있어서 변환후-> txt변환
python coco2yolo.py convert_loop (image_path) (json_path) (output_path)
````

### totxt.py
````
python totxt.py json2txt (output_path)
````

이후 Yolov8 segmentation 학습 진행
