I.MX6ULL 
###########


IMX6ull boot
=================


在uboot 来到main_loop 后， 


.. code-block:: c
   :linenos:

	s = bootdelay_process();
	if (cli_process_fdt(&s))
		cli_secure_boot_cmd(s);

	autoboot_command(s);


在 bootdelay_process 中， 完成了 启动的 延时，以及 自启动命令。
bootdelay_process 返回时， s 存入了 bootcmd   对应的 环境变量的
值。 然后 autoboot_command 去执行。


在 imx6ull 这个平台 ，

.. code-block:: c
   :linenos:

    "bootcmd="	CONFIG_BOOTCOMMAND		"\0"
    #define CONFIG_BOOTCOMMAND \
	   "run findfdt;" \
	   "mmc dev ${mmcdev};" \
	   "mmc dev ${mmcdev}; if mmc rescan; then " \
		   "if run loadbootscript; then " \
			   "run bootscript; " \
		   "else " \
			   "if run loadimage; then " \
				   "run mmcboot; " \
			   "else run netboot; " \
			   "fi; " \
		   "fi; " \
	   "else run netboot; fi"






Enhanced Configurable SPI(ECSPI)
=====================================

imx6ull 的 ECSPI 是 全双工， 同步， 四线的 SPI 接口。 有 64*32
bit 的 接收缓冲（RXFIFO）,和 64*32 的发送缓冲。这样可以可以提高通讯
效率。

下面是框图：

