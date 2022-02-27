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


# # Der Standardfehler
# 
# Ebenso wie die Verteilungen der Grundgesamtheit können auch die Stichprobenverteilungen mit Parametern beschrieben werden. Der Erwartungswert (Mittelwert) einer beliebigen Verteilung kann durch das Symbol $\mu$ dargestellt werden. Im Falle der Stichprobenverteilung wird der Mittelwert $\mu$ oft mit einem tiefgestellten Index geschrieben, um anzugeben, welche Stichprobenverteilung beschrieben wird. Der Erwartungswert der Stichprobenverteilung des Mittelwerts wird zum Beispiel durch das Symbol $\mu_{\bar{x}}$ dargestellt. Der Wert von $\mu_{\bar{x}}$ kann als der theoretische Mittelwert der Verteilung der Stichprobenmittelwerte angesehen werden.
# 
# Wenn wir aus einer Grundgesamtheit eine ausreichend große Anzahl von Stichproben (mit gleichem Umfang) auswählen und deren Mittelwerte berechnen, dann nähert sich der Mittelwert ($\mu_{\bar{x}}$) all dieser Stichprobenmittelwerte dem Mittelwert ($\mu$) der Grundgesamtheit an. Deshalb wird der Stichprobenmittelwert $\bar{x}$ als Schätzer des Populationsmittelwertes $\mu$ bezeichnet. Somit ist der Mittelwert der Stichprobenverteilung gleich dem Mittelwert der Grundgesamtheit.
# 
# $$\mu_{\bar{x}} = \mu$$
# 
# Für die Standardabweichung einer Stichprobenverteilung gibt es eine besondere Bezeichnung, den **<a href="https://en.wikipedia.org/wiki/Standard_error">Standardfehler</a>**. Der Standardfehler der Stichprobenverteilung einer Statistik, bezeichnet als $\sigma_{\bar{x}}$, beschreibt das Ausmaß, in dem die berechneten Statistiken erwartungsgemäß voneinander abweichen, wenn sie anhand einer Stichprobe ähnlichen Umfangs berechnet und aus ähnlichen Grundgesamtheitsmodellen ausgewählt werden. Je größer der Standardfehler einer bestimmten Statistik ist, desto größer sind die Unterschiede zwischen den berechneten Statistiken für die verschiedenen Stichproben *(Lovric 2010)*.
# 
# Es ist jedoch zu beachten, dass der Standardfehler $\sigma_{\bar{x}}$ nicht gleich der Standardabweichung $\sigma$ der Verteilung der Grundgesamtheit ist (es sei denn, $n=1$). Der Standardfehler ist gleich der Standardabweichung der Grundgesamtheit geteilt durch die Quadratwurzel des Stichprobenumfangs :
# 
# $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}}$$
# 
# Diese Gleichung gilt nur, wenn die Stichprobe entweder mit Ersatz aus einer endlichen Grundgesamtheit oder mit oder ohne Ersatz aus einer unendlichen Grundgesamtheit gezogen wird. Dies entspricht der Bedingung, dass der Stichprobenumfang $(n)$ im Vergleich zum Grundgesamtheitsumfang $(N)$ klein ist. Der Stichprobenumfang gilt als klein im Vergleich zum Umfang der Grundgesamtheit, wenn der Stichprobenumfang gleich oder weniger als 5 % des Umfangs der Grundgesamtheit ist, d. h., wenn
# 
# $$\frac{n}{N} \leq 0.05$$
# 
# Wenn diese Bedingung nicht erfüllt ist, wird die folgende Gleichung zur Berechnung von $\sigma_{\bar{x}}$ verwendet :
# 
# $$\sigma_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \sqrt{\frac{N-n}{N-1}}$$
# 
# In den meisten praktischen Anwendungen ist der Stichprobenumfang jedoch klein im Vergleich zur Grundgesamtheit.
