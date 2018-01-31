# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/22 19:20'

from . import StudyExperience
from extra import JsonIO

class TabPanel(StudyExperience.TabPanel):
    def __init__(self, parent):
        StudyExperience.TabPanel.__init__(self, parent, tabName=u'承担国防相关代表性项目情况', instructText=u'限5项', numLimit=5, editInfo=[u'起止年月', u'名称', u'项目类别', u'来源', u'经费', u'本人承担任务', u'本人排序'], colSize=[250, 250, 200, 200, 100, 250, 100], childOrder=3)

    def addToJsonDict(self):
        JsonIO.projects_info = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['id'] = str(i + 1)
            tmp['start_end_date'] = self.infoGrid.GetCellValue(i, 0)
            tmp['project_name'] = self.infoGrid.GetCellValue(i, 1)
            tmp['project_type'] = self.infoGrid.GetCellValue(i, 2)
            tmp['source'] = self.infoGrid.GetCellValue(i, 3)
            tmp['fund'] = self.infoGrid.GetCellValue(i, 4)
            tmp['mission'] = self.infoGrid.GetCellValue(i, 5)
            tmp['sort'] = self.infoGrid.GetCellValue(i, 6)

            JsonIO.projects_info.append(tmp)