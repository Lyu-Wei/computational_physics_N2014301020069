# -*- coding: utf-8 -*-

import pylab as pl
class uranium_decay(object):
   
    def __init__(self, number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.n_uranium_A = [number_of_nuclei_A]
        self.n_uranium_B = [number_of_nuclei_B]
        self.t = [0]
        self.tau = time_constant
        self.dn_A = [self.n_uranium_B[0] / self.tau - self.n_uranium_A[0] / self.tau]
        self.dn_B = [self.n_uranium_A[0] / self.tau - self.n_uranium_B[0] / self.tau]
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration / time_step)
        print "Initial number of nuclei A ->", number_of_nuclei_A
        print "Initial number of nuclei B ->", number_of_nuclei_B
        print "Time constant ->", time_constant
        print "time step -> ", time_step
        print "total time -> ", time_of_duration
    def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uranium_A[i] + ( self.n_uranium_B[i] / self.tau - self.n_uranium_A[i] / self.tau ) * self.dt
            tmpB = self.n_uranium_B[i] + ( self.n_uranium_A[i] / self.tau - self.n_uranium_B[i] / self.tau ) * self.dt
            self.n_uranium_A.append(tmpA)
            self.n_uranium_B.append(tmpB)
            tmpdA = self.n_uranium_B[i+1] / self.tau - self.n_uranium_A[i+1] / self.tau
            tmpdB = self.n_uranium_A[i+1] / self.tau - self.n_uranium_B[i+1] / self.tau
            self.dn_A.append(tmpdA)
            self.dn_B.append(tmpdB)
            self.t.append(self.t[i] + self.dt)
    def show_results(self):
        plot1, = pl.plot(self.t, self.n_uranium_A)
        plot2, = pl.plot(self.t, self.n_uranium_B)
        plot3, = pl.plot(self.t, self.dn_A, '--')
        plot4, = pl.plot(self.t, self.dn_B, '--')
        pl.xlabel('time ($s$)')
        pl.legend([plot1, plot2, plot3, plot4], [r'$N_A$', r'$N_B$', r'$dN_A/dt$', r'$dN_B/dt$'], loc="best")
        pl.show()
    
    def store_results(self):
        myfile = open('Exercise_04_data.txt', 'w')
        for i in range(len(self.t)):
            myfile.write(str(self.t[i]) + '\t' + str(self.n_uranium_A[i]) + '\t' + str(self.n_uranium_B[i]) + '\t' + str(self.dn_A[i]) + '\t' + str(self.dn_B[i]) + '\n')
        myfile.close()    
    
a = uranium_decay()
a.calculate()
a.show_results()
a.store_results()

import math
class exact_results_check(uranium_decay):
    def show_results(self):
        self.etA = []
        self.etB = []
        for i in range(len(self.t)):
            tempA = (self.n_uranium_A[0] + self.n_uranium_B[0]) * 0.5 + (self.n_uranium_A[0] - self.n_uranium_B[0]) * 0.5 * math.exp(- 2 * self.t[i] / self.tau)
            tempB = (self.n_uranium_A[0] + self.n_uranium_B[0]) * 0.5 + (self.n_uranium_B[0] - self.n_uranium_A[0]) * 0.5 * math.exp(- 2 * self.t[i] / self.tau)
            self.etA.append(tempA)
            self.etB.append(tempB)
        plot1, = pl.plot(self.t, self.etA, '--')
        plot2, = pl.plot(self.t, self.etB, '--')
        plot3, = pl.plot(self.t, self.n_uranium_A)
        plot4, = pl.plot(self.t, self.n_uranium_B)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.legend([plot1, plot2, plot3, plot4], [r'$N_A$ analytic solutions ', r'$N_B$ analytic solutions ', r'$N_A$ numerical solutions', r'$N_B$ numerical solutions'], loc="best")
        pl.xlim(0, self.time)
        pl.show()
b = exact_results_check(number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_step=0.05)
b.calculate()
b.show_results()       

c = uranium_decay(number_of_nuclei_A = 200, number_of_nuclei_B = 0, time_constant = 1, time_step=0.05)
c.calculate()
c.show_results()

d = uranium_decay(number_of_nuclei_A = 100, number_of_nuclei_B = 50, time_constant = 1, time_step=0.05)
d.calculate()
d.show_results()

e = uranium_decay(number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 5, time_step=0.05)
e.calculate()
e.show_results()

f = uranium_decay(number_of_nuclei_A = 100, number_of_nuclei_B = 0, time_constant = 1, time_step=0.5)
f.calculate()
f.show_results()