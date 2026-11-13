import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

def lihat(kode):
    tree = parser.parse(kode.encode())
    print(kode.strip())
    print("  ->", tree.root_node)
    print()

lihat("x = 1")
lihat("nama = 99")