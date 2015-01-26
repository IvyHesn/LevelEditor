choose_area = None  # 0翻页，1行数，2盘面，3元素，4文件操作

# 需要变量来分别记录盘面和元素区域的点选情况
choose_board_grid = [None, None]
choose_ele_grid = [None, None]
grid_ele = [
    [69, 24, 59, 60, 152, 998, 0, 1, 2, 3, 4, 5, 996, ],
    [51, 52, 53, 54, None, None, 6, 9, 12, 15, 18, 21, None, ],
    [101, 102, 103, 104, None, None, 7, 10, 13, 16, 19, 22, None, ],
    [56, 61, 55, 58, 57, 999, 8, 11, 14, 17, 20, 23, None, ],
    [105, 106, 107, 108, 151, None, 70, 71, 72, 73, 74, 75, 995, ],
    [109, 110, 111, 112, 113, None, 76, 77, 78, 79, 80, 81, 992, ],
    [114, 115, 116, 117, 118, None, 82, 83, 84, 85, 86, 87, 993, ],
    [119, 120, 121, 122, 123, 124, 88, 89, 90, 91, 92, 93, 994, ],
]

choose_ele = None

lp_path = './levelProperty.xml'
lc_path = './levelsCleanUp.xml'
levelId = 0
maxLine = 9
startLine = 0

kv_map = {
    '51': {'id': '51', 'layer': '1', 'objectType': '1', 'picType': '0'},
    '52': {'id': '52', 'layer': '1', 'objectType': '1', 'picType': '1'},
}
