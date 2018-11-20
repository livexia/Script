# Script
一些自己编写的脚本


dhcp.py: 将lede/openwrt的dhcp 设置转化为 merlin的ethers、host.dnsmq、dhcp_staticlist，利用nvram set dhcp_staticlist="$(cat dhcp_staticlist.txt)"和nvram commit在merlin上应用dhcp设置
