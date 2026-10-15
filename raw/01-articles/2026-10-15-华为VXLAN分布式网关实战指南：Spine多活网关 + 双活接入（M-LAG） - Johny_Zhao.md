---
title: "华为VXLAN分布式网关实战指南：Spine多活网关 + 双活接入（M-LAG） - Johny_Zhao"
source: "博客园"
url: "https://www.cnblogs.com/Johny-zhao/p/23318577"
date: "2026-10-15T09:45:00Z"
score: 0.85
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 华为VXLAN分布式网关实战指南：Spine多活网关 + 双活接入（M-LAG） - Johny_Zhao

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/Johny-zhao/p/23318577  
> **抓取日期**: 2026-10-15  
> **相关性评分**: 0.85

**一、方案架构与拓扑设计**

**1.1 架构总体思路**

分布式网关VXLAN架构的核心思想是将三层网关功能分散部署在多个Leaf节点上，避免集中式网关的单点瓶颈和次优转发路径问题。在Spine-Leaf组网中，Spine节点负责高速转发和路由反射，Leaf节点同时承担接入层和分布式网关功能，通过VXLAN隧道实现Overlay网络互通。

**Spine多活网关** 的实现关键在于：Spine节点以ECMP方式运行，上行路由设备到指定网段具有等价路由，多台Spine设备同时参与转发，不存在主备概念。当VXLAN网关部署在Leaf侧时，Spine节点不感知VXLAN隧道，仅作为VXLAN报文的转发节点，控制平面只需在Leaf之间建立VXLAN隧道。

**M-LAG双活接入** 将两台Leaf交换机在逻辑上虚拟成一台设备，下联的服务器或交换机通过LACP协议与两台设备进行链路聚合，完全感知不到后端实际是两台设备。M-LAG系统与分布式网关结合后，两台Leaf设备以相同的VTEP IP和网关IP对外呈现，实现真正的双活转发。

**1.2 典型拓扑**

text

┌─────────┐ ┌─────────┐

│ Spine1 │ │ Spine2 │

│ (RR) │ │ (RR) │

└────┬────┘ └────┬────┘

│ Underlay (OSPF/BGP) │

┌──────────┴──────────┬──────────┴──────────┐

│ │ │

┌────┴────┐ ┌────┴────┐ ┌────┴────┐

│ Leaf1 │ │ Leaf2 │ │ Leaf3 │

│ (M-LAG │==========│ (M-LAG │ │ │

│ Master)│ Peer-Link│ Backup) │ │ │

└────┬────┘ └────┬────┘ └────┬────┘

│ M-LAG Eth-Trunk │ │

└──────────┬───────────┘ │

┌────┴────┐ ┌────┴────┐

│ Server1 │ │ Server2 │

│(双归接入)│ │(单归/双归)│

└─────────┘ └─────────┘

Leaf1与Leaf2组成M-LAG系统，通过Peer-Link直连（建议采用独立物理链路，带宽不小于所有M-LAG成员口总带宽）。DAD双主检测链路使用独立的三层链路，不能与Peer-Link共用。

**1.3 设备命名与角色规划**

设备 |  角色 |  功能描述  
---|---|---  
Spine1 |  路由反射器/RR |  Underlay核心转发，BGP EVPN RR  
Spine2 |  路由反射器/RR |  与Spine1形成多活，ECMP负载分担  
Leaf1 |  分布式网关/M-LAG Master |  VTEP，分布式三层网关，M-LAG主设备  
Leaf2 |  分布式网关/M-LAG Backup |  VTEP，分布式三层网关，M-LAG备设备  
Leaf3 |  分布式网关 |  独立VTEP节点（非M-LAG组）  
  
**1.4 IP地址规划**

