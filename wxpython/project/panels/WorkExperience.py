# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/22 19:09'

from . import StudyExperience
from extra import JsonIO

class TabPanel(StudyExperience.TabPanel):
    def __init__(self, parent):
        StudyExperience.TabPanel.__init__(self, parent, tabName=u'工作经历', instructText=u'含学术兼职情况', numLimit=10, editInfo=[u'起止年月', u'工作单位', u'职务/职称'], colSize=[250, 250, 250], childOrder=2)

    def addToJsonDict(self):
        JsonIO.working_exp = []
        for i in xrange(self.gridRow):
            tmp = {}
            tmp['start_end_date'] = self.infoGrid.GetCellValue(i, 0)
            tmp['working_dep'] = self.infoGrid.GetCellValue(i, 1)
            tmp['job'] = self.infoGrid.GetCellValue(i, 2)
            JsonIO.working_exp.append(tmp)