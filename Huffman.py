class Node:
    def __init__(self,freq):
        self.father = None
        self.left = None
        self.right = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


def create(item):
    return [Node(freq) for freq in item]

def HUFFMAN(nodes):
    queue = nodes[:]

    while len(queue) > 1:
        queue.sort(key=lambda item:item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)

    queue[0].father = None
    return queue[0]


def encode(nodes,root):
    binarycode = [''] * len(nodes)
    for i in range(len(nodes)):
        temp = nodes[i]
        while temp != root:
            if temp.isLeft():
                binarycode[i] = '0' + binarycode[i]
            else:
                binarycode[i] = '1' + binarycode[i]

            temp = temp.father
    return binarycode


def decode(code,name,binarycode):
    encode = ''
    decode = ''
    for i in range(len(code)):
        encode = encode + code[i]
        for j in zip(name,binarycode) :
            if encode == j[1]:
                decode = decode + j[0][0]
                encode = ''

    print("Decode = " + decode)


if __name__ == '__main__':

    C = []
    while True:
        while True:
            num = input("Input a number : ")
            if num == "0" :
                quit()
            try:
                if (int(num) <= 0 ) :
                    print("請輸入正整數!")
                    continue
                else:
                    break
            except:
                print("Error Input!")
                continue

        print("=== Input a char and frequency ===" )
        k = 1
        while k-1 != int(num):
            try:
                ch, fre = input("Input" + str(k) + ": ").split()
            except:
                print("Error Input!")
                continue
            if fre.isdigit() and len(ch) == 1 and ch.isalpha():
                try:
                    if (int(fre) <= 0):
                        print("請輸入正整數!")
                        continue
                    else:
                        C.append((ch,int(fre)))
                        k = k + 1
                except:
                    print("Error Input!")
                    continue
            else:
                print("Error Input!")
                continue

        done = False
        while done == False:
            done = True
            code = input("Input a binary code: ")
            for i, v in enumerate(code):
                if v != "0" and v != "1":
                    done = False
                    print("Error Input!")
                    break

        nodes = create([freq[1] for freq in C])
        root = HUFFMAN(nodes)
        codes = encode(nodes, root)
        for item in zip(C, codes):
            print(item[0][0], item[1])

        decode(code, C, codes)
        C = []
