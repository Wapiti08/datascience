import matplotlib.gridspec as mg
import matplotlib.pyplot as mp

mp.figure('Grid',facecolor='lightgray')
#第一张图
gs=mg.GridSpec(3,3)
mp.subplot(gs[0,:2])
mp.xticks(())
mp.yticks(())
#其中的1表示第一张图
mp.text(0.5,0.5,'1',ha='center',va='center',size=36,alpha=0.5)

#第二张图
mp.subplot(gs[:2,2])
mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,'2',ha='center',va='center',size=36,alpha=0.5)

#第三张图
mp.subplot(gs[2,1:])
mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,'3',ha='center',va='center',size=36,alpha=0.5)

#第四张图
mp.subplot(gs[1:,0])
mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,'4',ha='center',va='center',size=36,alpha=0.5)

#第五张图
mp.subplot(gs[1,1])
mp.xticks(())
mp.yticks(())
mp.text(0.5,0.5,'5',ha='center',va='center',size=36,alpha=0.5)
mp.show()