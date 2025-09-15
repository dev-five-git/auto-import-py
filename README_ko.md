# Auto Import Py

디렉토리 구조에서 Python 모듈을 자동으로 임포트하는 라이브러리입니다.

[English](README.md) | 한국어

## 기능

- 📁 디렉토리 구조에서 모든 Python 모듈을 자동으로 임포트
- 🔄 하위 디렉토리를 재귀적으로 탐색
- ⚙️ 임포트된 모듈 객체의 리스트를 반환
- 🚀 간단하고 가벼운 구현
- 🛣️ 모든 디렉토리 구조에서 작동

## 설치

```bash
pip install auto-import-py
uv add auto-import-py
```

## 사용법

### 기본 사용법

```python
from auto_import import auto_import
from pathlib import Path

# 현재 디렉토리에서 모든 모듈 임포트
modules = auto_import()

# 특정 디렉토리에서 모든 모듈 임포트
modules = auto_import("my_modules")

# Path 객체로 모듈 임포트
modules = auto_import(Path("src/components"))
```

### 디렉토리 구조 예시

```
my_modules/
├── users.py          # 임포트됨
├── items.py          # 임포트됨
├── __init__.py       # 필터링됨
└── v1/
    ├── admin.py      # 임포트됨
    └── __init__.py   # 필터링됨
```

### 모듈 파일 예시

```python
# my_modules/users.py
def get_users():
    return {"users": []}

def create_user(name: str):
    return {"name": name, "id": 1}

# my_modules/items.py
class Item:
    def __init__(self, name: str):
        self.name = name

def get_items():
    return [Item("item1"), Item("item2")]
```

### 임포트된 모듈 사용하기

```python
from auto_import import auto_import

# 모든 모듈 임포트
modules = auto_import("my_modules")

# 임포트된 모듈의 함수와 클래스에 접근
for module in modules:
    print(f"모듈: {module.__name__}")
    
    # 모듈의 모든 함수 가져오기
    functions = [attr for attr in dir(module) if callable(getattr(module, attr)) and not attr.startswith('_')]
    print(f"함수: {functions}")
    
    # 모듈의 모든 클래스 가져오기
    classes = [attr for attr in dir(module) if isinstance(getattr(module, attr), type) and not attr.startswith('_')]
    print(f"클래스: {classes}")
```

### 고급 사용법

```python
from auto_import import auto_import
import inspect

# 모듈을 임포트하고 내용 검사
modules = auto_import("src")

for module in modules:
    print(f"\n=== {module.__name__} ===")
    
    # 모든 호출 가능한 객체 가져오기
    for name, obj in inspect.getmembers(module, callable):
        if not name.startswith('_'):
            print(f"호출 가능: {name}")
    
    # 모든 클래스 가져오기
    for name, obj in inspect.getmembers(module, inspect.isclass):
        if not name.startswith('_'):
            print(f"클래스: {name}")
```

## API 참조

### `auto_import(dir_path: Path | str = ".") -> list[ModuleType]`

지정된 디렉토리에서 모든 Python 모듈을 자동으로 임포트합니다.

**매개변수:**
- `dir_path` (Path | str): 모듈을 임포트할 디렉토리 경로 (기본값: ".")

**반환값:**
- `list[ModuleType]`: 임포트된 모듈 객체의 리스트

**동작:**
1. 지정된 디렉토리를 재귀적으로 탐색
2. 모든 `.py` 파일을 찾음
3. `importlib.import_module`을 사용하여 각 모듈을 임포트
4. 성공적으로 임포트된 모듈의 리스트를 반환

**참고:** 디렉토리가 존재하지 않으면 빈 리스트를 반환합니다.

## 개발

### 의존성 설치

```bash
# 개발 의존성 설치
uv sync
```

### 테스트 실행

```bash
# 모든 테스트 실행
uv run pytest
```

### 코드 품질 검사

```bash
# 린팅
ruff check src/ tests/

# 포맷팅
ruff format src/ tests/
```

## 라이선스

이 프로젝트는 아파치 라이선스 2.0 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여

버그 리포트, 기능 요청, 풀 리퀘스트를 환영합니다! 기여하기 전에 이슈를 먼저 생성해 주세요.

## 작성자

- **owjs3901** - *초기 작업* - [owjs3901@gmail.com](mailto:owjs3901@gmail.com)