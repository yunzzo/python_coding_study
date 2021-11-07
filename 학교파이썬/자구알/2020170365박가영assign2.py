from typing import List
from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0,next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heapStructure = []
        rootNode = ListNode()
        result = rootNode
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heapStructure,(lists[i].val,i,lists[i]))
        while heapStructure:
            oneNode = heapq.heappop(heapStructure)
            index = oneNode[1]
            result.next = oneNode[2]
            result = result.next
            if result.next: 
                heapq.heappush(heapStructure,(result.next.val,index,result.next))
        return rootNode.next


if __name__ == "__main__":
    data = [[1,4,5],[1,3,4],[2,6]]
    lists=[]
    for i in range(len(data)):
        root=head = ListNode(data[i][0])
        for j in range(1, len(data[i])):
            new = ListNode(data[i][j])
            head.next = new
            head = new
        lists.append(root)
    merge1 = Solution()
    result = merge1.mergeKLists(lists)
    while result:
        print(f'{result.val} --> ', end ='')
        result = result.next