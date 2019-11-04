import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
# np.random.seed(19680801)
np.random.seed(196)

# Compute areas and colors
N = 80
r = 2 * np.random.rand(N)
theta = 2 * np.pi * np.random.rand(N)
area = 600 * r**2
colors = theta

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
c = ax.scatter(theta, r, c=colors, s=area, cmap='hsv', alpha=0.6, edgecolor='k')
lw, bw = 2, 1
c.set_linewidth(bw)
# plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
plt.setp(ax.spines.values(), linewidth=lw)
# plt.subplots_adjust(left=0.05, right=0.95, top=0.98, bottom=0.05)
fontsize=8
for tick in ax.xaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
for tick in ax.yaxis.get_major_ticks():
    tick.label1.set_fontsize(fontsize)
    tick.label1.set_fontweight('bold')
plt.grid(linewidth=lw, alpha=0.4, color='k')
plt.show()
# plt.savefig('polar-plot.png', dpi=144, format='png')
