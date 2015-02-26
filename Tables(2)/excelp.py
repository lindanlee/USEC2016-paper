import csv
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
from xlrd import open_workbook
from numpy import median
def parser(x):
	x = open_workbook("data.xlsm")
	sheet = x.sheet_by_index(3)
	rtn = dict()
	benefit_dic = dict()
	risk_dic = dict()
	final_dic = dict()
	stat = dict()
	temp = dict()
	for j in range(312,323):
		lst = []

		if sheet.cell_value(0,j) == "ben" or sheet.cell_value(0,j) == "risk":


			for i in range(1,1785):
				cat = sheet.cell_value(i,j)
				arg = sheet.cell_value(i,j)
				if arg != '':
					if type(arg) != float:
						print('error', i,j,arg)
						return
				if arg > 100:
					arg = 100
				if sheet.cell_value(0,j) == "ben":
					ben_arg = str(sheet.cell_value(i,3)).replace(" ", "")
					if ben_arg+ "ben" in benefit_dic:
						benefit_dic[ben_arg+ "ben"].append(arg)
					else:
						benefit_dic[ben_arg + "ben"] = [arg]


				if str(sheet.cell_value(i,3)  +sheet.cell_value(0,j)) in rtn:
					rtn[str(sheet.cell_value(i,3))  + sheet.cell_value(0,j)].append(arg)
				else:
					rtn[str(sheet.cell_value(i,3))  +sheet.cell_value(0,j)] = [arg]


		else:
			for i in range(1,1785):
				arg = sheet.cell_value(i,j)
				if arg != '':
					if type(arg) != float:
						print('error', i,j,arg)
						return
					if arg > 100:
						arg = 100
					lst.append(int(arg))
			if len(lst)!= 0:
				check = sheet.cell_value(0,j)
				if "Electricity" in check:
					if "risk" in check:
						check = "Electricity Risk"
					else:
						check = "Electricity Benefit"
				elif "Motorcycle" in check:
					if "risk" in check:
						print("here it is")
						check = "Motorcycle Risk"
					else:
						check = "Motorcycle Benefit"
				elif "Handgun" in check:
					if "risk" in check:
						check = "Handgun Risk"
					else:
						check = "Handgun Benefit"
				elif "Lawnmower" in check:
					if "risk" in check:
						check = "Lawnmower Risk"
					else:
						check = "Lawnmower Benefit"
				rtn[check] = lst
	f = open("benefit.tex","w")
	g = open("risk.tex","w")
	h = open("riskbenefit.tex","w")
	h.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{2cm} | p{1cm} | p{1cm} | p{1cm} | c | p{2cm} | p{1cm} | p{1cm} | p{1cm} | c |}\n&\\multicolumn{4}{ |c| }{Risk} & \\multicolumn{4}{ c| }{Benefit}\\\\ \n \\\\hline\nTechnology &  Median & Q1 & Q3 & Distribution &  Median& Q1 & Q3 & Distribution   \\\\ \n\\hline\n")

	g.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{2cm} | p{1cm} | p{1cm} | p{1cm} | c |}\n\\hline\nTechnology & Q1 &  Median & Q3 & Distribution  \\\\ \n\\hline\n")

	f.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{2cm} | p{1cm} | p{1cm} | p{1cm} | c |}\n\\hline\nTechnology & Q1 &  Median & Q3 & Distribution  \\\\ \n\\hline\n")
	for i in benefit_dic.keys():
		lst = sorted(benefit_dic[i])
		if len(lst)!=0:
			index = len(lst)/2
			stat[i] = [median(lst),median(lst[:index]),median(lst[index+1:])]

	for i in rtn.keys():
		lst = sorted(rtn[i])
		if len(lst)!=0:
			index = len(lst)/2
			stat[i] = [median(lst),median(lst[:index]),median(lst[index+1:])]

		arg = reader([i,rtn[i]])

		arg = list(arg)
		for j in range(len(arg)):
			if arg[j] == ":":
				arg[j] = "/"
		arg = ''.join(arg)

		quart = stat[i]
		if "risk" in arg:
			var = str(i).replace("risk","").replace(" ","")
			var_2 = var + "ben"
			ben_var = reader([var_2, benefit_dic[var_2]])
			ben_var = list(ben_var)
			for j in range(len(ben_var)):
				if ben_var[j] == ":":
					ben_var[j] = "/"
			ben_var = ''.join(ben_var)
			quart2 = stat[ben_var]
			final_string = str(i).replace("risk","") + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" +arg+ "} & "+str(quart2[0]) + " & " + str(quart2[1]) + " & " + str(quart2[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + ben_var + "} \\\\ \n"

			if quart[0] in final_dic:
				final_dic[quart[0]].append(final_string)
			else:
				final_dic[quart[0]] = [final_string]
		#h.write(str(i).replace("risk","") + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" +arg+ "} & "+str(quart2[0]) + " & " + str(quart2[1]) + " & " + str(quart2[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + ben_var + "} \\\\ \n")

			g.write(str(i).replace("risk","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n")
		elif "Risk" in arg:
			final_string = str(i).replace(" Risk","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n"

			if quart[0] in final_dic:
				final_dic[quart[0]].append(final_string)
			else:
				final_dic[quart[0]] = [final_string]
			g.write(str(i).replace(" Risk","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n")
		elif "Benefit" in arg:
			final_string = str(i).replace(" Benefit","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n"
			if quart[0] in final_dic:
				final_dic[quart[0]].append(final_string)
			else:
				final_dic[quart[0]] = [final_string]
			f.write(str(i).replace(" Benefit","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n")
		else:
			f.write(str(i).replace(" ben","").title() + " & "+str(quart[0]) + " & " + str(quart[1]) + " & " + str(quart[2]) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../" + arg + "} \\\\ \n")


		# f.write(i + " ")
		# f.write(str(rtn[i])[1:len(str(rtn[i]))-1] + "\n")
	finlst = sorted(list(final_dic.keys()))
	for i in finlst:
		for j in final_dic[i]:
			h.write(j)


	f.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	g.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	h.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	
	f.close()
	g.close()
	h.close()

def reader(x):
	prev = x[0]
	numbers = x[1]

	title = str(x[0])
	title = title.replace(" ", "")
	plt.axis('off')
	nbins = [i for i in range(0,26)]
	for i in numbers:
		i = i/4
	plt.hist(edgecolor = "none",x = numbers,color = 'green',alpha = 0.5, align = 'mid',bins = nbins, rwidth = 1, normed = True)
	plt.axis([0,25,0,1])
	# plt.tick_params(\
#   axis='x',          # changes apply to the x-axis
#   which='both',      # both major and minor ticks are affected
#   bottom='off',      # ticks along the bottom edge are off
#   top='off',         # ticks along the top edge are off
#   labelbottom='off') # labels along the bottom edge are off
	#plt.xticks(np.arange(1,6))

	savefig(title, dpi=None, facecolor='w', edgecolor='w',
	orientation='portrait', papertype=None, format=None,
	transparent=False, bbox_inches='tight', pad_inches=0,
	frameon=None)
	plt.clf()
	return title

# def median(lst):
#     lst = sorted(lst)
#     import math
#     if len(lst) < 1:
#             return None
#     if len(lst) %2 == 1:
#             return float(lst[((len(lst)+1)/2)-1])
#     if len(lst) %2 == 0:
#             return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0

parser("data.xlsm")
