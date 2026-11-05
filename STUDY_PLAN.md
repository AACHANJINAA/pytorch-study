# 3주 PyTorch + CUDA 학습 계획

작성일: 2026-10-31

## 개요

3주 뒤 목표는 PyTorch 학습 루프를 직접 짤 수 있고, 직접 만든 CUDA 커널을 PyTorch에 붙인 미니 프로젝트 1개를 GitHub에 올리는 것이다.

| 항목 | 내용 |
| --- | --- |
| 기간 | 3주 (0일차 세팅 + 21일) |
| 하루 시간 | 3~4시간: PyTorch 2~3시간, CUDA 1시간 |
| 장비 | RTX 5060 Ti 16GB (Blackwell, CUDA 12.8 이상 필요) |
| 최종 결과물 | 미니 프로젝트 GitHub 저장소 (README, 결과 이미지, 속도 비교 표) |

진행 원칙

- 매일 코드를 직접 친다. 강의만 보는 날은 만들지 않는다.
- 밀리는 날은 CUDA를 줄이고 PyTorch 진도를 우선 지킨다.
- 매주 일요일은 밀린 과제를 채우는 버퍼로 쓴다.
- 하루 끝에 배운 것과 막힌 점을 3줄로 기록한다 (나중에 README와 면접 답변 재료가 된다).

## 0일차: 환경 세팅

GPU가 PyTorch와 CUDA 양쪽에서 인식되는 것까지 확인하면 끝이다.

- [x] 최신 NVIDIA 드라이버 설치, `nvidia-smi`로 GPU 이름과 VRAM(16GB) 확인
- [x] Python 3.10 이상 + 가상환경(venv) 만들기
- [x] pytorch.org에서 CUDA 12.8 이상 빌드로 PyTorch 설치 (현재 cu132)
- [x] `torch.cuda.is_available()` → True, `torch.cuda.get_device_name(0)` 출력 확인
- [x] numpy, matplotlib, jupyter, tensorboard 설치
- [ ] CUDA Toolkit 12.8 이상 설치, `nvcc --version` 확인
- [ ] Visual Studio (C++ 데스크톱 개발) 설치 — CUDA 빌드와 PyTorch extension에 필요
- [ ] CUDA 샘플(deviceQuery, vectorAdd) 빌드 후 실행
- [ ] GitHub 저장소 연결, `.gitignore` 작성

## 1주차: 기초 (Day 1~7)

주말까지 MNIST를 GPU로 학습시키고, CUDA로 행렬 곱 커널을 직접 짠다.

**Day 1 — Python/NumPy + Tensor**

- [ ] PyTorch: Python 문법(리스트, 클래스, 리스트 컴프리헨션), NumPy 배열 연산
- [ ] PyTorch: Tensor 생성, shape/dtype, 인덱싱, broadcasting, `.to("cuda")`
- [ ] CUDA: 호스트/디바이스 개념, `__global__` 함수로 Hello World 커널

**Day 2 — autograd**

- [ ] PyTorch: `requires_grad`, `backward()`, 계산 그래프, `torch.no_grad()`
- [ ] PyTorch: CPU vs GPU 행렬 곱 속도 비교 (4096×4096)
- [ ] CUDA: 스레드/블록/그리드, `threadIdx`, `blockIdx`, `blockDim`

**Day 3 — 학습 루프**

- [ ] PyTorch: 선형회귀를 직접 작성 (forward → loss → backward → step → zero_grad)
- [ ] PyTorch: 같은 모델을 `nn.Linear` + `optim.SGD`로 다시 작성
- [ ] CUDA: 벡터 덧셈 커널, `cudaMalloc` / `cudaMemcpy` / `cudaFree`

**Day 4 — nn.Module + DataLoader**

- [ ] PyTorch: `nn.Module` 상속으로 MLP 만들기
- [ ] PyTorch: torchvision MNIST + DataLoader(batch, shuffle)
- [ ] CUDA: 에러 체크 매크로, `cudaDeviceSynchronize`, cudaEvent로 시간 측정

**Day 5 — MNIST 완성**

- [ ] PyTorch: MNIST MLP 학습 + 검증 루프, 정확도 97% 이상
- [ ] PyTorch: `model.train()` / `model.eval()` 차이 정리
- [ ] CUDA: 2D 인덱싱, 이미지 흑백 변환 커널 (그래픽스 전공자에게 익숙한 예제)

**Day 6 — 도구 익히기**

- [ ] PyTorch: `torch.save` / `load_state_dict`, TensorBoard로 loss/accuracy 곡선
- [ ] CUDA: 단순(naive) 행렬 곱 커널 + CPU 결과와 검증

**Day 7 — 복습 / 버퍼**

- [ ] 밀린 과제 채우기
- [ ] Karpathy "Zero to Hero" 1편(micrograd) 시청
- [ ] 1주차 코드 GitHub 커밋, 배운 점 정리

## 2주차: 심화 (Day 8~14)