设备 |  接口 |  IP地址 |  用途  
---|---|---|---  
Spine1 |  GE1/0/1 |  192.168.1.1/24 |  连接Leaf1  
Spine1 |  GE1/0/2 |  192.168.2.1/24 |  连接Leaf2  
Spine1 |  Loopback1 |  1.1.1.1/32 |  Router ID / BGP源地址  
Spine2 |  GE1/0/1 |  192.168.5.1/24 |  连接Leaf1  
Spine2 |  GE1/0/2 |  192.168.6.1/24 |  连接Leaf2  
Spine2 |  Loopback1 |  1.1.1.2/32 |  Router ID / BGP源地址  
Leaf1 |  GE1/0/1 |  192.168.1.2/24 |  上行Spine1  
Leaf1 |  GE1/0/2 |  192.168.5.2/24 |  上行Spine2  
Leaf1 |  Loopback1 |  2.2.2.2/32 |  VTEP IP / BGP源地址  
Leaf1 |  Eth-Trunk1 |  — |  Peer-Link  
Leaf2 |  Loopback1 |  2.2.2.2/32 |  **与 Leaf1相同**（M-LAG虚拟VTEP）  
业务VBDIF |  Vbdif10 |  10.1.10.1/24 |  分布式网关IP（两台Leaf相同）  
  
**关键原则** ：M-LAG主备设备上对应M-LAG成员接口的VLANIF/VBDIF接口必须配置相同的IP地址和相同的虚拟MAC地址。所有Leaf的Loopback1地址在非M-LAG场景下必须全局唯一；在M-LAG场景下，同一M-LAG组的两台设备使用相同的VTEP IP地址。

**二、各设备配置范例**

**2.1 Underlay网络配置（OSPF）**

以Leaf1为例，配置Underlay三层互通：

text

system-view

sysname Leaf1

interface GE1/0/1

undo portswitch

ip address 192.168.1.2 24

ospf network-type p2p

quit

interface GE1/0/2

undo portswitch

ip address 192.168.5.2 24

ospf network-type p2p

quit

interface LoopBack1

ip address 2.2.2.2 32

quit

ospf 1

area 0

network 192.168.1.0 0.0.0.255

network 192.168.5.0 0.0.0.255

network 2.2.2.2 0.0.0.0

quit

commit

Spine1配置类似，注意Loopback1地址为1.1.1.1/32。验证Underlay连通性：display ospf peer查看邻居状态，ping -a 2.2.2.2 1.1.1.1验证Loopback互通。

**2.2 M-LAG配置（Leaf1 / Leaf2）**

**Leaf1（Master）关键配置：**

text

stp mode rstp

stp v-stp enable

dfs-group 1

priority 150

source ip 2.2.2.2 peer 3.3.3.3

dual-active detection source ip 6.6.6.6 peer 7.7.7.7

quit

interface Eth-Trunk1

trunkport GE1/0/3

trunkport GE1/0/4

mode lacp-static

peer-link 1

quit

interface Eth-Trunk2

trunkport GE1/0/5

mode lacp-static

m-lag 1

quit

commit

**Leaf2（Backup）** 对应配置中，DFS优先级设为120，source ip 3.3.3.3 peer 2.2.2.2，其他Peer-Link和M-LAG成员口配置与Leaf1完全一致。

**关键注意事项** ：

  * · Peer-Link必须使用独立Eth-Trunk接口，带宽要大于所有M-LAG成员口总带宽
  * · 必须启用V-STP以避免环路
  * · 建议Peer-Link成员口不少于2个物理接口，启用静态LACP模式
  * · 双主检测链路和Peer-Link链路不能共用物理路径



**2.3 BGP EVPN配置（Leaf1 / Leaf2）**

text

bgp 100

router-id 2.2.2.2

peer 1.1.1.1 as-number 100

peer 1.1.1.1 connect-interface LoopBack1

peer 1.1.1.2 as-number 100

peer 1.1.1.2 connect-interface LoopBack1

ipv4-family unicast

peer 1.1.1.1 enable

peer 1.1.1.2 enable

l2vpn-family evpn

peer 1.1.1.1 enable

peer 1.1.1.1 advertise irb

peer 1.1.1.2 enable

peer 1.1.1.2 advertise irb

quit

commit

Spine1作为RR配置：

text

bgp 100

router-id 1.1.1.1

peer 2.2.2.2 as-number 100

peer 2.2.2.2 connect-interface LoopBack1

peer 2.2.2.2 reflect-client

