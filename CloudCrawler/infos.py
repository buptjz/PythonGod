# -*- coding: utf-8 -*-
#!/usr/bin/env python

#Constant Variables

#云岗 error1
PLACES = ['延庆','八达岭','定陵','昌平','北部新区','植物园','古城','门头沟','云岗','房山','琉璃河','万柳','丰台花园','西直门北','官园',\
          '万寿西宫','南三环','大兴','榆垡','奥体中心','东四','前门','天坛','永定门内','农展馆','东四环','亦庄',\
          '永乐店','通州','顺义','怀柔','密云','密云水库','平谷','东高村']

ITEMSCHECK  = ['PM2.5','PM10','SO2','NO2','O3','CO']

GETDETAILURL = 'http://zx.bjmemc.com.cn/ashx/Data.ashx?Action=GetWRWInfo_ByStationAndWRWType'
GetGENERALURL = "http://zx.bjmemc.com.cn/ashx/Data.ashx?Action=GetIAQIAll_ByStation"

DISPLAYINFO = "使用流程：\n1、选择将要写入的EXCEl文件\n2、点击获取数据\n\n提示：\n程序默认在EXCEL的SHEET中没有数据的一列写入数据\n需要手动填写日期\n"