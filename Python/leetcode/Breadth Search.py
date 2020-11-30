# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
lsVal = []
explored = []
nodeStack = []

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        if t not in explored:
            explored.append(t)
            if (t.left != None)&(t.right != None):
                nodeStack.append(t.left)
                nodeStack.append(t.right)
            elif(t.left == None)&(t.right!=None):
                nodeStack.append(None)
                nodeStack.append(t.right)
            elif(t.left != None)&(t.right==None):
                nodeStack.append(t.left)
                nodeStack.append(None)

        if nodeStack != []:
            nxtNode = nodeStack.pop(0)
            if nxtNode != None:
                s = self.tree2str(nxtNode)
            else:
                lsVal.append(None)
        elif nodeStack == []:
            print("hai")

        return s
