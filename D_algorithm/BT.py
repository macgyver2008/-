class BTElement:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def  __init__(self):
        self.root = None




    def insert(self, value):
        node = BTElement(value, None, None)
        if self.root is None:
            self.root = node
            return
        curr = self.root
        while True:
            if value >= curr.value :
                if curr.right is None:
                    curr.right = node
                    return
                curr = curr.right
            else:
                if curr.left is None:
                    curr.left = node
                    return
                curr = curr.left
    def find(self, value):
        curr = self.root
        while curr is not None:
            if curr.value > value:
                if curr.left is None:
                    return None
                curr = curr.left
            if curr.value < value:
                if curr.right is None:
                    return None
                curr = curr.right
        return False

    def delete(self, value):
        if self.find(value) == False:
            pass
        parent = None
        curr = self.root
        while curr:
            if curr.value == value:
                if curr.right is None and curr.left is None: #자식노드 없을때
                    if parent.left == curr:
                        parent.left = None
                    else:
                        parent.right =None
                    return curr.value
                elif(curr.right is None and curr.left is not None):  #오른쪽 자식노드 없을때
                    if parent.left == curr:
                        parent.left = curr.left
                    else:
                        parent.right = curr.left
                elif curr.right is not None and curr.left is None: #왼쪽 자식노드 없을때
                    if parent.left == curr:
                        parent.left = curr.right
                    else:
                        parent.right = curr.right
                else:# 양쪽 자식노드 있으때
                    # 루속자 찾는 과정
                    ret_value = curr.value #리턴 삭제한값 저장
                    succ_p = None #후속자 부모
                    succ = curr.left#후속자 삭제할 경우 서브트리에서 찾는다
                    while succ.right is not None:
                        succ_p = succ
                        succ = succ.right
                    curr.value = succ.value  #삭제한 노드의 위치에 후속자의 값 복사
                    succ_p.right = succ.left # 후속자와 후속자 부모의 연결을 끊고 왼쪽 자식을 컨넥트(None도됨)
                return curr.vlaue
            elif curr.vlaue < value :
                parent = curr
                curr = curr.right
            else:
                parent = curr
                curr = curr.left
        return None
                
