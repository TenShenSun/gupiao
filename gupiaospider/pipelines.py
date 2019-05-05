# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import Request
from scrapy.pipelines.files import FilesPipeline
import urllib.parse as urlparse
from os.path import basename,dirname,join

class GupiaospiderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        fileUrl = item['file_urls'][0]
        filePath = item['file_name']
        # return filePath
        # return filePath
        # yield scrapy.Request(url=fileUrl,path1=filePath)
        yield Request(url=fileUrl,meta={'path':filePath})

    def file_path(self, request, response=None, info=None):
        # name = request.meta['name']
        # seriesName = request.meta['seriesName']
        # fileName = request.url.split('/')[-1]
        # filePath = name + "/"+ seriesName +'/'+fileName
        #return 'full/%s' % "11.csv"
        return '/%s' % request.meta['path']
       # filePath = "000755/"+ response.mata['path']
       # return filePath