# 🚀 GRUforTrajectories

![GitHub last commit](https://img.shields.io/github/last-commit/Yingzhe-maker/GRUforTrajectories)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange)

This project uses Gated Recurrent Unit (GRU) neural network to model and predict trajectory, which can be applied in fields such as traffic flow prediction and user behavior analysis.

## 📌 Catalogs
- [项目目标](#-项目目标)
- [数据集](#-数据集)
- [模型结构](#-模型结构)
- [实验结果](#-实验结果)
- [使用指南](#-使用指南)
- [项目结构](#-项目结构)
- [贡献与支持](#-贡献与支持)

## 🎯 项目目标
构建端到端的轨迹预测系统，通过历史轨迹数据预测未来位置序列。主要目标：
- 实现10-30步长的高精度位置预测
- 支持多种移动对象（车辆/行人/无人机）
- 适应复杂城市道路网络拓扑
- 预测误差 < 1.5米（短距离场景）

## 📊 数据集

### train datasets
- **Source**：[Geolife Trajectories](https://www.microsoft.com/en-us/research/publication/geolife-gps-trajectory-dataset-user-guide/) (替换为你的实际链接)
- **统计特征**：
  - 17,621条轨迹（总里程约1.2百万公里）
  - 采样频率：1-5秒/点
  - 覆盖范围：北京及周边区域
- **预处理**：
  - 坐标转换（WGS84 -> UTM）
  - 异常点滤波（速度>200km/h）
  - 轨迹分段（固定长度128点）

### 数据格式
```csv
trajectory_id,timestamp,latitude,longitude,speed
1,1612345678,39.906677,116.397755,12.3
1,1612345683,39.906732,116.398102,15.2
...
