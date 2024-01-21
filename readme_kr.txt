1. 프로그램 명칭
: 수딩 사운드 생성 프로그램

2. 본 프로그램 특징
    - 5개의 각기 다른 노이즈를 생성하는 프로그램
    - 총 3개의 함수로 구성되어 있으며 노이즈 샘플 생성, Bandpass 필터 적용과 생성된 샘플을 저장하는 함수
    - 생성한 노이즈는 wav 파일 형태로 저장

3. 주요 기능
    - 노이즈의 Sampling rate 및 생성되는 샘플의 길이를 구성할 수 있음
    - 3개의 Weighting Filter를 사용가능
    - 샘플을 저장할때 소리의 크기를 지정할 수 있음 (db)


4. 사용 방법
    - 각 함수는 단계적으로 사용
    - noise_generator.ipynb 파일을 실행하여 아래 모든 과정을 테스트해볼 수 있음

1) main.py

    1) generate_sample: 노이즈의 샘플을 생성
        - sec: 생성될 노이즈의 시간
        - sample_rate: 샘플링 레이트
        - color: 노이즈의 컬러
        - weight: 웨이팅 필터의 종류 

    2) bandpass_filter: 주파수 대역 단위에서 필터링
        - samples: 생성한 샘플
        - lowcut: 이 주파수 보다 낮은 음역은 필터링함
        - highcut: 이 주파수 보다 높은 음역을 필터링함

    3) save_sample: 샘플을 wav 파일로 저장함
        - samples: 생성한 샘플
        - db: 소리의 크기 정도
        - file_name: 저장할 파일 이름
