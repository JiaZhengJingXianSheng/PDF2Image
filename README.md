# PDF2Image
# PDF转图片



完整源码：https://github.com/JiaZhengJingXianSheng/PDF2Image

#### x86-64 可执行文件：

https://github.com/JiaZhengJingXianSheng/PDF2Image/releases



执行源码须自己配置依赖，需配置traits，请自行搜索解决。打包后的可执行程序链接如上。

### 注意：

程序因未作错误判定，请选择PDF文件夹时，保证文件夹下仅有pdf文件。

## 程序核心

```python
for file in os.listdir(self.path):
	pdf = fitz.open(self.path + "/" + file)

	# 逐页读取PDF
	for pg in range(0, pdf.page_count):
		page = pdf[pg]
		pm = page.get_pixmap()
		# 开始写图像
		pm.save(self.path + "/../Image/" + str(file) + "/" + str(pg) + ".png")
	
	pdf.close()
```

程序会在pdf文件夹同目录下生成Image文件夹，对应图片会放在以对应pdf名称为文件名的目录下。



## 执行效果

![1.PNG](https://s2.loli.net/2021/12/25/1URoFBX2d7Cb6ZK.png)

1. 点击选择路径，选择PDF所在文件夹，当下方提示PDF路径即为成功。

![2.PNG](https://s2.loli.net/2021/12/25/auhvk6TJrjBlINY.png)

2. 点击开始执行，下方会显示执行进度，在执行结束后会出现成功的弹窗。

![3.PNG](https://s2.loli.net/2021/12/25/k4WYLpeaRGQrwTz.png)

![4.PNG](https://s2.loli.net/2021/12/25/nFvVCeWobpqml49.png)

3. 接下来就可以去Image中找图片文件了，生活愉快😄
