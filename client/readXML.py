import re
import codecs
import sys
from xml.etree.ElementTree import ElementTree, Element
from config import *


def read_xml(in_path):
    '''读取并解析xml文件
       in_path: xml路径
       return: ElementTree'''
    tree = ElementTree()
    tree.parse(in_path)
    return tree


def write_xml(tree, out_path):
    '''将xml文件写出
       tree: xml树
       out_path: 写出路径'''
    tree.write(out_path, encoding="utf-8", xml_declaration=True)


def if_match(node, kv_map):
    '''判断某个节点是否包含所有传入参数属性
       node: 节点
       kv_map: 属性及属性值组成的map'''
    for key in kv_map:
        if node.get(key) != kv_map.get(key):
            return False
    return True

#---------------search -----


def find_nodes(tree, path):
    '''查找某个路径匹配的所有节点
       tree: xml树
       path: 节点路径'''
    return tree.findall(path)


def get_node_by_keyvalue(nodelist, kv_map):
    '''根据属性及属性值定位符合的节点，返回节点
       nodelist: 节点列表
       kv_map: 匹配属性及属性值map'''
    result_nodes = []
    for node in nodelist:
        if if_match(node, kv_map):
            result_nodes.append(node)
    return result_nodes

#---------------change -----


def change_node_properties(nodelist, kv_map, is_delete=False):
    '''修改/增加 /删除 节点的属性及属性值
       nodelist: 节点列表
       kv_map:属性及属性值map'''
    for node in nodelist:
        for key in kv_map:
            if is_delete:
                if key in node.attrib:
                    del node.attrib[key]
            else:
                node.set(key, kv_map.get(key))


tree_lp = read_xml(lp_path)
tree_lc = read_xml(lc_path)


def getAttribList(nodePath, tree_xml=tree_lc):
    '''返回多个字典形成的列表'''
    nodelist = find_nodes(tree_xml, nodePath)
    attribList = []
    for node in nodelist:
        attribList.append(node.attrib)
    return attribList


def getAttrib(nodePath, node, tree_xml=tree_lc):
    '''yaoqiu input many nodes!!!返回属性的列表?'''
    l = getAttribList(nodePath, tree_xml=tree_lc)
    rl = []
    for i in range(0, len(l)):
        rl.append(l[i][node])
    return rl


def levelBasicInfo(levelId):
    maxLine = int(getAttrib('./level[@id="%d"]' % (levelId), 'maxLine')[0])
    startLine = int(getAttrib('./level[@id="%d"]' % (levelId), 'startLine')[0])
    return maxLine, startLine


def getElementByGrid(levelId):
    '''按格分层整理元素'''
    levelBasicInfo(levelId)
    ElementByGrid = [{}] * 9 * maxLine
    for y in range(0, maxLine):
        for x in range(0, 9):
            ElementByGrid[9 * y + x] = {}  # 初始化为空字典
            l = getAttribList(
                './level[@id="%d"]/grid[@x="%d"][@y="%d"]/basic' % (levelId, x, y))
            for i in l:
                key = i['layer']
                value = i['id']
                ElementByGrid[9 * y + x]["%s" % (key)] = "%s" % (value)
    return ElementByGrid

#print (getElementByGrid(0))


def getElementByLayer(levelId):
    '''按层整理元素'''
    levelBasicInfo(levelId)
    ElementByLayer = {
        '0': [None] * 9 * maxLine,
        '1': [None] * 9 * maxLine,
        '2': [None] * 9 * maxLine,
        '3': [None] * 9 * maxLine,
        '4': [None] * 9 * maxLine,
        '5': [None] * 9 * maxLine,
        '6': [None] * 9 * maxLine,
        '7': [None] * 9 * maxLine,
        '8': [None] * 9 * maxLine,
        '9': [None] * 9 * maxLine,
    }
    for y in range(0, maxLine):
        for x in range(0, 9):
            l = getAttribList(
                './level[@id="%d"]/grid[@x="%d"][@y="%d"]/basic' % (levelId, x, y))
            for i in l:
                key = i['layer']
                value = i['id']
                ElementByLayer['%s' % (key)][x + 9 * y] = value
    return ElementByLayer

level_ele = [
    [
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
    ],
    [
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None, 996, None, None, None, None, None, ],
        [None, None, None, None,  4, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
        [None, None, None, None,  3, None, None, None, None, None, ],
    ],
]
