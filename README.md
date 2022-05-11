<!-- TABLE OF CONTENTS -->
<div align="center">
 <h1 style='text-align:center; font-size: 60px; '>밥비트🍚</h1>
 </p>
 <p align="center">
  <h3>소비자를 위한  물가 예측 서비스</h3>
</div>

##  0. 조원 소개
- 진정한(조장), 강혜진, 서아현, 이태우, 조영래, 조용준, 최승훈

## 1. 개발 배경 및 목적
물가 변동에 소비자가 능동적으로 대처할 수는 없을까? 라는 생각에서 출발하여
가공품들의 물가를 예측해 소비자들에게 정보를 제공하는 서비스를 기획

<br>

## 2. 기능 및 UI/UX
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/serviceflow.png?raw=true'>

<br>

## 3. 서비스 FLOW
 > - 코로나로 인한 폐업과 상권 경쟁 심화 문제
 > - 방대한 카페 자료로 인한 쉬운 검색서비스 필요
 > - 이미지 기반 추천 시스템으로 경쟁력 확보
<!-- <img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/background.PNG?raw=true' height='400'> -->
<br>

## 4. ERD
<img src='https://github.com/AIVLE-School-first-Big-Project/Acachu/blob/main/readmeImage/erd.png?raw=true'>

<br>

## 5. 개발 환경
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=HTML5&logoColor=white">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
<br>

## 6. 기대 효과
소상공인 및 일반 사용자
- 다음 달 물가를 예측하여 재고 관리에 도움
- 포인트 사용을 통해 물건 구매에 도움 (광고효과)
- 일반 발화 입력 챗봇으로 정보를 제공함으로써 접근성 향상

기업
- KT커머스에서 진행하는 메타버스 전자상거래과 같은 서비스와 연동을 통해 사용자에게 정보 제공
- 사용자에게 다양한 정보 제공을 통해 기업에 긍정적인 이미지 적용
- AI 기반 모달형식의 챗봇 BTC 서비스 제공

<br>

## 7. 유저 가이드

> git clone https://github.com/AIVLE-School-first-Big-Project/BobBit.git
> 프로젝트 폴더에 <my_settings.py> 파일 추가 후 아래 내용 추가
  SECRET_KEY = "<SECRET_KEY>"
  DATABASES = {
      "default": {
          "ENGINE": "<ENGINE>",
          'NAME': '<NAME>',
          'USER': '<USER NAME>',
          'PASSWORD': '<password>',
          'HOST': '<HOST NAME>',
          'PORT': <PORT NUM>,
      }
  }
> pip install -r requirements.txt
> python manage.py makemigrations(최초실행시)
> python manage.py migrate(최초실행시)
> sili/config/<DatabaseConfig.py> 파일 추가 후 아래 내용 추가
  DB_HOST = "<DB_HOST>"
  DB_USER = "<DB_USER>"
  DB_PASSWORD = "<DB_PASSWORD>"
  DB_NAME = "<DB_NAME>"

  def DatabaseConfig():
      global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
> python manage.py runserver

<br>
