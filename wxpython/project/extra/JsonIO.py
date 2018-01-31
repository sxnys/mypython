# -*- coding: utf-8
__author__ = 'Sxn'
__date__ = '2017/5/23 20:04'

import json

JsonFile = open('talent_fund.json')
JsonDict = json.loads(JsonFile.read())

isConfirm = [False for _ in xrange(11)]   # 标记是否所有的模块录入都确定，一共10个

# print isConfirm

# print JsonDict

outputName = ''

# cover_dep_recommend = JsonDict['cover'][0]
# cover_expert_nomination = JsonDict['cover'][1]
cover = JsonDict['cover']
JsonDict['cover'] = {}

expert = JsonDict['expert']
JsonDict['expert'] = []

personal_info = JsonDict['basic_info']['personal_info']
dep_info = JsonDict['basic_info']['dep_info']

research_result = JsonDict['research_result']
work_and_significance = JsonDict['work_and_significance']

learning_exp = []
JsonDict['personal_profile']['learning_exp'] = []

working_exp = []
JsonDict['personal_profile']['working_exp'] = []

projects_info = []
JsonDict['personal_profile']['projects_info'] = []

repr_results_to_word = []
JsonDict['personal_profile']['repr_results_to_word'] = []

# repr_results = []
# JsonDict['personal_profile']['repr_results'] = []

awards = []
JsonDict['personal_profile']['awards'] = []

patent = []
JsonDict['personal_profile']['patent'] = []


def getNewJsonDict():
    return JsonDict

def getNewJson(JsonDict):
    return JsonDict