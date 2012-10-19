class FruitListNode:
    def __init__(self,data):
        #initiates the data member
        self.data=data
        self.tail=None
    def SetHead(self,node):
        node.tail=self
    def SetTail(self,node):
        self.tail=node
        
def TraverseFruitList(Node):
    while Node!=None:
        print(Node.data)
        Node=Node.tail

Node1=FruitListNode("Guava")
Node2=FruitListNode("Apple")
Node3=FruitListNode("Chico")
Node4=FruitListNode("Mango")
Node5=FruitListNode("Jackfruit")
Node6=FruitListNode("Banana")


Node2.SetTail(Node6)
Node6.SetTail(Node3)
Node3.SetTail(Node1)
Node1.SetTail(Node5)
Node5.SetTail(Node4)

TraverseFruitList(Node2)
