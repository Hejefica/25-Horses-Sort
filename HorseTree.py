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

    def Add(self, Time, Name):
        self.__RecursiveAddition(self.root, Time, Name)

    def OrderedPrint(self):
        print("Ordered Horse Tree: ")
        self.__OrderRecursive(self.root)
        print("")
