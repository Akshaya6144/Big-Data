import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
random=[]
ll=[]
rr=[]
with open("logs.txt",'r') as f1:
	logs=f1.readlines()

k=0
for i in range(len(logs)):
	
	if(logs[i]=='RANDOM\n'):
		k=1
		continue
	if(logs[i]=='LL\n'):
		k=2
		continue
	if(logs[i]=='RR\n'):
		k=3
		continue
	if(k==1):
		
		random.append(logs[i])
	if(k==2):
		ll.append(logs[i])
	if(k==3):
		rr.append(logs[i])

random.sort()
ll.sort()

rr.sort()
#print(random)
#print(ll)

def get_results(filename):
	
	joblist={}
	
	with open(filename,"r") as f:
		while True:
			line=f.readline()
			if not line:
				break
			#print(line)
			line=line.strip()
			line=line.split(",")
			joblist[line[2]]=(line[3],line[0])
			#print(joblist)
	if(filename=='RANDOM'):
		tasktime=[]
		jobtime=[]
		for i in range(len(random)):
			random[i]=random[i].strip("\n")
			random[i]=random[i].split(",")
		
			if(i%2!=0):
				#print(random[i])
				
				t=(float(random[i][2])-float(random[i-1][2]))
				tasktime.append(t)
				
				mr,rid=(random[i][0].split("_")[1][0],int(random[i][0].split("_")[1][1:]))
				#print(mr,rid)
				jid=random[i][0].split("_")[0]
	
				#print(jid)
				#print(type(rid))
				#print(type(joblist[jid][0]))
				
				if(mr=='R'):
					#print(rid)
				
					if(rid==int(joblist[jid][0])):
						#print(rid,jid,joblist[jid][0],random[i][2],joblist[jid][1])
						jtime=(float(random[i][2])-float(joblist[jid][1]))
						jobtime.append(jtime)
		
	if(filename=='LL'):
		tasktime=[]
		jobtime=[]
		for i in range(len(ll)):
			ll[i]=ll[i].strip("\n")
			ll[i]=ll[i].split(",")
		
			if(i%2!=0):
				
				t=(float(ll[i][2])-float(ll[i-1][2]))
				tasktime.append(t)
				
				mr,rid=(ll[i][0].split("_")[1][0],int(ll[i][0].split("_")[1][1:]))
				#print(mr,rid)
				jid=ll[i][0].split("_")[0]
				#print(jid)
				#print(type(rid))
				#print(type(joblist[jid][0]))
				
				if(mr=='R'):
					#print(rid)
				
					if(rid==int(joblist[jid][0])):
						#print(rid,jid,joblist[jid][0],ll[i][2],joblist[jid][1])
						jtime=(float(ll[i][2])-float(joblist[jid][1]))
						jobtime.append(jtime)
	if(filename=='RR'):
		tasktime=[]
		jobtime=[]
		for i in range(len(rr)):
			rr[i]=rr[i].strip("\n")
			rr[i]=rr[i].split(",")
		
			if(i%2!=0):
				
				t=(float(rr[i][2])-float(rr[i-1][2]))
				tasktime.append(t)
				
				mr,rid=(rr[i][0].split("_")[1][0],int(rr[i][0].split("_")[1][1:]))
				#print(mr,rid)
				jid=rr[i][0].split("_")[0]
				#print(jid)
				#print(type(rid))
				#print(type(joblist[jid][0]))
				
				if(mr=='R'):
					#print(rid)
				
					if(rid==int(joblist[jid][0])):
						#print(rid,jid,joblist[jid][0],rr[i][2],joblist[jid][1])
						jtime=(float(rr[i][2])-float(joblist[jid][1]))
						jobtime.append(jtime)	
				
	
	tasktime=sorted(tasktime)
	jobtime=sorted(jobtime)
	
	mean_task=np.mean(tasktime)	
	mean_job=np.mean(jobtime)
	print("Mean of tasks and jobs of "+filename+' algorithm'+' '+str(mean_task)+' '+str(mean_job))	
	
	median_task=np.median(tasktime)	
	median_job=np.median(jobtime)
	print("Median of tasks and jobs of "+filename+' algorithm'+' '+str(median_task)+' '+str(median_job))
	
files=['RANDOM','LL','RR']

for filename in files:
	get_results(filename)
