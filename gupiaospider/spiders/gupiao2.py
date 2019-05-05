 # -*- coding: utf-8 -*-
import random

import scrapy
import time
import json
import os

from gupiaospider.items import GupiaospiderItem
from gupiaospider.spiders.gupiao import GupiaoSpider


class GupiaoSpider(scrapy.Spider):
    def __init__(*args, **kwargs):
        pass
        # def __init__(self,start_date=None,end_date=None,code=None, *args, **kwargs):
    #     super(GupiaoSpider, self).__init__(*args, **kwargs)
    #     # self.code = code
    #     # self.start_date = start_date
    #     # self.end_date = end_date
    #     self.start_urls = ['http://quotes.money.163.com/service/chddata.html?code=1%s&start=%s&end=%s&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP' % (str(code),str(start_date),str(end_date))]

        # scrapy.Request(url, callback=self.parse)
    # gs = GupiaoSpider()
    name = 'gupiao2'
    # start_urls = ''
    # print(start_urls)
    # code = code
    # code = input("请输入股票代码")
    # start_date = input("起始日期：eg：20190412")
    # end_data = input("终止日期")
    #url = "http://quotes.money.163.com/1"+code+".html";

    code = '000725'
    start_date = '20180417'
    end_date = '20190417'
    start_urls = [
        'http://quotes.money.163.com/service/chddata.html?code=1%s&start=%s&end=%s&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP' % (
        str(code), str(start_date), str(end_date))]
    #start_urls = [url]
    # 处理响应函数
    def parse(self, response):
        # print(self.start_date)
        # print(self.end_date)
        print(self.start_urls)
        # print(response.body)
        item = GupiaospiderItem()
        href = response.url+"//000755.csv"
        item['file_urls'] = [href]
        # scrapy通过response.headers.getlist(
        item['file_name'] = response.headers.getlist('Content-Disposition')[0][21:32].decode('utf-8')


        # print(response.headers)
        # print(response.headers.getlist('Content-Disposition')[0][21:32].decode('utf-8'))
        # print(response.headers.getlist('Content-Disposition'))
        yield item
        # return file
        # print(response)
        # 获取response的body
        # print(response.body)
        # a_list = response.xpath("/html/body/div[2]/div[8]/ul/li[6]/a/@href")
        # stock_url = "http://quotes.money.163.com"+a_list.extract()[0];
        # print(stock_url)
        # pass


        # href_url = response.url
        # filename_location = r"D:\gupiao\full\11.csv"
        # output = open(filename_location, "wb")
        # print(response.content)
        # output.write(response.content)
        # output.close()
        # return None

        # yield scrapy.Request(href_url, callback=self.parse_data)

    # 对每个股票的数据
    def parse_data(self, response):
        filename_location = r"D:\gupiao\full\11.csv"
        output = open(filename_location, "wb")
        print(response.content)
        output.write(response.content)
        output.close()
        return None

