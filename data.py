lines = []
with open('./data.txt', 'r',encoding='UTF-8') as f:
    data1 = f.readlines()
tmp = ''
for line in data1:
    if line[0] >= '1' and line[0] <= '9' :
        # print(tmp)
        lines.append(tmp)
        tmp = ''
        tmp += line
    else:
        tmp += line
lines.remove('')
lines.append(tmp)

for i in range(9):
    lines[i] = lines[i][2:]
for i in range(9,48):
    # print(lines[i])
    lines[i] = lines[i][3:]

# print(lines[9])

ans = []
with open('./data2.txt', 'r',encoding='UTF-8') as f:
    data1 = f.readlines()
tmp = ''
for line in data1:
    if line[0] >= '1' and line[0] <= '9' :
        # print(tmp)
        ans.append(tmp)
        tmp = ''
        tmp += line
    else:
        tmp += line
ans.remove('')
ans.insert(32,' ')
ans.append(tmp)
# print(len(ans),ans[32])

merged_list = sorted(zip(lines, ans))

# 打印排序后的列表
for it in merged_list:
    for i in it:
        if i == '\n':
            print()
        else :
            print(i)

# print(merged_list)
# for item in merged_list:
#     print(item)