l2vpn-family evpn

peer 2.2.2.2 enable

peer 2.2.2.2 reflect-client

quit

commit

**2.4 VXLAN业务接入配置**

text

bridge-domain 10

vxlan vni 5010

quit

interface Nve1

source 2.2.2.2

vni 5010 head-end peer-list protocol bgp

quit

interface GE1/0/6.10 mode l2

encapsulation dot1q vid 10

bridge-domain 10

quit

interface Vbdif10

ip binding vpn-instance vpn1

ip address 10.1.10.1 24

mac-address 0000-5e00-0101

vxlan anycast-gateway enable

arp collect host enable

quit

**关键配置说明** ：vxlan anycast-gateway enable开启分布式网关功能后，网关收到网络侧的ARP或NS报文将做丢弃处理，只学习用户侧主机的ARP或NS报文。VBDIF接口的MAC地址在M-LAG两台设备上必须配置为相同的虚拟MAC。

**三、 M-LAG流量转发机制**

**3.1 M-LAG核心组件**

M-LAG系统由四个核心组件构成：

**DFS Group** 是M-LAG的“大脑”，负责两台设备间的配对、状态协商及表项同步。优先级高者当选Master，负责协调系统行为；Backup设备在正常情况下同样转发流量，没有性能差异。

**Peer-Link** 是M-LAG的“大动脉”，必须是二层Eth-Trunk接口，传输协商报文、同步MAC/IP表项，并在单归链路故障时转发流量。

**双主检测链路（ DAD）** 是M-LAG的“保命符”。当Peer-Link断开但心跳正常时，备设备自动Error-Down掉M-LAG成员口，防止双主冲突。

**M-LAG成员接口** 直接连接下联设备，被加入Eth-Trunk并绑定到特定的M-LAG ID。

**3.2 正常转发流程**

**同子网已知单播** ：Leaf1收到本地下联主机发往同子网远端主机的报文后，查找MAC表，若目的MAC在远端VTEP（Leaf3）上，则进行VXLAN封装后直接通过Underlay转发至Leaf3，不经过Spine节点。

**同子网 BUM报文**：通过EVPN Type 3路由建立头端复制列表，源VTEP将BUM报文复制为多个单播报文，分别封装后发送至各远端VTEP。

**跨子网报文转发** ：Leaf1收到主机报文后，发现目的IP不在本子网，查找L3VPN实例下的路由表（通过BGP EVPN IRB路由学习获得）。网关在本地完成三层转发，重新封装VXLAN后发送至目的VTEP。两台M-LAG设备使用相同的网关IP和MAC，服务器感知到的网关是唯一的。

**3.3 M-LAG故障切换流程**

**Peer-Link故障** ：DAD链路检测到Peer-Link断开但心跳正常，Backup设备将M-LAG成员口置为Error-Down状态，所有流量切换到Master设备转发。此时下联服务器通过LACP感知到一条链路故障，自动收敛到剩余链路。

**Master设备故障** ：Master设备下电或重启后，Backup设备通过DAD心跳超时感知，升为新的Master，接管所有M-LAG成员口，流量切换至新的Master转发。

**上行链路故障** ：建议配置Monitor Link关联上行接口和下行接口，当上行出接口Down时，下行接口状态变为Down，防止用户侧流量被丢弃。

**Peer-Link故障时Bypass VXLAN隧道** ：在物理Peer-Link场景下，若设备通过M-LAG双归接入VXLAN且接入侧链路故障，业务流量无法直接通过物理Peer-Link接口传输，此时可配置Bypass VXLAN隧道解决。

**四、网络调试详细步骤**

**4.1 Underlay调试**

**步骤 1：检查OSPF邻居状态**

text

display ospf peer brief

所有邻居状态应为Full。

**步骤 2：验证Loopback互通**

text

ping -a 2.2.2.2 1.1.1.1

ping -a 2.2.2.2 1.1.1.2

**4.2 M-LAG调试**

**步骤 1：检查DFS配对状态**

text

display dfs-group 1 m-lag

