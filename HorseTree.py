from Horse import Horse

class HorseTree:
    def __init__(self, Time, Name):
        self.root = Horse(Time, Name)

    def __RecursiveAddition(self, Node, Time, Name):
        if Time < Node.Time:
            if Node.Left is None:
                Node.Left = Horse(Time, Name)
            else:
                self.__RecursiveAddition(Node.Left, Time, Name)
        else:
            if Node.Right is None:
                Node.Right = Horse(Time, Name)
            else:
                self.__RecursiveAddition(Node.Right, Time, Name)

    def __OrderRecursive(self, Node):
        if Node is not None:
            self.__OrderRecursive(Node.Right)
            print(Node.Name, ": ", Node.Time)
            self.__OrderRecursive(Node.Left)
    
    def __Search(self, node, Time):
        if node is None:
            return None
        if node.Time == Time:
            return node
        if Time < node.Time:
            return self.__Search(node.Left, Time)
        else:
            return self.__Search(node.Right, Time)

    def Add(self, Time, Name):
        self.__RecursiveAddition(self.root, Time, Name)

    def OrderedPrint(self):
        print("Ordered Horse Tree: ")
        self.__OrderRecursive(self.root)
        print("")

    def Search(self, Time):
        return self.__Search(self.root, Time)