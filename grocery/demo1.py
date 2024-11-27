
import re
import sys

# 格式化函数
def format_question(arg1):
    if not arg1:
        return "Invalid input format: argument is empty or None."

    # 使用正则表达式匹配题目和选项
    pattern = r"q:(.*?)\s+o_1:\s*(.*?)\s+o_2:\s*(.*?)\s+o_3:\s*(.*?)\s+o_4:\s*(.*)"


    # 使用正则表达式从 arg1 中提取题目和选项

    print(" === " * 10)
    match = re.search(pattern, arg1)
    print(" *** " * 10)


    if match:
        # 获取匹配到的内容
        q = match.group(1)  # 题目部分
        o_1 = match.group(2).strip()  # 选项 1
        o_2 = match.group(3).strip()  # 选项 2
        o_3 = match.group(4).strip()  # 选项 3
        o_4 = match.group(5).strip()  # 选项 4
        print(q)
        print(o_1)
        print(o_2)
        print(o_3)
        print(o_4)

        # 格式化输出为目标的 JSON 风格字符串
        formatted_string = (
            f'"q":"{q}", '
            f'"o_1":"{o_1}", '
            f'"o_2":"{o_2}", '
            f'"o_3":"{o_3}", '
            f'"o_4":"{o_4}"'
        )
        return formatted_string
    else:
        return "Invalid input format: does not match the expected pattern."

# 主函数
def main(arg):
    # 通过 sys.stdin.read() 获取输入，适用于不支持 input() 的环境
    arg1 =arg.strip()

    # 调用 format_question 函数进行格式化
    formatted_string = format_question(arg)

    # 打印格式化后的结果
    print(formatted_string)

# 调用主函数
if __name__ == "__main__":
    arg = "q:在设计三消游戏的牌面时，哪种颜色配置可以帮助用户更好地理解玩法？ o_1:A. 三种颜色 o_2:B. 四种颜色 o_3:C. 五种颜色 o_4:D. 六种颜色"
    main(arg)