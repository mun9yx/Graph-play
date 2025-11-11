# Knowledge Graph Toy Project

간단한 지식그래프(Knowledge Graph) 구조를 직접 구축하고 탐색하는 토이 프로젝트입니다.  
`networkx`를 활용하여 CSV 형태의 트리플 데이터를 그래프로 구성하고,  
`pyvis`를 이용해 인터랙티브 시각화(HTML)까지 수행합니다.

트리플의 기본적인 형태 파악과 networkx의 구조 살펴보는 용도입니다.

---

## 프로젝트 구조
kg-toy/
├── data/
│ └── triples.csv # (head, relation, tail) 형식의 샘플 데이터
├── src/
│ ├── build_kg.py # CSV → NetworkX 그래프 생성
│ ├── query_kg.py # 간단한 질의 예제 (출연작 탐색 등)
│ └── visualize_kg.py # 그래프 시각화 (Pyvis → HTML)
└── README.md

### 실행 순서
1. uv run src/build_kg.py
2. uv run src/query_kg.py
3. uv run src/visualize_kg.py

