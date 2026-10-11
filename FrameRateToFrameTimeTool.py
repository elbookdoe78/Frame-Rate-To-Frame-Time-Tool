import matplotlib.pyplot as plt 
import numpy as np

MaxFrames = int(input("What is the maximum frame rate you would want to see on the graph?\n"))

Frames = [] 
FrameTally = 0 
while len(Frames) != MaxFrames: 
    FrameTally += 1 
    Frames.append(FrameTally)

FrameTimes = []
for x in range(0,len(Frames)):
    FrameTime = 1 / Frames[x] * 1000
    FrameTimes.append(FrameTime)

xdata = np.array(Frames)
ydata = np.array(FrameTimes)

plt.figure().canvas.manager.set_window_title('Frame Rate To Frame Time')
plt.plot(xdata, ydata)
plt.grid()
plt.title("Frame Rate To Frame Time")
plt.xlabel("Frame Rate (Frames Per Second)")
plt.ylabel("Frame Time (Milliseconds)")
plt.show()