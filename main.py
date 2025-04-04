# main.py
import sys
import io
import os
import argparse
import torch
import pandas as pd
import numpy as np
from torch.utils.data import TensorDataset, DataLoader

# 本地导入
from configs.config import ModelConfig
from configs.paths import get_paths
from data.preprocessing import prepare_datasets
from models.gru import GRUModel
from trainers.gru_trainer import GRUTrainer
from evaluators.metrics import calculate_metrics
from utils.visualization import plot_trajectories

if sys.stdout.encoding != 'UTF-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def parse_args():
    parser = argparse.ArgumentParser(description="Trajectory Prediction Training")
    parser.add_argument("-model", "--model_number", type=str, required=True)
    parser.add_argument("-test", "--test_number", type=str, default="1")
    parser.add_argument("-time", "--time_solution", type=str, required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    paths = get_paths(args.model_number, args.time_solution, args.test_number)
    cfg = ModelConfig()

    # 准备数据
    train_df = pd.read_csv(paths["train_data"], usecols=['lon', 'lat'])
    test_df = pd.read_csv(paths["test_data"], usecols=['lon', 'lat'])

    (X_train, y_train), (X_val, y_val), (X_test, y_test), scaler = prepare_datasets(
        train_df, test_df, cfg.timestep, cfg.train_population
    )

    # 创建DataLoader
    train_loader = DataLoader(
        TensorDataset(torch.FloatTensor(X_train), torch.FloatTensor(y_train)),
        batch_size=cfg.batch_size, shuffle=True
    )
    val_loader = DataLoader(
        TensorDataset(torch.FloatTensor(X_val), torch.FloatTensor(y_val)),
        batch_size=cfg.batch_size
    )

    # 初始化模型
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GRUModel(
        input_size=cfg.featrue_size,
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        output_size=cfg.output_size
    )

    # 训练配置（修改检查逻辑）
    model_save_path = os.path.join(
        paths["outputs"]["models"],
        f"gru_{args.model_number}_test{args.test_number}_{args.time_solution}.pth"
    )

    if not os.path.exists(model_save_path):
        print("\n开始模型训练...")
        trainer = GRUTrainer(  # 初始化训练器
            model=model,
            train_loader=train_loader,
            val_loader=val_loader,
            optimizer=torch.optim.AdamW(model.parameters(), lr=cfg.learning_rate),
            criterion=torch.nn.MSELoss(),
            device=device,
            save_path=model_save_path
        )
        trainer.train(cfg.epochs)
    else:
        print(f"\n检测到预训练模型，跳过训练阶段")

    # 测试评估
    test_loader = DataLoader(
        TensorDataset(torch.FloatTensor(X_test), torch.FloatTensor(y_test)),
        batch_size=cfg.batch_size
    )

    try:
        model.load_state_dict(
            torch.load(model_save_path, map_location=torch.device(device))  # 设备兼容性处理
        )
        print(f"成功加载模型权重")
    except Exception as e:
        print(f"\n模型加载失败: {str(e)}")
        exit()

    model.eval()

    all_preds, all_trues = [], []
    with torch.no_grad():
        for inputs, targets in test_loader:
            inputs = inputs.to(device)
            preds = model(inputs).cpu().numpy()
            all_preds.append(preds)
            all_trues.append(targets.numpy())

    preds_denorm = scaler.inverse_transform(np.concatenate(all_preds))
    trues_denorm = scaler.inverse_transform(np.concatenate(all_trues))

    # 保存结果
    results_df = pd.DataFrame({
        'true_lon': trues_denorm[:, 0],
        'true_lat': trues_denorm[:, 1],
        'pred_lon': preds_denorm[:, 0],
        'pred_lat': preds_denorm[:, 1]
    })

    results_dir = paths["outputs"]["results"]
    os.makedirs(results_dir, exist_ok=True)
    results_path = os.path.join(results_dir,
                                f"result_route{args.model_number}_test{args.test_number}_{args.time_solution}.csv")
    results_df.to_csv(results_path, index=False)

    # 可视化保存
    plot_path = os.path.join(paths["outputs"]["plots"],
                             f"result_route{args.model_number}_test{args.test_number}_{args.time_solution}.png")
    plot_trajectories(trues_denorm, preds_denorm, plot_path)

    # 计算指标
    metrics = calculate_metrics(trues_denorm, preds_denorm)

    # 保存指标
    os.makedirs(paths["outputs"]["accuracy"], exist_ok=True)
    metrics_str = "\n".join([f"{k}: {v:.4f}" for k, v in metrics.items()])
    metrics_path = os.path.join(paths["outputs"]["accuracy"],
                                f"metrics_route{args.model_number}_test{args.test_number}_{args.time_solution}.txt")
    with open(metrics_path, 'w') as f:
        f.write(metrics_str)

    print(f"route{args.model_number}结果已保存！")


if __name__ == "__main__":
    main()