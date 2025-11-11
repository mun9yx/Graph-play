import pandas as pd
import networkx as nx
from IPython import embed

def load_triples(path:str) -> nx.MultiDiGraph: #매개변수는 문자형, 반환값은 그래프라는 것을 알려줌
    df = pd.read_csv(path)
    # embed(color='Linux'); exit(1)
    G = nx.MultiDiGraph() #그래프 객체 생성

    for _, row in df.iterrows(): #데이터프레임을 한 줄씩 순회하며 엔티티, 관계 생성
        h,r,t = row['head'], row['relation'], row['tail']
        G.add_node(h,label='entity')
        G.add_node(t,label='entity')
        G.add_edge(h,t,relation=r)
    return G #그래프 반환

if __name__ == '__main__': #이 파일을 직접 실행할 때만 아래 코드를 실행
    G = load_triples('data/triple.csv')
    print(f'nodes: {len(G.nodes())} edges: {len(G.edges())}')

