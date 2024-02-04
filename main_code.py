import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 用户输入参数
num_people = 400  # 人数
speed_mean = 0  # 移动速度均值
speed_std = 1  # 移动速度标准差
canvas_size = (800, 800)  # 画布大小
collision_distance = 5  # 碰撞距离阈值

# 初始化人群位置和速度
positions = np.random.rand(num_people, 2) * canvas_size
speeds = np.random.randn(num_people, 2) * speed_std + speed_mean

# 初始化谣言传播状态，初始时只有一个人知道谣言
rumor_status = np.zeros(num_people, dtype=bool)
rumor_spreader = np.random.randint(num_people)
rumor_status[rumor_spreader] = True

# 创建画布
fig, ax = plt.subplots()
ax.set_xlim(0, canvas_size[0])
ax.set_ylim(0, canvas_size[1])
scat = ax.scatter(positions[:, 0], positions[:, 1], c=['red' if x else 'blue' for x in rumor_status])

# 更新函数，用于动画
def update(frame_number):
    global positions, speeds, rumor_status

    # 更新点的位置
    positions += speeds
    # 处理边界碰撞，让点反弹
    for i in range(num_people):
        if positions[i, 0] > canvas_size[0] or positions[i, 0] < 0:
            speeds[i, 0] = -speeds[i, 0]
        if positions[i, 1] > canvas_size[1] or positions[i, 1] < 0:
            speeds[i, 1] = -speeds[i, 1]

    # 处理谣言传播
    for i in range(num_people):
        if rumor_status[i]:  # 如果这个人知道谣言
            for j in range(num_people):
                if not rumor_status[j] and np.linalg.norm(positions[i] - positions[j]) < collision_distance:
                    rumor_status[j] = True  # 传播谣言

    # 更新散点图对象的位置和颜色
    scat.set_offsets(positions)
    scat.set_color(['red' if status else 'blue' for status in rumor_status])

    # 检查是否所有人都知道谣言，如果是，则结束动画
    if all(rumor_status):
        #plt.close(fig)
        ani.event_source.stop()
        return

    return scat,

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=2000, interval=50, blit=True)

# 保存动画
ani.save(r'C:\Users\10031558\Documents\hu_excel\rumor_spread_simulation_03.mp4', writer='ffmpeg', fps=20)

# 显示动画
plt.show()
