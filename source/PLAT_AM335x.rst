AM335x
#########




bring up
================


boot SD 卡 制作
-------------------


在整个SDK 目录中 ， bin  文件夹下 提供了 create-sdcard.sh





系统启动
=============


在这里记录一些 系统的 启动特性。 参考 SPRUH73P。 

这些过程在 ROM code 之后，分为两种启动类型：

* Memory Booting : 系统从 主要的 memory 中 开始执行code , 比如说，flash ,memory card ,一般
都是这个情况。

* Peripheral Booting： 系统通过外设启动， 比如串口 和 usb 下载。 这个一般并不常用。 

设备类型
--------

high-secure (HS) device and a general-purpose (GP) deviece. HS 设备不会允许没有经过签名
认证的可执行镜像执行。 GP 设备 是 禁用secure 的，所以不需要镜像 进行签名认证。 
