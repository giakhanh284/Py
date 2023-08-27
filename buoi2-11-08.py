size=4
def bar():
    print("#" + 4*size * "=" + "#")
def drawTopHalf():
    '''for line in range(1,5):
        print("|" + \
              " " * (-2 * line+8) + \
                "<>" +\
                "." *(4*line-4) +\
                "<>" +\
                " " *(-2*line +8) +\
                "|"
             ) '''
    for line in range(1,size+1):
        print("|" + " " *(-2 * line + 2*size)+ "<>" +"." *(4*line -4) +\
                 "<>" + " " *(-2 * line + 2*size)+ "|")
                 
def drawBottomHalf():
    '''for line in range(4,0,-1):
        print("|" + \
              " " * (-2 * line+8) + \
                "<>" +\
                "." *(4*line-4) +\
                "<>" +\
                " " *(-2*line +8) +\
                "|"
             )'''
    for line in range(size-1,0,-1):
        print("|" + " " *(-2 * line + 2*size)+ "<>" +"." *(4*line -4) +\
                 "<>" + " " *(-2 * line + 2*size)+ "|")
bar()
drawTopHalf()
drawBottomHalf()
bar()