#print(random)	
#print(logs)		
workerRandom_1=0
workerRandom_2=0
workerRandom_3=0
r_1=[]
r_2=[]
r_3=[]	
timeRandom_1=0
timeRandom_2=0
timeRandom_3=0			
for i in range(len(random)):
	if(random[i][4]=='1'):
		
		workerRandom_1+=1
		r_1.append(random[i][2])
	if(random[i][4]=='2'):
		workerRandom_2+=1
		r_2.append(random[i][2])
	if(random[i][4]=='3'):
		workerRandom_3+=1
		r_3.append(random[i][2])

if (len(r_1)>0):
	timeRandom_1=float(max(r_1))-float(min(r_1))
if (len(r_2)>0):
	timeRandom_2=float(max(r_2))-float(min(r_2))
if (len(r_3)>0):
	timeRandom_3=float(max(r_3))-float(min(r_3))
x=[timeRandom_1,timeRandom_2,timeRandom_3]
y=[workerRandom_1/2,workerRandom_2/2,workerRandom_3/2]

classes=['worker1','worker2','worker3']
colors = ['red','green','blue']
l1=plt.scatter(x[0],y[0],c=colors[0])
l2=plt.scatter(x[1],y[1],c=colors[1])
l3=plt.scatter(x[2],y[2],c=colors[2])

plt.legend((l1,l2,l3),labels=('worker1','worker2','worker3'), scatterpoints=1)

#plt.legend((colors),['worker1','worker2','worker3'])
plt.title('Random')
plt.xlabel('time')
plt.ylabel('number of task')
plt.show()		
workerll_1=0
workerll_2=0
workerll_3=0
l_1=[]
l_2=[]
l_3=[]	
			
for i in range(len(ll)):
	if(ll[i][4]=='1'):
		workerll_1+=1
		l_1.append(ll[i][2])
	if(ll[i][4]=='2'):
		workerll_2+=1
		l_2.append(ll[i][2])
	if(ll[i][4]=='3'):
		workerll_3+=1
		l_3.append(ll[i][2])
timell_1=0
timell_2=0
timell_3=0
if(len(l_1)>0):
	timell_1=float(max(l_1))-float(min(l_1))
if(len(l_2)>0):
	timell_2=float(max(l_2))-float(min(l_2))
if(len(l_3)>0):
	timell_3=float(max(l_3))-float(max(l_3))
x=[timell_1,timell_2,timell_3]
y=[workerll_1/2,workerll_2/2,workerll_3/2]
classes=['worker1','worker2','worker3']
colors = ['red','green','blue']
l1=plt.scatter(x[0],y[0],c=colors[0])
l2=plt.scatter(x[1],y[1],c=colors[1])
l3=plt.scatter(x[2],y[2],c=colors[2])

plt.legend((l1,l2,l3),labels=('worker1','worker2','worker3'), scatterpoints=1)

#plt.legend((colors),['worker1','worker2','worker3'])
plt.title('LeastLoaded')
plt.xlabel('time')
plt.ylabel('number of task')
plt.show()
workerRR_1=0
workerRR_2=0
workerRR_3=0
rr_1=[]
rr_2=[]
rr_3=[]	
timeRR_1=0
timeRR_2=0
timeRR_3=0	
		
for i in range(len(rr)):
	if(rr[i][4]=='1'):
		
		workerRR_1+=1
		rr_1.append(rr[i][2])
	if(rr[i][4]=='2'):
		workerRR_2+=1
		rr_2.append(rr[i][2])
	if(rr[i][4]=='3'):
		workerRR_3+=1
		rr_3.append(rr[i][2])


if (len(rr_1)>0):
	timeRR_1=float(max(rr_1))-float(min(rr_1))
if (len(rr_2)>0):
	timeRR_2=float(max(rr_2))-float(min(rr_2))
if (len(rr_3)>0):
	timeRR_3=float(max(rr_3))-float(min(rr_3))
	
x=[timeRR_1,timeRR_2,timeRR_3]
y=[workerRR_1/2,workerRR_2/2,workerRR_3/2]
classes=['worker1','worker2','worker3']
colors = ['red','green','blue']
l1=plt.scatter(x[0],y[0],c=colors[0])
l2=plt.scatter(x[1],y[1],c=colors[1])
l3=plt.scatter(x[2],y[2],c=colors[2])

plt.legend((l1,l2,l3),labels=('worker1','worker2','worker3'), scatterpoints=1)

#plt.legend((colors),['worker1','worker2','worker3'])
plt.title('RoundRobin')
plt.xlabel('time')
plt.ylabel('number of task')
plt.show()		
