# Image-segmentation

> COCO 라벨의 YOLO 형식 변환

## 프로젝트 개요

- 주제: COCO 라벨의 YOLO 형식 변환
- 형태: 코드·데이터·문서 저장소
- 저장소: https://github.com/ttony0321/Image-segmentation
- 기본 브랜치: master
- 공개 범위: Public

치아 이상유무 탐지 이미지 segmentation

제한된 시간과 gpu할당시간으로 인하여 여러 모델을 실험할 시간이 부족
간편화 되어있고 빠르게 학습 진행가능한 Yolo사용 학습 진행

공모전이 시작하면 인터넷이 제한되는 폐쇄망으로 전환되기떄문에 제한되는 부분이 많음


## 주요 기능

- COCO 라벨 읽기
- YOLO 라벨 변환
- data.yaml 데이터셋 설정
- 텍스트 라벨 생성

## 기술 스택

- Python

## 프로젝트 구조

- `README.md`
- `checking.py`
- `coco2yolo.py`
- `data.yaml`
- `totxt.py`

## 실행 방법

- 로컬 경로·외부 API 설정 확인
- 실행 명령: python "checking.py"

## 핵심 구현

- 목적별 파일 분리
- 재사용 가능한 코드·데이터 자산 구성

## 개선 과제

- 의존성 버전 고정
- 환경변수 기반 경로·설정 관리



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
