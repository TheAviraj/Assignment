import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")

tips = sns.load_dataset("tips")
sns.relplot(x="total_bill", y="tip", data=tips);

sns.relplot(x="total_bill", y="tip", hue="smoker", data=tips);

sns.relplot(x="total_bill", y="tip", hue="smoker", style="smoker",
            data=tips);

sns.relplot(x="total_bill", y="tip", hue="smoker", style="time", data=tips);

sns.relplot(x="total_bill", y="tip", hue="size", data=tips);

sns.relplot(x="total_bill", y="tip", hue="size", palette="ch:r=-.5,l=.75", data=tips);

sns.relplot(x="total_bill", y="tip", size="size", data=tips);

sns.relplot(x="total_bill", y="tip", size="size", sizes=(15, 200), data=tips);

df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)
g.fig.autofmt_xdate()

df = pd.DataFrame(np.random.randn(500, 2).cumsum(axis=0), columns=["x", "y"])
sns.relplot(x="x", y="y", sort=False, kind="line", data=df);

fmri = sns.load_dataset("fmri")
sns.relplot(x="timepoint", y="signal", kind="line", data=fmri);

sns.relplot(x="timepoint", y="signal", ci=None, kind="line", data=fmri);

sns.relplot(x="timepoint", y="signal", kind="line", ci="sd", data=fmri);

sns.relplot(x="timepoint", y="signal", estimator=None, kind="line", data=fmri);
