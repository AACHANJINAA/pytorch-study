# pytorch-study

PyTorch + CUDA 3주 학습용 폴더. 목표는 PyTorch 학습 루프를 직접 작성하고, 직접 만든 CUDA 커널을 PyTorch에 붙인 미니 프로젝트 1개를 완성해 GitHub 포트폴리오로 올리는 것.

- 학습 계획(날짜별 체크리스트): [STUDY_PLAN.md](STUDY_PLAN.md)
- 기간: 3주 (0일차 세팅 + 21일), 하루 3~4시간 (PyTorch 2~3시간, CUDA 1시간)
- 1주차: PyTorch 기초(Tensor, autograd, 학습 루프, MNIST) + CUDA 기초(스레드/블록, 벡터 덧셈, 행렬 곱)
- 2주차: CNN(CIFAR-10, 전이학습) + CUDA 심화(공유 메모리, reduction, Nsight) + PyTorch C++/CUDA extension
- 3주차: 미니 프로젝트(스타일 트랜스퍼 또는 이미지 디노이징) + 일부 연산을 직접 만든 CUDA 커널로 교체 + mixed precision

## 진행 상황

- [x] 0일차: 드라이버, Python, 가상환경, PyTorch 설치 및 GPU 인식 확인 (2026-11-05)
- [x] numpy, matplotlib, jupyter, tensorboard 설치
- [x] 폴더를 `C:\Users\ckswl\Desktop\GITHUB\pytorch-study`로 이동 후 가상환경 재구성, GPU 재확인
- [ ] 0일차 남은 것: CUDA Toolkit 12.8+, Visual Studio C++ 워크로드
- [ ] 1주차 Day 1 시작

## 환경

| 항목 | 값 |
| --- | --- |
| OS | Windows (x64) |
| GPU | NVIDIA GeForce RTX 5060 Ti 16GB (Blackwell) |
| 드라이버 | 610.88 (CUDA 13.3까지 지원) |
| Python | 3.13.14 (Microsoft Store 버전) |
| 가상환경 | `.venv` (이 폴더 안) |
| torch | 2.15.0+cu132 |
| torchvision | 0.29.2+cu132 |
| torchaudio | 2.11.0+cu128 (torch와 버전 불일치, 아래 참고) |
| 에디터 | VS Code, 인터프리터 `.venv\Scripts\python.exe` |

GPU 확인 결과 (`check_pytoch.py`): `torch.cuda.is_available()` = True, GPU에서 행렬 곱 정상 동작.

## 폴더 구조

```
pytorch-study/
├─ .venv/              가상환경 (Git에 올리지 않음)
├─ check_pytoch.py     GPU/PyTorch 설치 확인 스크립트
├─ STUDY_PLAN.md       3주 학습 계획 (날짜별 체크리스트, 활용처, 참고 자료)
└─ README.md           이 파일
```

앞으로 추가 예정: `week1/`, `week2/`, `week3/`, `cuda/` (CUDA 커널 실습), `requirements.txt`

## 사용법

터미널을 새로 열 때마다:

```
cd C:\Users\ckswl\Desktop\GITHUB\pytorch-study
.venv\Scripts\activate
```

프롬프트 앞에 `(.venv)`가 붙으면 준비 완료. VS Code에서는 Ctrl+Shift+P → `Python: Select Interpreter` → `.venv` 선택.

## 환경 재구성 (새 PC 또는 폴더 이동 시)

`.venv`는 만든 위치의 절대 경로가 박혀 있어서 폴더를 옮기면 깨진다. 옮긴 뒤에는 `.venv`를 지우고 다시 만든다.

```
python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu132
pip install numpy matplotlib jupyter tensorboard
python check_pytoch.py
```

(RTX 5060 Ti는 CUDA 12.8 이상 빌드가 필요. cu118, cu126 빌드는 GPU 인식 안 됨.)

`requirements.txt`를 만들어 두면 더 편하다: `pip freeze > requirements.txt` → 나중에 `pip install -r requirements.txt`.

## 메모

- torchaudio가 torch와 다른 버전(cu128)으로 설치되어 있음. 이 계획에서는 쓰지 않지만, import 오류가 나면 torch와 같은 인덱스(cu132)로 다시 설치하거나 제거.
- Git 사용 시 `.gitignore`에 `.venv/`, `__pycache__/`, `runs/`(TensorBoard 로그), `data/`(데이터셋) 추가.
