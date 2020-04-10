init python:
    def addEnd(line):
        if line not in persistent.end:
            persistent.end.append(line)
            
screen hijikata_dd():
    tag menu
    text "你好，测试而已。"
