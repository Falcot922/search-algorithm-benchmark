import networkx as nx
import matplotlib.pyplot as plt

def hierarchy_pos(G, root):
    def _hierarchy_pos(G, root, leftmost, width, vert_gap, vert_loc, pos, parent=None):
        children = list(G.neighbors(root))
        if parent is not None and root in children:
            children.remove(root)

        if len(children) != 0:
            dx = width / len(children)
            nextx = leftmost
            for child in children:
                pos = _hierarchy_pos(G, child, nextx, dx, vert_gap, vert_loc - vert_gap, pos, root)
                nextx += dx
        pos[root] = (leftmost + width/2, vert_loc)
        return pos

    return _hierarchy_pos(G, root, 0, 1, 0.12, 1, {})


# --- Création d'un arbre binaire de profondeur 6 ---
G = nx.DiGraph()

def add_children(parent, depth, max_depth):
    if depth > max_depth:
        return
    left = f"{parent}L"
    right = f"{parent}R"
    G.add_edge(parent, left)
    G.add_edge(parent, right)
    add_children(left, depth+1, max_depth)
    add_children(right, depth+1, max_depth)

# profondeur 6
root = "A"
add_children(root, 1, 6)

# --- Plot ---
pos = hierarchy_pos(G, root)

plt.figure(figsize=(12, 12))
nx.draw(
    G, pos,
    with_labels=False,
    node_size=300,
    node_color="lightblue",
    arrows=False
)
plt.title("Arbre binaire profondeur 6")
plt.show()
