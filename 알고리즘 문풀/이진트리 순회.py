import sys
N= int(sys.stdin.readline().strip())
tree = {}

def preorder(root):  # 전위 순회
    if root != '.':  # 루트 노드에 뭔가 있는 경우만 프린트
        print(root, end='')
        preorder(tree[root][0])  # 왼쪽을 루트로 해서 호출하고
        preorder(tree[root][1])  # 오른쪽을 루트로 해서 이를 호출한다.

def inorder(root):  # 중위 순회
    if root != '.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])


def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

for i in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left,right]

preorder('A')
print()
inorder('A')
print()
postorder('A')