关注Heart beat state（应为OK）和State字段（Master/Backup）。Causation字段为“-”表示配对成功。

**步骤 2：检查Peer-Link状态**

text

display dfs-group 1 peer-link

display eth-trunk 1 verbose

Peer-Link接口应为Up，成员口状态正常。

**步骤 3：检查M-LAG成员口配对**

text

display dfs-group 1 m-lag brief

确认M-LAG成员口在主备设备上均已配对成功。

**步骤 4：检查双主检测状态**

text

display dfs-group 1 dual-active

**4.3 BGP EVPN调试**

**步骤 1：检查BGP EVPN对等体**

text

display bgp evpn peer

所有EVPN对等体状态应为Established。

**步骤 2：检查EVPN路由**

text

display bgp evpn all routing-table

应能看到Type 2（MAC/IP）、Type 3（IMET）和Type 5（IP前缀）路由。

**步骤 3：检查VXLAN隧道**

text

display vxlan tunnel

display vxlan vni

VNI状态应为Up，隧道信息应包含远端VTEP IP。

**4.4 常见故障排查**

现象 |  排查方向 |  关键命令  
---|---|---  
DFS配对失败 |  检查peer-link配置、心跳地址 |  display dfs-group 1 m-lag 查看Causation字段  
Peer-Link Down |  检查物理链路、Eth-Trunk状态 |  display eth-trunk 1 verbose  
EVPN邻居Down |  检查BGP配置、Underlay连通性 |  display bgp evpn peer  
VXLAN隧道Down |  检查NVE源地址、BGP路由 |  display vxlan tunnel  
跨子网不通 |  检查IRB路由、VBDIF网关 |  display bgp evpn all routing-table  
  
**五、注意事项**

**5.1 M-LAG配置注意事项**

**Peer-Link配置** ：必须在心跳状态正常时才能配置peer-link，防止一台M-LAG成员设备的接口错误进入error-down状态。如果M-LAG以根桥模式配置，需在接口上禁用STP（undo stp enable）。建议Peer-Link接口成员口采用10GE或更大带宽物理口，成员口数不少于2个，启用静态LACP模式，直连不能加透传设备。

**M-LAG成员口一致性** ：DeviceA与DeviceB上的M-LAG接口配置必须完全一致，包括VLAN划分、LACP模式等，否则会导致协商异常。

**广播域隔离** ：如果属于不同进程的M-LAG成员端口同属于一个广播域，在peer-link接口被阻塞时可能造成环路，需要划分不同进程的M-LAG成员端口到不同广播域。

**配置顺序** ：建议先配置物理peer-link接口以及Bypass VXLAN隧道，待peer-link接口Up之后再配置双主检测source-ip和peer-ip地址。

**5.2 分布式网关注意事项**

**License要求** ：通过BGP EVPN方式部署的分布式网关为VXLAN增强功能，使用License控制，需要申请并购买相应License。

**配置一致性** ：请确保两台双归接入设备上关于VXLAN业务接入点和VXLAN隧道的配置保持一致。

**ARP抑制** ：BGP EVPN方式支持主机IP路由通告、ARP通告，可直接使能ARP广播抑制功能。在三层网关上开启分布式网关功能后，网关收到网络侧的ARP或NS报文将做丢弃处理，只学习用户侧主机的ARP或NS报文。

**主机路由发布** ：根据Overlay网络类型选择发布IRB路由（arp collect host enable）或IP前缀路由（arp direct-route enable）。

**上行口 STP处理**：VLANIF的上行口需配置stp disable，并将物理Peer-Link端口退出上行口所在VLAN，上行口配置为三层主接口。

**六、验证与测试**

**6.1 基础连通性测试**

**测试 1：Underlay连通性**

  * · 在各设备上执行 ping -a Loopback IP 对端Loopback IP，验证Underlay三层可达。
  * · 执行 display ospf peer 确认所有OSPF邻居为Full。



**测试 2：VXLAN隧道建立验证**

  * · 执行 display vxlan tunnel 确认隧道状态为Up。
  * · 执行 display vxlan vni 确认VNI状态为Up，隧道列表包含正确的远端VTEP IP。



