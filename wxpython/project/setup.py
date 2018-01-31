#-*-coding: UTF-8-*-
from distutils.core import setup
import py2exe
# Powered by ***
INCLUDES = []
options = {"py2exe" :  
    {"compressed" : 1,  
     "optimize" : 2,  
     "bundle_files" : 2,  
     "includes" : INCLUDES,  
     "dll_excludes": [ "MSVCP90.dll", "mswsock.dll", "powrprof.dll", "w9xpopen.exe"] }}  
setup(
    options = options, 
    description = u"国防科技卓越青年人才基金项目申报系统",  
    zipfile=None,
    console=[{"script": "mainApp.py", "icon_resources": [(1, "logo.ico")] }],
    data_files=[('image', [
    		'about.png', 'bglogo.jpg', 'edit.png', 'export.png', 'help.png', 
    		'homeBackground.jpg', 'word.png'
    	])
    ]
)