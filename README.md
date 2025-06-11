# Team9_Gurumi Mutual Cloud System

**Gurumi**는 P2P 구조 기반의 분산 클라우드 실험용 프로젝트로, 수요자-공급자 간 안전한 작업 전송 및 처리를 실현하는 Mutual Cloud 모델입니다.

## 프로젝트 구조
Gurumi-Main/
├── common/ # 공통 설정 및 로깅, 유틸리티 모듈
├── demand_node/ # 수요자 노드 클라이언트 관련 모듈
├── supply_node/ # 공급자 노드 처리기 관련 모듈
├── requirements.txt # Python 의존 패키지 명세
├── run_demo.sh # 데모 실행 스크립트
├── GroundRule.md # 프로젝트 규칙 또는 설명 문서


## 실행 방법

1. Python 환경 설정 (Python 3.8 이상 추천)
2. 패키지 설치

```
pip install -r requirements.txt
```

3. 데모 실행
```
bash run_demo.sh
```

## 주요 기능 설명
수요자 노드 (demand_node/)

client.py: 작업을 서버로 전송하는 기본 클라이언트

client_safe.py: AES 암호화를 적용한 안전 전송 클라이언트

encryption.py: 암복호화 모듈

공급자 노드 (supply_node/)

processor.py: 작업 수신 후 실행 및 결과 반환 로직

encryption.py: 수신된 데이터를 복호화하는 모듈

공통 모듈 (common/)

config.py: 시스템 설정값 관리

logger.py: 실험 로깅 도구

utils.py: 기타 보조 기능

## 보안 구조
WireGuard 기반 암호화된 네트워크 통신

AES (pycryptodome) 기반 데이터 암호화

VM → WireGuard 라우팅을 통한 격리된 네트워크 환경

향후 Confidential Computing 기반 격리 확장 고려

## 참고 문서
GroundRule.md: 실험 가이드 및 규칙

기술 시나리오 및 구조 설명은 /docs 혹은 보고서 참조

## 팀 정보 및 기여자
금채원(2276029): 실험 전체 설계 및 코드 작성

이서영(2276218): 실험 영상 촬영 및 편집, UI 시나리오 테스트

송예린(2171023): 보안 구조 조사, 기술 확장 및 후속 전략 설계


