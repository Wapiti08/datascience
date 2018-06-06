import matplotlib.pyplot as mp

values=[26,17,21,29,11]
spaces=[0,0,0,0,0]
labels=['Python','JavaScript','C++','C','PHP']
colors=['dodgerblue','orangered','limegreen',
        'violet','gold']
mp.figure('Pie',facecolor='lightgray')
mp.title('Pie',fontsize=20)
mp.pie(values,spaces,labels,colors,'%d%%')
mp.show()