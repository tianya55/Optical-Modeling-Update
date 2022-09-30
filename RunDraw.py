import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pickle

############################
# 绘制合并的图，共用一个色柱
# 2022-9-22
# pickle模块记录runModeling过程数据：ax2，ax5（包括XYZ，self）
# 此程序直接运行，输出两幅合并的图
############################


filelist = [
    "Result\20220930 171924\",
    "Result\20220930 171924\",
]#两个文件的目录
front_size = 14

plt.clf()
fig, ax = plt.subplots(1, 2,figsize=(14,5))
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.4,hspace=0.15)# 调整间隔

data = []

for i in range(len(filelist)):
    with open(filelist[i]+"_Fig_EfieldE2",'rb') as f:
        X,Y,Z = pickle.load(f)
    ax[i].set_ylabel('Wavelength (nm)', size=front_size)
    ax[i].set_xlabel('Position (nm)', size=front_size)
    ax[i].set_xlim(min(X[0]), max(X[0]))
    ax[i].set_ylim(Y[0][0], Y[-1][0])
    im = ax[i].contourf(X, Y, Z, 50, cmap=None)
    for c in im.collections:  # avoid white gaps when converting to pdf
        c.set_edgecolor("face")
    ax[i].tick_params(labelsize=front_size)
# fig.colorbar(im, ax=[ax[i] for i in range(len(filelist))])
fig.colorbar(im, ax=ax.ravel().tolist())

for i in range(len(filelist)):
    with open(filelist[i]+"_EfieldE2self",'rb') as f:
        self = pickle.load(f)
for i in range(len(filelist)):
    for matind in range(2, len(self.layers) + 1):

        ax[i].axvline(self.t_cumsum[matind - 1], color="black")
        x_text = (self.t_cumsum[matind - 2] +
                  self.t_cumsum[matind - 1]) / 2.0
        ax[i].text(x_text, ax[i].get_ylim()[1] + 0.01, self.layers[matind - 1],
                 size=front_size, va="bottom", ha="center")
        ax[i].set_title(filelist[i],y=1.07)

plt.show()#第一幅电场图

plt.clf()
fig, ax = plt.subplots(1, 2,figsize=(14,5))
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0.4,hspace=0.15)
for i in range(len(filelist)):
    with open(filelist[i]+"G",'rb') as f:
        X,Y,Z = pickle.load(f)

    ax[i].set_ylabel('Wavelength (nm)', size=front_size)
    ax[i].set_xlabel('Position (nm)', size=front_size)
    ax[i].set_xlim(min(X[0]), max(X[0]))
    ax[i].set_ylim(Y[0][0], Y[-1][0])
    im = ax[i].contourf(X, Y, Z, 50, cmap=None)
    for c in im.collections:  # avoid white gaps when converting to pdf
        c.set_edgecolor("face")
    ax[i].tick_params(labelsize=front_size)
# fig.colorbar(im, ax=[ax[i] for i in range(len(filelist))])
fig.colorbar(im, ax=ax.ravel().tolist())

for i in range(len(filelist)):
    with open(filelist[i]+"_FigGself",'rb') as f:
        self = pickle.load(f)
for i in range(len(filelist)):
    for matind in range(2, len(self.layers) + 1):

        ax[i].axvline(self.t_cumsum[matind - 1], color="black")
        x_text = (self.t_cumsum[matind - 2] +
                  self.t_cumsum[matind - 1]) / 2.0
        ax[i].text(x_text, ax[i].get_ylim()[1] + 0.01, self.layers[matind - 1],
                 size=front_size, va="bottom", ha="center")
        ax[i].set_title(filelist[i],y=1.07)
plt.show()

