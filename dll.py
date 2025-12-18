class Node:
    def __init__(self,val):
        val=val
        next=None
        prev=None

class dll:
    def __init__(self,val):
        head=Node(-1,None,None)
        tail=Node(-1,None,None)
        head.next=tail
        tail.prev=head
       
    def delete(node):
        pre=node.prev      
        nex=node.next
        pre.next=nex 
        del node
        #delete node
    def inser_node_at_end(self,node):
        prev=self.tail.prev
        prev.next=node
        node.next=self.tail
        self.tail.prev=node

from collections import defaultdict
class RegisterDemo:
    def __init__():
        mapper=defaultdict(None)
        dll=dll()
    def register(self,user_id):

        if self.mapper[user_id]:
            #dll
            self.dll.delete(node)
        else:
            self.mapper[user_id]=Node()





