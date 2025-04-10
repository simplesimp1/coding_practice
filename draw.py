import matplotlib.pyplot as plt

# 任务编号 (task0-task10)
tasks = ['task' + str(i) for i in range(1,11)]

# 两条线的准确率数据
accuracy_line1 = [98.8,95.05,92.5,91.22,89.96,87.73,86.86,86.34,86.29,85.3]
accuracy_line2 = [98.8,95.15,92.5,91.22,89.80,88.87,88.67,87.01,87.02,86.31]

# 创建折线图
plt.figure(figsize=(8, 6))
plt.plot(tasks, accuracy_line1, marker='o', label='Dualprompt', color='blue', linestyle='-')
plt.plot(tasks, accuracy_line2, marker='s', label='CBDNet', color='green', linestyle='--')

# 图表标题和标签
plt.title('Accuracy Across Tasks', fontsize=14)
plt.xlabel('Tasks', fontsize=12)
plt.ylabel('Accuracy (%)', fontsize=12)
plt.ylim(85, 100)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.xticks(rotation=45)

# 显示图表
plt.tight_layout()
plt.show()
