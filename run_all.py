# run_all.py
import os
import subprocess
import time
import sys

os.environ["PYTHONUTF8"] = "1"
os.environ["PYTHONIOENCODING"] = "utf-8"

# 配置参数组合
models = range(1, 10)  # 1-9号模型
time_solutions = ['15min', '30min', '45min', '60min']
test_number = 1

# 进度跟踪
current_task = 0
total_tasks = len(models) * len(time_solutions)


def show_progress():
    progress = current_task / total_tasks * 100
    bar_length = 30
    filled = '■' * int(bar_length * current_task / total_tasks)
    empty = '□' * (bar_length - len(filled))
    sys.stdout.write(f"\r进度: [{filled}{empty}] {progress:.1f}% ({current_task}/{total_tasks})")
    sys.stdout.flush()


def run_command(model, time_sol):
    global current_task

    cmd = [
        "python", "main.py",
        "--model_number", str(model),
        "--time_solution", time_sol,
        "--test_number", str(test_number)
    ]

    try:
        # 执行命令
        subprocess.run(
            cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT
        )
        status = "✓"
    except subprocess.CalledProcessError:
        status = "✗"

    current_task += 1
    show_progress()
    print(f"\n任务 route{model}-{time_sol}: {status}")


if __name__ == "__main__":
    print(f"开始执行 {total_tasks} 个任务...")
    for model in models:
        for time_sol in time_solutions:
            run_command(model, time_sol)
    print("\n全部任务完成！")