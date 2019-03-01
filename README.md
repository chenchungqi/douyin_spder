# douyin_spder
1.安装最新的fidder,下载fidder的证书到手机
2.设置手机的代理IP设置为电脑的IP，现在fidder获取了手机的数据包
![Fidder](https://github.com/chenchungqi/douyin_spder/blob/master/jietu/183450w7r36616y8yzu9ts.png)
3.用json解析这个抖音的数据包
![json](https://github.com/chenchungqi/douyin_spder/blob/master/jietu/183449n3l4oltmszsvx7ko.png)
4.修改fiddlerscript，利用这个修改的函数，把它保存到本地某个文件夹
![fiddlerscript](https://github.com/chenchungqi/douyin_spder/blob/master/jietu/183451ynhmi4igzps1wndz.png)
5.fidder函数的保存到本地的数据只能覆盖，不能添加，所以用python写个循环脚本读取写入数据库
![python_script](https://github.com/chenchungqi/douyin_spder/blob/master/jietu/183452iyft6z2hy9ckczfj.png)
6.最后一步写一个模拟人工划抖音的脚本了
![free](https://github.com/chenchungqi/douyin_spder/blob/master/jietu/183703zouuequesxu2uare.png)