주말까지 CIFAR-10 CNN을 완성하고, 직접 짠 CUDA 커널을 PyTorch extension으로 불러온다.

**Day 8 — CNN 기초**

- [ ] PyTorch: Conv2d, 풀링, 채널/커널/stride/padding 계산
- [ ] PyTorch: CIFAR-10 로드, 간단한 CNN 학습 (목표 70%)
- [ ] CUDA: 메모리 계층 (global / shared / register), coalescing 개념

**Day 9 — 성능 올리기**

- [ ] PyTorch: 데이터 증강(flip, crop), BatchNorm, Dropout
- [ ] PyTorch: 학습률 스케줄러(CosineAnnealing), AdamW 비교
- [ ] CUDA: 공유 메모리 타일링 행렬 곱 구현

**Day 10 — 전이학습**

- [ ] PyTorch: 사전학습 ResNet18 불러와 CIFAR-10 파인튜닝 (목표 90%)
- [ ] CUDA: naive vs 타일링 행렬 곱 속도 비교 표 작성

**Day 11 — 평가와 시각화**

- [ ] PyTorch: confusion matrix, 틀린 예측 이미지 보기, 오버피팅 진단
- [ ] CUDA: reduction(배열 합) 커널, warp와 `__syncthreads`

**Day 12 — 프로파일링**

- [ ] PyTorch: `torch.profiler`로 병목 찾기, DataLoader `num_workers` / `pin_memory`
- [ ] CUDA: Nsight Systems / Nsight Compute로 내 커널 분석

**Day 13 — PyTorch extension**

- [ ] 공식 튜토리얼 "Custom C++ and CUDA Extensions" 따라하기
- [ ] `torch.utils.cpp_extension.load`로 내 커널(예: ReLU 또는 흑백 변환) 빌드 후 호출
- [ ] 결과가 PyTorch 기본 연산과 같은지 `torch.allclose`로 검증

**Day 14 — 복습 / 버퍼**

- [ ] extension에 backward(autograd.Function) 추가 시도
- [ ] Karpathy 2~3편 시청
- [ ] 3주차 프로젝트 주제 후보 2개 고르고 참고 코드 모으기

## 3주차: 미니 프로젝트 (Day 15~21)

주제는 스타일 트랜스퍼 또는 이미지 디노이징 오토인코더 중 하나를 골라, 일부 연산을 내 CUDA 커널로 바꾼 버전까지 완성한다.

**Day 15 — 주제 확정**

- [ ] 주제 1개 선택, 논문/블로그 1개 읽고 핵심 구조 요약
- [ ] 데이터셋 준비 (스타일 트랜스퍼: 콘텐츠/스타일 이미지, 디노이징: 원본 + 노이즈 추가)

**Day 16 — 베이스라인 구현**

- [ ] 모델 구조 + 손실 함수 작성 (스타일: VGG 특징 + Gram 행렬, 디노이징: U-Net 또는 Conv 오토인코더)
- [ ] 작은 데이터로 학습이 돌아가는지 확인

**Day 17 — 본 학습**

- [ ] 전체 학습, TensorBoard에 중간 결과 이미지 기록
- [ ] 하이퍼파라미터 2~3개 비교, 디노이징은 PSNR로 평가

**Day 18 — CUDA 커널 교체**

- [ ] 모델 내 연산 1개(활성화 함수, Gram 행렬, 가우시안 블러 필터 등)를 직접 만든 커널로 교체
- [ ] 결과 일치 검증 + 연산 시간 비교

**Day 19 — 최적화**

- [ ] `torch.autocast` + `GradScaler`로 mixed precision 적용
- [ ] FP32 vs mixed precision: 학습 시간, VRAM 사용량, 결과 품질 비교
- [ ] (선택) `torch.compile` 적용 전후 비교

**Day 20 — 데모**

- [ ] 이미지 넣으면 결과 나오는 추론 스크립트 (선택: Gradio 웹 데모)
- [ ] 전/후 비교 이미지 제작

**Day 21 — 포트폴리오 정리**

- [ ] README: 목표, 구조도, 결과 이미지, 속도 비교 표, 실행 방법
- [ ] 배운 점과 어려웠던 점 정리 (영어 면접 답변용 버전도 작성)
- [ ] 다음 목표 정하기 (아래 활용처 중 하나)

## 이 학습으로 할 수 있는 것

3주를 마치면 아래 프로젝트에 바로 도전할 수 있고, 추가 학습 양에 따라 난이도를 나눠두었다. 그래픽스·게임 전공과 직접 연결되는 것부터 정렬했다.

### 그래픽스 / 렌더링

