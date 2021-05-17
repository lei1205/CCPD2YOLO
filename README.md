# CCPD2YOLO
Process CCPD picture filenames, translate car plate into readable Chinese, draw bounding boxes and make corresponding txt for YOLO.

### Format
* **CCPD filename format:**

> 面积比-斜度-左上右下坐标-四个角坐标（右下角开始顺时针）-车牌-亮度-模糊度

* **YOLO txt format:**

> 0 中心点（归一化宽） 中心点（归一化长） 框宽度（归一化） 框长度（归一化）

