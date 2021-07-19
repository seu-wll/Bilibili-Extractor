import sys
sys.path.append("..")
import extractor.pipeline
import os
import database.msql

sql_res = database.msql.query("banime","select distinct bvid in Vinfo")
for i in sql_res:
    bvid = i[0]
    filename = "/home/wzc/mtmp/%s.mp4"%bvid
    extractor.pipeline.importMedia(bvid, filename)
    extractor.pipeline.downloadInfo(bvid)
    extractor.pipeline.shotCut(bvid)
    extractor.pipeline.extract(bvid, 0, 0)
    extractor.pipeline.extract(bvid, 0, 1)
    extractor.pipeline.extract(bvid, 0, 2)
    extractor.pipeline.extract(bvid, 0, 3)