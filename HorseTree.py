from Horse import Horse

class HorseTree:
    def __init__(self, Points, Name):
        self.root = Horse(Points, Name)

    def __RecursiveAddition(self, Node, Points, Name):
        if Points < Node.Points:
            if Node.Left is None:
                Node.Left = Horse(Points, Name)
            else:
                self.__RecursiveAddition(Node.Left, Points, Name)
        else:
            if Node.Right is None:
                Node.Right = Horse(Points, Name)
            else:
                self.__RecursiveAddition(Node.Right, Points, Name)

    def __OrderRecursive(self, Node):
        if Node is not None:
            self.__OrderRecursive(Node.Right)
            print(Node.Name, ": ", Node.Points, "pts")
            self.__OrderRecursive(Node.Left)
    
    def __Search(self, node, Points):
        if node is None:
            return None
        if node.Points == Points:
            return node
        if Points < node.Points:
            return self.__Search(node.Left, Points)
        else:
            return self.__Search(node.Right, Points)

    def Add(self, Points, Name):
        self.__RecursiveAddition(self.root, Points, Name)

    def OrderedPrint(self):
        print("Ordered Horse Tree: ")
        self.__OrderRecursive(self.root)
        print("")

    def Search(self, Points):
        return self.__Search(self.root, Points)