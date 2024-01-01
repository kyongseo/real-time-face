# MOSAINFO - 얼굴 인식을 기반한 초상권 침해 방지 멀티 스트리밍 애플리케이션  <br/>

## 목차 
1. [About Project ](#1장-About-Project)
2. [Duration ](#2장-Duration)
3. [Preview ](#3장-preview)
4. [Stacks ](#4장-stacks)
5. [System Structure](#5장-system-structure)
6. [Structure Internal Details 멀티 스트리밍 구조](#6장-structure-internal-details-멀티-스트리밍-구조)
7. [AI Training Details](#7장-ai-training-details)
8. [More Details...](#8장-More-Details)
<br/>
<br/>


## 1장. About Project..

#### 주기능 
라이브 스트리밍에서 일반인의 얼굴이 등장하면 인공지능이 감지하여 실시간으로 자동 모자이크를 처리합니다.
<br/>

#### 개발 배경
최근 몇년간 인터넷이 급속도로 발전함에 따라 실시간 스트리밍 방송을 제공하는 플랫폼들 역시 크게 성장했습니다. 이는 양날의 검으로, 그 이면에는 심각한 부작용이 존재합니다. 그중 하나로는 “초상권 침해의 위험성”이 있습니다. 개인 방송 플랫폼의 증가로 인해 실시간 방송을 진행하는 과정에서 지나가는 시민들의 얼굴이 무차별적으로 노출이 되어 초상권을 침해하는 일이 빈번하게 발생하고 국민 청원뿐만 아니라 피해 신고 접수 또한 급격히 늘고 있습니다. 추가적으로 일반 영상에 비해, 실시간 스트리밍은 시청자들에게 영상이 즉시 전달되기 때문에 수습할 시간이 주어지지 않아 그 심각성이 더욱 크다고 생각됩니다.

이를 해결하기 위한 방안으로, 실시간으로 얼굴 인식을 기반한 초상권 침해 방지를 위한 멀티 스트리밍 애플리케이션을 개발하게 되었습니다.
<br/>

#### 개인 정보 모자이크 대상
모자이크 대상으로는, 다음으로 선정하였습니다.
- 일반 시민
<br/>

## 2장. Duration
- 2022.09 ~ 2023.01 (5개월)
<br/>

## 3장. Preview
<!-- <img src="https://user-images.githubusercontent.com/102573192/210356297-37bff7e5-de71-4aa0-966e-c9e7660e455c.png" width="30%" height="10%">  <img src="https://github.com/kyounggseo/real-time-face/assets/102573192/b7258bad-fec2-42dc-9b71-60d96ce24290" width="40%" height="200%"> -->

<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/9e3ede76-d711-40d2-9ac3-268f7cab079a" width="40%" height="20%">

<!-- ![미디어01](https://github.com/kyounggseo/real-time-face/assets/102573192/702e048b-de90-41d8-851d-4e0131842f3f)

 <img src="https://github.com/kyounggseo/real-time-face/assets/102573192/9ebc3fc3-4106-4c21-b6c0-16da77fb7979" width="30%" height="20%" align='right'> -->
<br/>





## 4장. Stacks
#### 백엔드 (BACKEND)
- Python 3.6.8
- Java 11.0.1 <br/>
- FireBase storage <br/>
- Raspberry Pi 3B+
- Android Studio
- OpenCV
- NginX
  
#### 인공지능 모델 학습 (AI Model Training)
- Yolov5
<br/>

## 5장. System Structure
<!-- <img src="https://github.com/kyounggseo/real-time-face/assets/102573192/f0c690c0-91e4-4e11-8d75-7a07511654db" width="80%" height="70%"> <br/> -->
<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/b65e9f18-716c-43ea-a69c-88f2208d19b3" width="80%" height="70%"> <br/>
1️⃣ 스트리머가 카메라로 실시간 스트리밍을 시작합니다. <br/>
2️⃣ 이때 스트리머는 사전에 OpenCV를 통해 얼굴 등록 과정을 거쳐 DB에 저장합니다.  <br/>
3️⃣ 백엔드 Flask 서버에서 이를 요청 받습니다. <br/>
4️⃣ Flask 서버 내부에서 Pytorch, OpenCV를 통해 일반 시민을 인식하고 모자이크를 진행합니다. <br/>
5️⃣ 일반 시민의 초상권이 보호된 스트리밍을 Rtmp 서버로 내보냅니다. <br/>
6️⃣ 시청자는 모자이크가 적용된 스트리밍을 앱에서 보게 됩니다. <br/>
<br/>


## 6장. Structure Internal Details 멀티 스트리밍 구조
- 내부적으로 모자이크가 진행되는 멀티 스트리밍 구조입니다. <br/>
- Hi-DN은 여러 명의 사용자가 동시에 스트리밍을 할 수 있도록 각 스트리밍에 고유 아이디를 부여하는 방식을 사용했습니다. <br/>
<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/24eac308-c08b-4397-bc2d-764c4c5f857e" width="80%" height="70%"> <br/>
<br/>

## 7장. AI Training Details
#### 학습 데이터 셋
: 총 약 100장 X 2배 증폭
- 스트리머 얼굴 데이터
<!-- 택배 운송장: 원본 1200장 × 3배 증폭
차량 번호판: 원본 1107장 × 3배 증폭
신분증: 원본 1141장 × 3배 증폭
백그라운드 이미지: 전체 데이터 셋의 10% -->

### 인공지능 모델 학습 결과
#### 인식률
- loss: 1% 미만
- mAP, precision과 recall: 평균 0.95 이상
  
<!-- ![image](https://github.com/kyounggseo/real-time-face/assets/102573192/bd5a3028-9aa6-433e-b746-469d45a82a43)
![image](https://github.com/kyounggseo/real-time-face/assets/102573192/ffc5857a-9eea-4f60-8694-56739991e5b8)-->

<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/268d82e7-584d-4606-9791-bfd15c9418d3" width="50%" height="70%"> <br/>


#### Confidence Check & Decision
- precision과 recall 에 대한 결과 그래프를 통해 백엔드에서 모자이크를 진행할 때 사용되는 객체 인식 confidence를 적정선인 0.6으로 결정하였습니다.  <br/>

<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/fc7c6b30-187f-4fd7-b31d-2d39682d7bd8" width="40%" height="60%">
<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/764e36b3-1503-4f08-8ccd-5f467daaf9f6" width="38%" height="60%">
<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/764e36b3-1503-4f08-8ccd-5f467daaf9f6" width="38%" height="60%">
<img src="https://github.com/kyounggseo/real-time-face/assets/102573192/5b49bdfe-46d2-4334-8cd0-417090d7ac2e" width="40%" height="50%">
<br/>

## 8장. More Details...
- MOSAINFO 프로젝트에 대한 더 자세한 설명이 궁금하시다면 다음 유튜브 영상을 참고해주시면 감사하겠습니다 😊 <br/>
[YouTube](https://www.youtube.com/watch?v=YUD-Zv0phgY)
