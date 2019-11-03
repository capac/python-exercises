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
c.set_linewidth(2)
plt.tick_params(axis='both', which='both', bottom=False, top=False, labelbottom=False, right=False, left=False, labelleft=False)
plt.setp(ax.spines.values(), linewidth=2)

# fontsize=8
# for tick in ax.xaxis.get_major_ticks():
#     tick.label1.set_fontsize(fontsize)
#     tick.label1.set_fontweight('bold')
# for tick in ax.yaxis.get_major_ticks():
#     tick.label1.set_fontsize(fontsize)
#     tick.label1.set_fontweight('bold')
plt.grid(linewidth=2, alpha=0.4, color='k')
plt.show()
# plt.savefig('polar-plot.png', dpi=144, format='png')
