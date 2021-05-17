# CCPD2YOLO
Process CCPD picture filenames, translate car plate into readable Chinese, draw bounding boxes and make corresponding txt for YOLO.

CCPD paper: [Towards End-to-End License Plate Detection and Recognition: A Large Dataset and Baseline](https://openaccess.thecvf.com/content_ECCV_2018/papers/Zhenbo_Xu_Towards_End-to-End_License_ECCV_2018_paper.pdf)

To download CCPD dataset...
* 2019 and 2020 Blue Plate and Renewable Energy Green Plate: https://github.com/detectRecog/CCPD
* 2021 Yellow Plate: https://github.com/xiaosongshine/CCPD_Plus

### Prerequisite:
```bash
pip install opencv-python
```
Just run `bbox.py` or `ccpd2yolotxt.py`. Don't forget to replace the default CCPD directory with yours.



### Format:
* **CCPD filename format:**
  > 面积比-斜度-左上右下坐标-四个角坐标（右下角开始顺时针）-车牌-亮度-模糊度

* **YOLO txt format:**
  > 0 中心点（归一化宽） 中心点（归一化长） 框宽度（归一化） 框长度（归一化）

### Issue:
* It is not easy for opencv to draw Chinese characters on a picture. You could replace Chinese characters with pinyin if needed.
