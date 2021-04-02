#INPUT huffman tree, current code taken from edges
#OUTPUT build dictionary of words and code
#NOTHING is explicitly returned, it should fill in the dictionary d
#RECURSIVE FUNCTION


def make_code(xlst,code):
    #TODO: IMPLEMENT
    if len(xlst) > 0:
        return make_code(xlst[1:], code)
    else:
        pass


#INPUT list of word, count pairs
#OUTPUT huffman tree with a single node
#[node [0 or 1 [node]]]
def make_tree(xlst):
    #TODO: IMPLEMENT FUNCTION
    def smallest(xlst):
        min1 = xlst[0]
        min1num = xlst[0][0]
        xlst = xlst[1:] 
        while xlst:
            if xlst[0][0] < min1num:
                min1 = xlst[0]
                min1num = xlst[0][0]
            xlst = xlst[1:]
        return min1
    def intFirst(xlst):
        newlst = []
        while xlst:
            intCopy = xlst[0][1]
            letterCopy = xlst[0][0]
            xlst[0][0] = intCopy
            xlst[0][1] = letterCopy
            newlst += [xlst[0]]
            xlst = xlst[1:]
        return newlst
    xlst = intFirst(xlst)
    huff_tree = []
    while len(xlst) > 1:
        zeroNode = smallest(xlst)
        xlst.remove(zeroNode)
        oneNode = smallest(xlst)
        xlst.remove(oneNode)
        newNode = [zeroNode[0] + oneNode[0], [0, zeroNode], [1, oneNode]]
        huff_tree.append(newNode)
        xlst.append(newNode)
    return huff_tree

    
        



###DATA
xlst = [['w',7],['u',12],['x',15],['v',18],['y',20]]
d = {}
f = lambda x: x[1] if type(x[0]) == str else x[0]
xlst.sort(key=f) #sorts either original or new nodes 
print(xlst)

tree = make_tree(xlst)
print(tree)
print('#'*30)
print(tree[0])
print('#'*30)
print(tree[1])
print('#'*30)
print(tree[2])
print('#'*30)
print(tree[3])
d = make_code(xlst[0],"")
print(d)