from objects.instance import Instance
from objects.job import Job
import plotly.figure_factory as ff
import plotly.graph_objs as go
from datetime import datetime
import random

instance: Instance
j: Job

def plot_gantt(instance, by="JOB", grouping=True):
    # Affiche le diagram de Gantt
    # Input : Objet de type Instance

    # df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
    #      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
    #     dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

    # Création d'une liste de dictionnaire
    # Parcours les jobs de l'instance

	if len(instance.jobs_list) > 8:
		colors = []
		for i in range(1, len(instance.jobs_list) + 1):
			r = lambda: random.randint(0,255)
			current_colors = '#%02X%02X%02X' % (r(),r(),r())
			colors.append(current_colors)

	df = []
	for j in instance.jobs_list:
		# Parcours les tâches de jobs
		for t in j.list_task:
			# On associe chaque
			if by == "JOB":
				df.append(dict(Task="Job  #" + str(t.jobID),
                               Start=datetime.fromordinal(t.startDate + 1),
                               Finish=datetime.fromordinal(t.finishDate + 1),
                               Resource="Machine #" + str(t.machineID)))
			elif by == "MACHINE":
				df.append(dict(Task="Machine  #" + str(t.machineID),
                               Start=datetime.fromordinal(t.startDate + 1),
                               Finish=datetime.fromordinal(t.finishDate + 1),
                               Resource="Job #" + str(t.jobID)))
				
	if len(instance.jobs_list) > 8:
		fig = ff.create_gantt(df, index_col='Resource',
                          reverse_colors=False,
                          show_colorbar=True,
                          group_tasks=grouping,
                          show_hover_fill=True,
                          showgrid_x=True,
                          showgrid_y=True,
						  colors=colors)
	else:
		fig = ff.create_gantt(df, index_col='Resource',
                          reverse_colors=False,
                          show_colorbar=True,
                          group_tasks=grouping,
                          show_hover_fill=True,
                          showgrid_x=True,
                          showgrid_y=True)
		
	fig.layout.xaxis.tickformat = '%'
	go.FigureWidget(fig)
	fig.show()