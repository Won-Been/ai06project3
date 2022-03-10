# Sales Point(판매지수) 예측 서비스


- flask_app: flask 관련 파일
- getdata: 데이터 스크래핑 및 데이터베이스 구축 관련 파일
- Project3_model.ipynb: 모델 구현 코랩 파일
- point_predict.pickle: 모델 파일

## 서비스 목표
- 책의 순위, 평점, 장르를 통해 해당 책의 Sales Point를 예측하는 서비스
  - 알라딘 홈페이지의 Sales Point 정보:

    ![스크린샷 2022-03-10 오전 11 29 07](https://user-images.githubusercontent.com/86759423/157576511-c6ba0f13-7926-4087-9734-7817770d64d0.png)

## 파이프 라인
![스크린샷 2022-03-10 오전 11 43 28](https://user-images.githubusercontent.com/86759423/157577987-c6939a37-3b70-4c86-8bc1-a31e2f9e2422.png)
1. 알라딘 베스트셀러 페이지에서 책의 순위, 평점 및 장르 데이터를 scrapping 해 온다. (베스트 셀러 200권의 데이터 수집)
2. 관계형 데이터 베이스 구축
3. Colab을 활용하여 다중선형회귀 모델 구축 후 최종 모델 저장
4. Flask를 통해 로컬 호스트를 생성?하고, 모델을 연결시켜 책의 정보를 입력하면 Sales Point를 예측해주는 페이지 생성?

## 상세한 과정
1. 베스트 셀러 200권 데이터 가져오기

  ![스크린샷 2022-03-10 오후 1 24 02](https://user-images.githubusercontent.com/86759423/157589142-5d84d599-02b2-490a-a960-25dc17c646c7.png)
- {책 id: [순위, 평점, 장르]}의 형태로 데이터 스크래핑

2. 관계형 데이터베이스에 저장

  ![스크린샷 2022-03-10 오후 1 25 48](https://user-images.githubusercontent.com/86759423/157589298-a169525e-cad9-4c55-a057-8f3474c0a8aa.png)
- 데이터 구조에 변화가 없으며, 데이터의 양이 적다. 또한, 구조화된 질의를 통해 데이터를 다룰 수 있으며 탐색 속도가 비교적 빠르기 때문에 관계형 데이터베이스에 저장

3. 모델 생성 후 로컬 호스트 연결

  ![스크린샷 2022-03-10 오후 1 26 39](https://user-images.githubusercontent.com/86759423/157589393-f8614851-8643-49ec-9816-f3d5badacb0a.png)
- 다중 선형 회귀 모델을 이용해 Sales Point를 예측하는 모델 개발
- 해당 모델을 로컬 호스트에 연결해 순위, 평점, 장르를 입력하면 Sales Point를 예측하는 페이지를 보여주는 서비스 개발


## 결과물

https://user-images.githubusercontent.com/86759423/157589016-0c67aa9f-9412-4bd2-a989-6504312d1747.mov

------------------------------------------------------
## 추가적인 사항
## Metabase를 이용한 분석용 대시보드 개발
- Docker를 활용해 대시보드 개발

  ![스크린샷 2022-03-10 오후 1 30 45](https://user-images.githubusercontent.com/86759423/157589819-f8d15cde-3501-42b0-ba2a-44c0feff75be.png)
  ![스크린샷 2022-03-10 오후 1 33 33](https://user-images.githubusercontent.com/86759423/157590128-0ad642c0-b40e-4f17-a584-705f9b2d3a39.png)



