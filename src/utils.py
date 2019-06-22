def printArrayMirrored(V):
    width,height = V.shape
    for j in range(0, height):
        for i in range(0, width):
            item = V[i, height-1-j]
            numberFormat = "{:.4f}" if item < 0 else " {:.4f}"
            printToFile(numberFormat.format(item) + '     ')
        printToFile("\n\n")

outputFile = open("build/outt.out", "w+")
def printToFile(content):
    outputFile.write(content)