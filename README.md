# 🚀 GRUforTrajectories - 轨迹预测系统

![GitHub last commit](https://img.shields.io/github/last-commit/Yingzhe-maker/GRUforTrajectories)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange)
![License](https://img.shields.io/badge/License-MIT-green)

基于门控循环单元(GRU)的端到端轨迹预测系统，适用于交通流量预测、用户行为分析和无人机航迹规划等场景。项目利用深度学习技术实现高精度、低时延的未来位置预测。

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
   - 城市车辆轨迹预测
   - 行人移动路径分析
   - 无人机航线规划
3. **复杂环境适应**：
   - 城市道路网络拓扑建模
   - 交通信号灯时序影响分析
   - 交叉口通行模式识别
4. **实时性能**：
   - 单条轨迹推理时延<20ms
   - 支持每秒1000+条轨迹的批量预测

## 📊 数据集

### 训练数据集
- **数据来源**：[Geolife Trajectory Dataset](https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/)
- **关键统计**：
  | 指标 | 值 |
  |------|----|
  | 轨迹总数 | 17,621 |
  | 总里程 | ≈1.2百万公里 |
  | 时间跨度 | 2007-2012 |
  | 采样频率 | 1-5秒/点 |
  | 地理范围 | 北京及周边(500km²) |
  
- **预处理流程**：
  1. 坐标系转换：WGS84 → UTM50N
  2. 数据清洗：
     - 移除速度异常点(>200km/h)
     - 补全缺失采样点(三次样条插值)
     - 消除GPS漂移(Kalman滤波)
  3. 轨迹标准化：
     - 固定长度分段(128点)
     - 归一化处理(Min-Max Scaling)
     - 80/20训练验证集划分

### 数据格式
```csv
trajectory_id,timestamp,latitude,longitude,speed,heading
1,1612345678,39.906677,116.397755,12.3,135.2
1,1612345683,39.906732,116.398102,15.2,138.7
...
