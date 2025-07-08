# 🚀 GRUforTrajLine

![GitHub last commit](https://img.shields.io/github/last-commit/Yingzhe-maker/GRUforTrajectories)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)



## 📌 目录
- [项目目标](#-项目目标)
- [数据集](#-数据集)
- [模型结构](#-模型结构)
- [算法创新](#-算法创新)
- [实验结果](#-实验结果)
- [使用指南](#-使用指南)
- [项目结构](#-项目结构)
- [贡献与支持](#-贡献与支持)
- [版权声明](#-版权声明)

## 🎯 项目目标
1. **高精度预测**：实现10-30步长的高精度位置预测（误差<1.5米）
2. **多场景支持**：


## 📊 数据集

### 训练数据集
- **数据来源**：[Geolife Trajectory Dataset](https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/)
- **关键统计**：

  
- **预处理流程**：
  1. 坐标系转换：WGS84 → UTM50N
  2. 数据清洗：
  
  3. 轨迹标准化：
  

### 数据格式
```csv
trajectory_id,timestamp,latitude,longitude,speed,heading
1,1612345678,39.906677,116.397755,12.3,135.2
1,1612345683,39.906732,116.398102,15.2,138.7
...

## 版权声明
MIT License

Copyright (c) 2023 Yingzhe-maker

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OT
