import pandas as pd
#import warnings
#warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
from pandas.tools.plotting import parallel_coordinates
from pandas.tools.plotting import radviz


sns.set(style="white", color_codes=True)

iris = pd.read_csv("wine.csv")
#iris.head()
#print iris
#print iris["Wine"].value_counts()
#sns.jointplot(x="A1", y="A2", data=iris, kind='reg', size=6)

#sns.pairplot(iris, hue="Wine",size=1)

parallel_coordinates(iris, "Wine")
radviz(iris, "Wine")
sns.plt.show()