| 할 수 있는 것 | 내용 | 추가로 필요한 것 | 난이도 |
| --- | --- | --- | --- |
| 렌더링 디노이저 | 샘플 수 적은 레이트레이싱 이미지의 노이즈 제거 | U-Net, 렌더러에서 G-buffer 추출 | 중 |
| 업스케일링 (DLSS 닮은 프로젝트) | 저해상도 프레임을 고해상도로 복원 | ESRGAN 계열 모델, 모션 벡터 개념 | 중 |
| 텍스처 생성 / 스타일 변환 | 게임 에셋에 아트 스타일 적용, 타일링 텍스처 생성 | 3주차 프로젝트 확장 | 하 |
| NeRF | 사진 여러 장으로 3D 장면 복원 | 볼류메트릭 렌더링, 포지셔널 인코딩 | 상 |
| 3D Gaussian Splatting | 실시간으로 렌더되는 3D 장면 복원 | CUDA 래스터라이저 이해 (CUDA 공부가 직접 쓰임) | 상 |
| 뉴럴 머티리얼 / 뉴럴 텍스처 압축 | 작은 네트워크로 BRDF나 텍스처를 표현 | 셰이더에서 MLP 추론 | 상 |

### 게임 AI

| 할 수 있는 것 | 내용 | 추가로 필요한 것 | 난이도 |
| --- | --- | --- | --- |
| 강화학습 에이전트 | 간단한 게임(벽돌 깨기, 퐁)을 스스로 풀기 | Gymnasium, DQN / PPO | 중 |
| Unity ML-Agents | Unity 게임 안에서 NPC를 학습 | Unity, ML-Agents 툴킷 | 중 |
| 학습한 모델을 엔진에 붙이기 | PyTorch 모델을 ONNX로 내보내 C++ 엔진에서 추론 | ONNX Runtime 또는 TensorRT | 중 |
| 애니메이션 생성 | 모션 데이터로 캐릭터 동작 예측 | 시퀀스 모델(Transformer) | 상 |

### GPU / 최적화

| 할 수 있는 것 | 내용 | 추가로 필요한 것 | 난이도 |
| --- | --- | --- | --- |
| 커스텀 CUDA 연산 만들기 | PyTorch에 없는 연산을 빠르게 구현 | 2주차 extension 확장 | 하 |
| 이미지 처리 커널 라이브러리 | 블러, 엣지 검출, 톤매핑을 CUDA로 | 컨볼루션 최적화 | 하 |
| Triton 커널 | Python으로 GPU 커널 작성 (`torch.compile` 내부 기술) | OpenAI Triton | 중 |
| 추론 가속 | 모델 양자화(INT8/FP8), TensorRT 변환 | TensorRT, 양자화 개념 | 중 |
| CUDA–그래픽스 API 연동 | D3D/OpenGL 텍스처를 CUDA로 바로 처리 (복사 없이) | CUDA Graphics Interop | 중 |

### 일반 AI

| 할 수 있는 것 | 내용 | 추가로 필요한 것 | 난이도 |
| --- | --- | --- | --- |
| 이미지 분류기 서비스 | 내 데이터로 전이학습 후 웹 데모 | Gradio / FastAPI | 하 |
| 객체 탐지 | 사진이나 게임 화면에서 물체 찾기 | YOLO 계열 모델 | 중 |
| 미니 GPT | 글자 단위 텍스트 생성 모델 직접 학습 | Karpathy nanoGPT, Transformer | 중 |
| LLM 파인튜닝 | 작은 오픈 모델을 LoRA로 학습 (16GB면 더 수월) | Hugging Face, PEFT | 중 |
| 이미지 생성 | 작은 확산 모델을 처음부터 학습 | Diffusion 이론 | 상 |

### 취업에서 어필할 수 있는 것

- 게임 엔진 / 그래픽스 프로그래머: 뉴럴 렌더링, GPU 최적화 경험
- GPU / 고성능 컴퓨팅 엔지니어: 직접 짠 CUDA 커널과 프로파일링 결과
- AI 엔지니어 (비전 / 추론 최적화): PyTorch 학습 + 배포까지 해본 프로젝트
- 면접에서 자주 나오는 주제: 메모리 계층, coalescing, 공유 메모리 최적화, 역전파 원리 — 모두 이 계획에 포함되어 있다

3주 후 추천 다음 단계는 렌더링 디노이저 또는 3D Gaussian Splatting이다. 그래픽스 전공, PyTorch, CUDA를 한 프로젝트에서 모두 보여줄 수 있다.

## 참고 자료

| 자료 | 쓰는 시기 |
| --- | --- |
| [PyTorch 공식 튜토리얼](https://pytorch.org/tutorials/) — Learn the Basics | 1주차 |
| [PyTorch 설치 페이지](https://pytorch.org/get-started/locally/) | 0일차 |
| [NVIDIA CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) | 1~2주차 |
| PyTorch 튜토리얼 — Custom C++ and CUDA Extensions | 2주차 Day 13 |
| Andrej Karpathy, Neural Networks: Zero to Hero (YouTube) | 1~2주차 복습일 |
| Stanford CS231n 강의 노트 | CNN 이론 보충 |
| Nsight Systems / Nsight Compute 문서 | 2주차 Day 12 |
