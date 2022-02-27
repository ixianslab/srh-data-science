#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
# Load the "autoreload" extension
get_ipython().run_line_magic('load_ext', 'autoreload')
# always reload modules
get_ipython().run_line_magic('autoreload', '2')
# black formatter for jupyter notebooks
#%load_ext nb_black
# black formatter for jupyter lab
get_ipython().run_line_magic('load_ext', 'lab_black')

get_ipython().run_line_magic('run', '../src/notebook_env.py')


# # Die Grundgesamtheitsverteilung

# **Importiere Module**

# In[2]:


import numpy as np


# Die **Grundgesamtheitsverteilung** ist die Wahrscheinlichkeitsverteilung, die sich aus der Kenntnis aller Elemente einer Grundgesamtheit ergibt {cite:p}`mann2007introductory`. Wir wissen, dass die interessierende Zufallsvariable je nach der betrachteten Grundgesamtheit eine diskrete Variable sein kann, d. h. eine Variable, die zumindest im Prinzip abzählbar ist (abzählbar unendlich), oder die Zufallsvariable kann eine kontinuierliche Variable sein, d. h. eine Variable, die jeden Wert innerhalb eines bestimmten Intervalls annehmen kann (überabzählbar unendlich). Sowohl die diskrete als auch die kontinuierliche Wahrscheinlichkeitsverteilung kann durch statistische Parameter wie den Mittelwert, die Standardabweichung, den Median, den Modalwert und andere beschrieben werden. Diese Parameter, die die Grundgesamtheit beschreiben, sind jedoch **immer konstant**, da die Grundgesamtheit die Menge aller Elemente ist und sich somit die Grundgesamtheitsstatistik nicht ändert. So gibt es beispielsweise für jeden Populationsdatensatz **nur einen Wert** für den Populationsmittelwert, **einen Wert** für die Standardabweichung usw.

# ## Grundgesamtheitsstatistiken und Stichprobenstatistiken
# 
# Betrachten wir ein einfaches Beispiel für eine kleine diskrete Grundgesamtheit, die aus den ersten zehn ganzen Zahlen $\{1,2,3,4,5,6,7,8,9,10\}$ besteht.

# In[3]:


population = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mean = np.mean(population)
std = np.std(population)

print(f"Mittelwert (Grundgesamtheit):         {mean}")
print(f"Standartabweichung (Grundgesamtheit): {std}")


# Der Populationsmittelwert $μ$, und die Populationsstandardabweichung $σ$ beträgt $5,5$ bzw. etwa $3,028$. Es ist wichtig zu erkennen, dass sich diese Parameter, die Populationsparameter, nicht ändern! Sie sind durch die Grundgesamtheit festgelegt.
# 
# Nehmen wir nun eine Zufallsstichprobe ohne Ersetzung mit dem Umfang $n=3$ aus dieser Grundgesamtheit. 

# In[4]:


my_sample = np.random.choice(population, size=3, replace=False)
my_sample


# Nun berechnen wir den Mittelwert und die Standardabweichung der gegebenen Stichprobe. Da wir uns aber auf eine bestimmte Stichprobe beziehen, nennen wir den statistischen Parameter diesmal **Stichprobenstatistik** oder, wenn wir uns auf die Verteilung der Werte (Elemente) beziehen, **Stichprobenverteilung**. Um dies zu verdeutlichen, wird der Stichprobenmittelwert mit $\bar{x}$ und die Stichprobenstandardabweichung mit $s$ bezeichnet.

# In[5]:


x_bar = np.mean(my_sample)
s = np.std(my_sample, ddof=1)

print(f"Mittelwert (Stichprobe):         {x_bar}")
print(f"Standartabweichung (Stichprobe): {s}")


# Bitte beachten Sie, dass sich die Stichprobenstatistiken je nach den tatsächlichen Elementen in der Stichprobe von Stichprobe zu Stichprobe ändern.

# ## Der Stichprobenfehler
# 
# Wir wiederholen die Stichprobe aus dem vorigen Abschnitt fünfmal und geben den Mittelwert $\bar{x}$ für jede einzelne Stichprobe aus.

# In[6]:


for i in range(5):
    my_sample = np.random.choice(population, size=3, replace=False)
    mean = np.mean(my_sample)
    print(f"Die {i}. Stichprobe hat einen Mittelwert von {mean}")


