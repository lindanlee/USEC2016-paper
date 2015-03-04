
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

def parse(text):

	f = open(text,'r')
	# friends = open("friends.tex",'w')
	# work = open("work.tex",'w')
	# pub = open("pub.tex",'w')
	# app = open("app.tex",'w')
	collapsed = open("collapsed.tex",'w')
	collapsed_std = open("collapsedstd.tex",'w')
	VUR_combined = open("VURcombined.tex",'w')
	recipient = open("recipient.tex",'w')
	x = """\\documentclass[a4paper,12pt]{article}
\\usepackage[cm]{fullpage}
\\usepackage{longtable}
\\usepackage{graphicx}
\\begin{document}
\\begin{longtable}{| p{0.5cm} | p{7cm} | p{1cm} | c |}

\\hline \\multicolumn{1}{|c|}{\\textbf{Rank}} & \\multicolumn{1}{c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{VUR}} &  \\multicolumn{1}{c|}{\\textbf{Distribution}} \\\\ \\hline 
\\endfirsthead

\\multicolumn{3}{c}%
{{\\bfseries \\tablename\ \\thetable{} -- continued from previous page}} \\\\
\\hline \\multicolumn{1}{|c|}{\\textbf{Rank}} & \\multicolumn{1}{c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{VUR}} &  \\multicolumn{1}{c|}{\\textbf{Distribution}} \\\\ \\hline 
\\endhead

\\hline \\multicolumn{4}{|r|}{{Continued on next page}} \\\\ \\hline
\\endfoot
\\hline 
\\endlastfoot\n"""
	recipient.write("""\\begin{table}[t]
\\begin{center}
\\small
\\begin{tabular}{| r | p{1.5cm} | p{1cm} | p{1cm} | p{2cm} |}
\\hline
Rank & Recipient & VUR & Standard Deviation & Distribution\\\\
\\hline\n""")
	# friends.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{0.5cm} | p{7cm} | p{1cm} | c |}\n\\hline\n Rank & Q &  VUR & Distribution  \\\\ \n\\hline\n")
	# work.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{0.5cm} | p{7cm} | p{1cm} | c |}\n\\hline\n Rank & Q &  VUR & Distribution  \\\\ \n\\hline\n")
	# pub.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{0.5cm} | p{7cm} | p{1cm} | c |}\n\\hline\n Rank & Q &  VUR & Distribution  \\\\ \n\\hline\n")
	# app.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{0.5cm} | p{7cm} | p{1cm} | c |}\n\\hline\n Rank & Q &  VUR & Distribution  \\\\ \n\\hline\n")
	# collapsed.write("\\begin{table}[t]\n\\begin{center}\n\\small\n\\begin{tabular}{| p{0.5cm} | p{7cm} | p{1cm} | c |}\n\\hline\n Rank & Q &  VUR & Distribution  \\\\ \n\\hline\n")
	# friends.write(x)
	# work.write(x)
	# pub.write(x)
	# app.write(x)
	collapsed.write(x)
	collapsed_std.write("""\\documentclass[a4paper,12pt]{article}
\\usepackage[cm]{fullpage}
\\usepackage{longtable}
\\usepackage{graphicx}
\\begin{document}
\\begin{longtable}{| p{0.5cm} | p{7cm} | p{1cm} |p{1cm} | c |}

\\hline \\multicolumn{1}{|c|}{\\textbf{Rank}} & \\multicolumn{1}{c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{VUR}} &  \\multicolumn{1}{c|}{\\textbf{Standard Deviation}} &\\multicolumn{1}{c|}{\\textbf{Distribution}} \\\\ \\hline 
\\endfirsthead

\\multicolumn{3}{c}%
{{\\bfseries \\tablename\ \\thetable{} -- continued from previous page}} \\\\
\\hline \\multicolumn{1}{|c|}{\\textbf{Rank}} & \\multicolumn{1}{c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{VUR}} & \\multicolumn{1}{c|}{\\textbf{Standard Deviation}} & \\multicolumn{1}{c|}{\\textbf{Distribution}} \\\\ \\hline 
\\endhead

\\hline \\multicolumn{4}{|r|}{{Continued on next page}} \\\\ \\hline
\\endfoot
\\hline 
\\endlastfoot\n""")
	VUR_combined.write("""\\documentclass[a4paper,12pt]{article}
\\usepackage[cm]{fullpage}
\\usepackage{longtable}
\\usepackage{graphicx}
\\begin{document}
\\begin{longtable}{| p{7cm} | l | l | l | l | l |}

\\hline \\multicolumn{1}{|c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{All}} & \\multicolumn{1}{c|}{\\textbf{Friends}} &  \\multicolumn{1}{c|}{\\textbf{Public}} & \\multicolumn{1}{c|}{\\textbf{Work}} & \\multicolumn{1}{c|}{\\textbf{Appserver}} \\\\ \\hline 
\\endfirsthead

\\multicolumn{6}{c}%
{{\\bfseries \\tablename\ \\thetable{} -- continued from previous page}} \\\\
\\hline \\multicolumn{1}{|c|}{\\textbf{Question}} & \\multicolumn{1}{c|}{\\textbf{All}} & \\multicolumn{1}{c|}{\\textbf{Friends}} &  \\multicolumn{1}{c|}{\\textbf{Public}} & \\multicolumn{1}{c|}{\\textbf{Work}} & \\multicolumn{1}{c|}{\\textbf{Appserver}} \\\\ \\hline 
\\endhead

\\hline \\multicolumn{6}{|r|}{{Continued on next page}} \\\\ \\hline
\\endfoot
\\hline 
\\endlastfoot\n""")

	line = f.readline()
	prev = None
	combined = []
	collapsed_dict = dict()
	std_dict = dict()
	friends_dict = dict()
	work_dict = dict()
	pub_dict = dict()
	app_dict = dict()
	VUR_friends = []
	VUR_work = []
	VUR_pub = []
	VUR_app = []
	VUR_collapsed = []

	new_friends = dict()
	new_work = dict()
	new_pub = dict()
	new_app = dict()
	new_collapsed = dict()
	recipient_friends = []
	recipient_work = []
	recipient_pub = []
	recipient_app = []
	recipient_total = []
	recipient_dic = dict()


	while line:
		x = line.split()
		if prev != None and prev != x[0]:
			plt.hist(edgecolor = "none",x = combined,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
		# plt.tick_params(\
  #   axis='x',          # changes apply to the x-axis
  #   which='both',      # both major and minor ticks are affected
  #   bottom='off',      # ticks along the bottom edge are off
  #   top='off',         # ticks along the top edge are off
  #   labelbottom='off') # labels along the bottom edge are off
		#plt.xticks(np.arange(1,6))
			# plt.xticks([])
			# plt.yticks([])
			plt.axis([1,6,0,1])
			ax = plt.gca()
			ax.set_autoscale_on(False)
			plt.axis('off')

			savefig(str(prev) + "combined", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
			VUR = combined.count(5)
			VUR = round(float(VUR)/len(combined),4) * 100
			std = np.std(combined)
			std = round(std,4)
			combined = []
			plt.clf()
			if VUR in collapsed_dict:
				new_collapsed[VUR].append(str(prev))
			else:
				new_collapsed[VUR] = [str(prev)]
				collapsed_dict[VUR] =[" & "  + str(prev).title()+ " & " + str(VUR) + " & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + str(prev) + "combined} \\\\ \n"]
			if std in std_dict:
				std_dict[std].append(" & "  + str(prev).title()+ " & " + str(VUR) + " & " + str(std) + "& \\includegraphics[width = 2cm, height = 0.5cm]{../tables" + str(prev) + "combined} \\\\ \n")
			else:
				std_dict[std] = [" & "  + str(prev).title()+ " & " + str(VUR) + " & "+ str(std) + "&\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + str(prev) + "combined} \\\\ \n"]

			VUR_collapsed.append(VUR)

		prev = x[0]

		numbers = list(x[2])

		title = str(x[0]) + str(x[1])
		for i in range(len(numbers)):
			numbers[i] = int(numbers[i])
			combined.append(numbers[i])
		count = numbers.count(5)
		count = round(float(count)/len(numbers),4) * 100
		plt.hist(edgecolor = "none",x = numbers,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
		plt.axis([1,6,0,1])
		ax = plt.gca()
		ax.set_autoscale_on(False)

		if str(x[1]) == "FRIENDS":
			if count in friends_dict:
				friends_dict[count].append(" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n")

			else:
				
				friends_dict[count] = [" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n"]
			for i in numbers:
				recipient_friends.append(i)
				recipient_total.append(i)
			new_friends[str(prev)] = count
			VUR_friends.append(count)

		elif str(x[1]) == "WORKCONTACTS":
			if count in work_dict:
				work_dict[count].append(" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n")
			else:

				work_dict[count] = [" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n"]
			for i in numbers:
				recipient_work.append(i)
				recipient_total.append(i)

			new_work[str(prev)] = count
			VUR_work.append(count)

		elif str(x[1]) == "PUBLIC":
			if count in pub_dict:
				pub_dict[count].append(" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n")
			else:
				pub_dict[count] = [" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\  \n"]
			for i in numbers:
				recipient_pub.append(i)
				recipient_total.append(i)

			new_pub[str(prev)] = count
			VUR_pub.append(count)

		elif str(x[1]) == "APPSERVER":
			if count in app_dict:
				app_dict[count].append(" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\ \n")
			else:
				app_dict[count] = [" & "  + str(prev).title()+ " & " + str(count) + "\% & " + "\\includegraphics[width = 2cm, height = 0.5cm]{../tables" + title + "} \\\\ \n"]
			for i in numbers:
				recipient_app.append(i)
				recipient_total.append(i)

			new_app[str(prev)]=count
			
			VUR_app.append(count)

		# plt.tick_params(\
  #   axis='x',          # changes apply to the x-axis
  #   which='both',      # both major and minor ticks are affected
  #   bottom='off',      # ticks along the bottom edge are off
  #   top='off',         # ticks along the top edge are off
  #   labelbottom='off') # labels along the bottom edge are off
		#plt.xticks(np.arange(1,6))
		# plt.xticks([])
		# plt.yticks([])
		plt.axis('off')


		savefig("tables/" + title, dpi=None, facecolor='w', edgecolor='w',
		orientation='portrait', papertype=None, format=None,
		transparent=False, bbox_inches='tight', pad_inches=0,
		frameon=None)
		line = f.readline()
		plt.clf()
	count = 1
	VUR_app = sorted(VUR_app, reverse = True)
	VUR_friends = sorted(VUR_friends, reverse = True)
	VUR_collapsed = sorted(VUR_collapsed, reverse = True)
	VUR_work = sorted(VUR_work, reverse = True)
	VUR_pub = sorted(VUR_pub, reverse = True)
	rank = 1
	for i in sorted(list(std_dict.keys()),reverse = True):
		for j in std_dict[i]:

			collapsed_std.write(str(rank) + j)
			rank +=1

	# for i in VUR_friends:
	# 	for j in friends_dict[i]:
	# 		friends.write(str(count)  +j)
	# 		count +=1
	# count = 1
	rank = 1
	for i in VUR_collapsed:
		for j in collapsed_dict[i]:
			collapsed.write(str(count)  +j)
			count +=1
		for j in new_collapsed[i]:
			q = j
			VUR_combined.write(q + " & " + str(i) + "(" + str(rank) + ") & " + str(new_friends[q]) + "(" + str(VUR_friends.index(new_friends[q]) +1)) 
			VUR_combined.write(") & " + str(new_pub[q]) + "("+ str(VUR_pub.index(new_pub[q]) +1))
			VUR_combined.write(") & " + str(new_work[q]) + "("+ str(VUR_work.index(new_work[q])+1 ))
			VUR_combined.write(") & " + str(new_app[q]) + "(" +str(VUR_app.index(new_app[q]) +1) + ") \\\\ \n")
			rank +=1
	count = 1


	favg = round(np.mean(recipient_friends),4)
	fvariance = 0
	fvariance = round(np.std(recipient_friends),4)
	plt.hist(edgecolor = "none",x = recipient_friends,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
	plt.axis('off')
	savefig("tables/" + "recipient_friends", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
	plt.clf()
	VUR = str(round(float(recipient_friends.count(5))/len(recipient_friends),4)*100)
	recipient_dic[VUR] = "& FRIENDS & " + VUR +" & " + str(fvariance**(0.5))+ " & \\includegraphics[width = 2cm, height = 2cm]{../tables/recipient_friends}\\\\ \n"

	wavg = round(np.mean(recipient_work),4)

	wvariance = 0
	wvariance = round(np.std(recipient_work),4)
	plt.hist(edgecolor = "none",x = recipient_work,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
	plt.axis('off')
	savefig("tables/" + "recipient_work", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
	plt.clf()
	VUR = str(round(float(recipient_work.count(5))/len(recipient_work),4)*100)
	recipient_dic[VUR] = "& WORKCONTACTS & " + VUR +" & " +str(wvariance** (0.5)) + "& \\includegraphics[width = 2cm, height = 2cm]{../tables/recipient_work}\\\\ \n"


	aavg = round(np.mean(recipient_app),4)
	avariance = round(np.std(recipient_app),4)

	plt.hist(edgecolor = "none",x = recipient_app,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
	plt.axis('off')
	savefig("tables/" + "recipient_app", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
	plt.clf()
	VUR = str(round(float(recipient_app.count(5))/len(recipient_app),4)*100)
	recipient_dic[VUR] = "& APPSERVER & " + VUR +" & "+ str(avariance ** (0.5)) + "& \\includegraphics[width = 2cm, height = 2cm]{../tables/recipient_app}\\\\ \n"


	pavg = round(np.mean(recipient_pub),4)
	pvariance = round(np.std(recipient_pub),4)
	plt.hist(edgecolor = "none",x = recipient_pub,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
	plt.axis('off')
	savefig("tables/" + "recipient_pub", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
	plt.clf()
	VUR = str(round(float(recipient_pub.count(5))/len(recipient_pub),4)*100) 
	recipient_dic[VUR] = "& PUBLIC & " + VUR +" & " +str(pvariance ** 0.5) + "& \\includegraphics[width = 2cm, height = 2cm]{../tables/recipient_pub}\\\\ \n"


	tavg = round(np.mean(recipient_total),4)
	tvariance = round(np.std(recipient_total),4)
	plt.hist(edgecolor = "none",x = recipient_total,color = 'green',bins = range(0,7),alpha = 0.5, align = 'mid', rwidth = 1,normed = True)
	plt.axis('off')
	savefig("tables/" + "recipient_total", dpi=None, facecolor='w', edgecolor='w',
			orientation='portrait', papertype=None, format=None,
			transparent=False, bbox_inches='tight', pad_inches=0,
			frameon=None)
	plt.clf()
	VUR = str(round(float(recipient_total.count(5))/len(recipient_total),4)*100)
	recipient_dic[VUR] = "& ALL & " + VUR +" & " +str(tvariance**0.5) + "& \\includegraphics[width = 2cm, height = 2cm]{../tables/recipient_total}\\\\ \n"
	rank = 1
	for i in sorted(list(recipient_dic.keys()),reverse = True):

		recipient.write(str(rank)  +recipient_dic[i])
		rank +=1


	# for i in VUR_work:
	# 	for j in work_dict[i]:
	# 		work.write(str(count)  +j)
	# 		count +=1
	# count = 1

	# for i in VUR_app:
	# 	for j in app_dict[i]:
	# 		app.write(str(count)  +j)
	# 		count +=1
	# count = 1
	# for i in VUR_pub:
	# 	for j in pub_dict[i]:
	# 		pub.write(str(count)  +j)
	# 		count +=1

	x = """\\end{longtable}
\n\\end{document}"""
	# friends.write(x)
	# work.write(x)
	# pub.write(x)
	# app.write(x)
	collapsed_std.write(x)
	collapsed.write(x)
	VUR_combined.write(x)
	recipient.write("""\hline
\end{tabular}
\end{center}
\end{table}""")

	# friends.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	# collapsed.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	# work.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	# app.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")
	# pub.write("\\hline\n\\end{tabular}\n\\caption{The 10 most and least upsetting data types, across all recipients.}\n\\label{top10}\n\\end{center}\n\\end{table}\n")


	# friends.close()
	collapsed.close()
	collapsed_std.close()
	# work.close()
	# app.close()
	# pub.close()
	VUR_combined.close()




	
parse("file.txt")
