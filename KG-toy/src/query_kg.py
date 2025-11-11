import networkx as nx
from build_kg import load_triples
from IPython import embed

def get_acted_in(G:nx.MultiDiGraph,actor:str):
    result = []
    for _, tgt,data in G.out_edges(actor,data=True): #actor에서 나가는 엣지
        if data.get('relation') == 'acted_in':
            result.append(tgt)
    # embed(color='Linux'); exit(1) ''디버깅용도''
    return result

if __name__ == '__main__':
    G = load_triples('data/triple.csv')
    works = get_acted_in(G,'이정재')
    print('이정재 출연직', works)