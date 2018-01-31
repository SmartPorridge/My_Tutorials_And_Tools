# @Author  : SmartPorridge

*****************Sports-1M数据集说明*****************
1.data文件夹下存放需要下载的三个csv文件
2.视频总大小预计在1TB以上
3.使用Windows系统进行下载，直接运行即可

*****************WINDOWS下载说明*********************
1.使用方法：
	为了下载方便，train、test、val数据分开下载，因此需要执行三次程序。
    在download_win.py当前目录内执行，参数分别为：CSV文件 视频存放路径 -n:同时下载的线程数，-t:缓存存放路径;下面为命令示例：
	
		python download_win.py D:\\download_kinetics\\data\\kinetics_test_modefied.csv D:\\download_kinetics\\video\\test -n=25 -t=D:\\download_kinetics\\tmp\\kinetics
		python download_win.py D:\\download_kinetics\\data\\kinetics_val.csv D:\\download_kinetics\\video\\val -n=25 -t=D:\\download_kinetics\\tmp\\kinetics
		python download_win.py D:\\download_kinetics\\data\\kinetics_train.csv D:\\download_kinetics\\video\\train -n=25 -t=D:\\download_kinetics\\tmp\\kinetics
		
	即可进行下载
	注意：必须使用绝对路径
2.说明
	视频缓存将缓存在tmp/kinetics文件夹下，程序会自动删除，最终需要的视频会存放于video文件夹下的三个文件夹内。