**测试 3：EVPN路由学习验证**

  * · 执行 display bgp evpn all routing-table 检查Type 2和Type 5路由是否正确学习。
  * · 执行 display bgp evpn peer 确认所有EVPN邻居状态为Established。



**6.2 M-LAG状态验证**

text

display dfs-group 1 m-lag # DFS配对状态

display dfs-group 1 peer-link # Peer-Link状态

display eth-trunk 2 verbose # M-LAG成员口状态

display m-lag consistency-check # 配置一致性检查

**6.3 业务测试场景**

**场景一：同子网二层互通**

Server1（10.1.10.100/24）与Server2（10.1.10.200/24）处于同一子网。Server1 ping Server2，预期正常通信。在Leaf1上执行 display mac-address bridge-domain 10 确认远端MAC地址通过VXLAN隧道学习到。抓包确认报文经过VXLAN封装，在Underlay中传输。

**场景二：跨子网三层互通**

Server1（10.1.10.100/24）与Server3（10.1.20.100/24）处于不同子网。Server1 ping Server3，预期正常通信。在Leaf1上执行 display ip routing-table vpn-instance vpn1 确认到10.1.20.0/24的路由通过BGP EVPN学习到。验证分布式网关功能：两台M-LAG设备使用相同的网关IP和MAC，ARP应答一致。

**场景三： M-LAG链路故障切换**

在Server1持续ping Server2的同时，手动shutdown Leaf1（Master）的M-LAG成员口。预期Server1通过LACP感知链路故障，自动切换到Leaf2（Backup）的链路，ping丢包在预期范围内（LACP收敛时间）。验证：display dfs-group 1 m-lag 显示Leaf2仍为Backup状态，M-LAG成员口状态正常。

**场景四： Peer-Link故障测试**

模拟Peer-Link断开（在Eth-Trunk1接口执行shutdown），验证DAD机制是否生效：Backup设备（Leaf2）的M-LAG成员口应进入Error-Down状态。执行 display error-down recovery 查看接口状态。恢复Peer-Link后，接口自动恢复。

**场景五： Master设备整机故障**

直接将Leaf1（Master）下电。预期Leaf2通过DAD心跳超时感知，升为新的Master，接管所有流量。Server1到Server2的业务应在DAD检测超时后恢复。记录切换时间和丢包数，评估业务影响。

**场景六： Spine多活验证**

Leaf1上执行 display ip routing-table 确认到Spine1和Spine2的Loopback路由均为等价路由（ECMP）。断开Leaf1到Spine1的链路，验证流量自动切换到Spine2，Underlay转发不受影响。

**6.4 VXLAN Ping/Tracert验证**

华为设备支持VXLAN Ping和Tracert功能，可用于端到端VXLAN网络测试。在发起端使能VXLAN Ping功能后，可对VXLAN隧道进行连通性检测。执行VXLAN Ping时指定源VTEP IP和目的VTEP IP，验证VXLAN隧道的端到端可达性。

**6.5 大数据包测试**

在业务测试场景中，建议在服务器上使用大数据包（10000字节以上）进行ping测试，同时在沿途路径设备上配置ACL计数，通过报文数确定丢包点和故障设备

官方参考文档

  * · ‌IPv4分布式网关+M-LAG示例‌：[配置分布式网关部署方式的IPv4 VXLAN示例](<https://support.huawei.com/enterprise/zh/doc/EDOC1000037064/ec8427c3>)
  * · ‌双活网关配置详解‌：[(可选)配置双活网关](<https://support.huawei.com/enterprise/zh/doc/EDOC1100352676/f1dad88a>)‌‌



[https://support.huawei.com/enterprise/zh/doc/EDOC1000037064/ec8427c3](<https://support.huawei.com/enterprise/zh/doc/EDOC1000037064/ec8427c3>)

[https://support.huawei.com/enterprise/zh/doc/EDOC1100352676/f1dad88a](<https://support.huawei.com/enterprise/zh/doc/EDOC1100352676/f1dad88a>)


---
> 原文链接: https://www.cnblogs.com/Johny-zhao/p/23318577