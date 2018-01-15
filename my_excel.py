import os
import xlwt
import io



def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    return style


def write_excel():
    # 创建工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建sheet
    data_sheet = workbook.add_sheet('demo')
    rown = [(u'字段名称', u'大致时段', 'CRNTI', 'CELL-ID', 'test')]
    row1 = [(1, 2, 3, 4, 5), (4, 5, 6, 4, 3), (5, 6, 4, 3, 2)]
    rown.extend(row1)


    # 生成第一行和第二行
    for i in range(len(rown)):
        for j in range(len(rown[i])):
            # print(i,j)
            data_sheet.write(i, j, rown[i][j], set_style('Times New Roman', 220, True))

    # for i in range(len(row0)):
    #     for j in rown:
    #         data_sheet.write(i, j, rown[j], set_style('Times New Roman', 220, True))
    #         # data_sheet.write(1, i, row1[i], set_style('Times New Roman', 220, True))

        # 保存文件
    # sio = io.StringIO()
    # workbook.save(sio)
    workbook.save('/Users/liying/Documents/task/my_practice/demo.xls')


if __name__ == '__main__':
    write_excel()