# Es liegt auf der Hand, dass verschiedene Stichproben (mit derselben Länge), die aus derselben Grundgesamtheit ausgewählt wurden, unterschiedliche Stichprobenstatistiken ergeben, da sie unterschiedliche Elemente enthalten. Darüber hinaus unterscheidet sich jede aus einer Stichprobe gewonnene Stichprobenstatistik, z. B. der Stichprobenmittelwert $\bar{x}$, von dem Ergebnis, das aus der entsprechenden Grundgesamtheit, dem Grundgesamtheitsmittelwert $μ$, gewonnen wird. Die Differenz zwischen dem Wert einer aus einer Stichprobe gewonnenen Statistik und dem Wert des entsprechenden, aus der Grundgesamtheit gewonnenen Parameters wird als **<a href="https://en.wikipedia.org/wiki/Sampling_error">Stichprobenfehler</a>** bezeichnet. Im Fall des Mittelwerts kann der Stichprobenfehler wie folgt geschrieben werden
# 
# $$ \text{Sampling error} = \bar{x} - \mu$$
# 
# Aufgrund des Charakters von Zufallsstichproben und willkürlichen Ziehung einer Reihe von Werten aus der Grundgesamtheit ist der daraus resultierende Stichprobenfehler zufällig, oder anders gesagt, der Stichprobenfehler ist eine Zufallsvariable. Es ist jedoch zu beachten, dass es neben der beschriebenen Zufälligkeit noch andere Fehlerquellen gibt. Diese Fehler hängen oft mit dem Prozess der Datenerzeugung zusammen und werden unter dem Begriff <a href="https://en.wikipedia.org/wiki/Non-sampling_error">Nicht-Stichprobenfehler</a> zusammengefasst. Solche Fehler werden beispielsweise durch die menschliche Handhabung der Daten, Kalibrierungsfehler der Messgeräte etc. verursacht.
# 
# Um ein Gefühl für die Art des Stichprobenfehlers zu bekommen, führen wir ein Experiment durch. Bei diesem Experiment besteht die interessierende Grundgesamtheit aus den ersten $100$ ganzen Zahlen $\{1,2,3,...,100\}$. Wir wollen den Einfluss des Stichprobenumfangs $n$ auf den Stichprobenfehler untersuchen. Der Einfachheit halber wählen wir den Stichprobenmittelwert als die interessierende Statistik. Für eine ausreichend große Anzahl von Versuchen (z.B. 5000 Versuche) berechnen wir den Stichprobenfehler für Stichproben mit dem Umfang $n=10,25,50,75$.

# In[7]:


TRIAL_SIZE = 5000  # 5000 Versuche
SAMPLE_SIZE = [10, 25, 50, 75]  # Stichprobenumfang
population = range(1, 101)
mean_pop = np.mean(population)
for n in SAMPLE_SIZE:
    error_sample = []
    for _ in range(TRIAL_SIZE):
        my_sample = np.random.choice(population, size=n, replace=False)
        mean = np.mean(my_sample)
        error_sample.append(abs(mean - mean_pop))
    print(f"Stichprobenfehler (n={n}):", np.mean(error_sample))


# Aus dem obigen Experiment können wir schließen, dass der Stichprobenfehler umso kleiner ist, je größer der Stichprobenumfang ist. Mit anderen Worten: Je größer der Stichprobenumfang ist, desto mehr nähert sich der Stichprobenmittelwert $\bar{x}$ dem Grundgesamtheitsmittelwert $μ$ an. Dies ist eine wichtige Erkenntnis, die im Abschnitt über die *Inferenzstatistik* ausführlicher behandelt werden wird.

# In[8]:


import matplotlib.pyplot as plt


def dot_diagram(dataset, ax=None, min_max=(30, 70)):
    """
    Function to compute a dotplot.
    Inspried by https://stackoverflow.com/a/66398730
    """
    values, counts = np.unique(dataset, return_counts=True)
    data_range = max(values) - min(values)
    # fig_width = data_range / 2 if data_range < 30 else 15
    fig_width = 16
    fig_height = max(counts) / 3 if data_range < 50 else max(counts) / 4
    marker_size = 5
    if ax is None:
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    for value, count in zip(values, counts):
        ax.plot(
            [value] * count,
            list(range(count)),
            marker="o",
            color="tab:blue",
            markersize=marker_size,
            linestyle="",
        )
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.yaxis.set_visible(False)
    # ax.set_ylim(-1, max(counts))
    ax.set_ylim(-1, 18)
    ax.set_xticks(range(min_max[0], min_max[1] + 1, 5))
    ax.set_xlim(min_max[0] - 1, min_max[1] + 1)
    ax.tick_params(axis="x", length=0, pad=10)


# population = list(range(1, 101))
# mean_pop = np.mean(population)

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(16, 9))
_axes = np.ravel(axes)
trials = [1, 10, 100, 500, 1000, 3000]
SAMPLE_SIZE = 30
np.random.seed(42)
for e, trial in enumerate(trials):
    sample_statistic = []
    for n in range(trial):
        sample = np.random.choice(population, size=SAMPLE_SIZE)
        mean_sample = np.mean(sample)
        sample_statistic.append(mean_sample)
    dot_diagram(sample_statistic, ax=_axes[e])
    _axes[e].text(x=60, y=15, s=f"{trials[e]} Stichproben", size=13)
    _axes[e].text(x=mean_pop, y=16, s=f"$\mu$", size=14, ha="center")
    _axes[e].vlines(x=mean_pop, ymin=-1, ymax=15, color="k", linestyle="dashed")


# Je häufiger wir eine Stichprobe nehmen, desto besser nähert sich die relative Häufigkeitsverteilung der Stichprobenstatistik der Stichprobenverteilung an. Mit anderen Worten: Wenn die Anzahl der Stichproben gegen unendlich geht, nähert sich die resultierende Häufigkeitsverteilung der Stichprobenverteilung an. **Die Stichprobenverteilung einer Statistik** ist eine Wahrscheinlichkeitsverteilung dieser Statistik, die aus allen möglichen Stichproben mit demselben Umfang aus der Grundgesamtheit abgeleitet wird. Die Stichprobenverteilung sollte jedoch nicht mit einer Stichprobenverteilung verwechselt werden: Letztere beschreibt die Verteilung der Werte (Elemente) in einer bestimmten Stichprobe.
