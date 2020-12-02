# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# f_con = open('test_copy.txt')
# print(f_con.read())
with open('web.png', 'rb') as rf:
    with open('web_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
