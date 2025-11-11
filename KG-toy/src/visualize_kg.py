from pyvis.network import Network
from build_kg import load_triples

def visualize_graph(G, output_path="docs/kg_graph.html"):
    # pyvis 네트워크 생성
    net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white", directed=True)

    # networkx 그래프의 노드/엣지 추가
    for node in G.nodes():
        net.add_node(node, label=node, title=node, color="#6fa8dc")

    for u, v, data in G.edges(data=True):
        relation = data.get("relation", "")
        net.add_edge(u, v, label=relation, color="#f6b26b")

    # 인터랙티브 HTML 파일로 저장
    net.write_html(output_path)
    print(f" 그래프 시각화 저장 완료: {output_path}")

if __name__ == "__main__":
    G = load_triples("data/triple.csv")
    visualize_graph(G)
