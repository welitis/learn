# 2.写一个函数get_chinese_char_count(s),此函数返回
#     一个字符串s中所有中文字符的个数
#         def get_chinese_char_count(x)
#     注：    
#         中文编码范围是：0x4e00-0x9fa5(包含)
def get_chinese_char_count(s):
    l = []
    for x in list(s):
        if ord(x) in range(0x4e00,0x9fa6):
            l.append(x)
    return len(l)
print(get_chinese_char_count('asd爱你哟！'))
        