# Scalar and Vector Spherical Harmonic Visualiser with GUI.  
# This version adapted to suit definitions from:  
#  Section 2 from R. Grinter, J. Phys. B At. Mol. Opt. Phys., 2014, 47, 075004.  
#  Table 1 from 1 R. Grinter, J. Phys. B At. Mol. Opt. Phys., 2008, 41, 095001.  
  
#~Shalini Narayan, 09/04/2019~  
  
  
import matplotlib.pyplot as plt  
import numpy as np  
from mpl_toolkits.mplot3d import axes3d  
import matplotlib.cm as cm  #Import colour maps  
from tkinter import *                    # Python 3 GUI   
import tkinter.ttk as ttk  
from tkinter.messagebox import showinfo  # dialogue box   
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg #Canvas and toolbar  
import scipy.special as scp #For sph_harm function  
import sys  
  
  
  
#Vector Spherical Harmonics   
  
#1      Y000 = 0  
Y_000 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' :0}  
  
#2      Y010 = (1/sqrt(3){Y1+1 * e1-1 - Y10 * e10 + Y1+1 * e1+1}  
Y_010 = {'e1min1_CG': +0.5774, 'e1min1_l': +1, 'e1min1_m' : +1, 'e10_CG' : -0.5774, 'e10_l' : +1, 'e10_m' : 0, 'e1pl1_CG' : +0.5774, 'e1pl1_l' : +1, 'e1pl1_m' :-1}  
  
#3      Y10+1 = Y00 * e1+1  
Y_10pl1 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : +1, 'e1pl1_l' : 0, 'e1pl1_m' : 0}  
  
#4      Y100 = Y00 * e10  
Y_100 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : +1, 'e10_l' :0 , 'e10_m' : 0, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' : 0 }  
  
#5      Y10-1 = Y00 * e1-1  
Y_10min1 = {'e1min1_CG': +1 , 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' : 0}  
  
#6      Y11+1 = (1/sqrt(2)){Y1+1 *e10 - Y10 * e1+1}  
Y_11pl1 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : +0.7071, 'e10_l' : +1, 'e10_m' : +1, 'e1pl1_CG' : -0.7071, 'e1pl1_l' : +1, 'e1pl1_m' : 0 }  
  
  
#7      Y110 = (1/sqrt(2)){Y1+1 * e1-1 - Y1-1 * e1+1}  
Y_110 = {'e1min1_CG': +0.7071, 'e1min1_l': +1, 'e1min1_m' : +1, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : -0.7071, 'e1pl1_l' : +1, 'e1pl1_m' : +1}  
  
  
#8      Y11-1 = (1/sqrt(2)){Y10 * e1-1 - Y1-1 * e10}  
Y_11min1 = {'e1min1_CG': -0.7071, 'e1min1_l': +1, 'e1min1_m' : 0, 'e10_CG' : +0.7071, 'e10_l' : +1, 'e10_m' : 0, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' :0 }  
  
  
#9      Y12+1 = (1/sqrt(10)){sqrt(6)Y2+2 * e1-1 - sqrt(3)Y2+1 * e10 + Y20 * e1+1}  
Y_12pl1 = {'e1min1_CG': +0.7746, 'e1min1_l': +2, 'e1min1_m' : +2, 'e10_CG' : -0.5477, 'e10_l' : +2, 'e10_m' : +1, 'e1pl1_CG' : +0.3162, 'e1pl1_l' : +2, 'e1pl1_m' : 0}  
  
  
#10     Y120 = (1/sqrt(10){sqrt(3)Y2+1 * e1-1 - 2Y20 * e10 + sqrt(3)Y2-1 * e1+1  
Y_120 = {'e1min1_CG': +0.5477, 'e1min1_l': +2, 'e1min1_m' : +1, 'e10_CG' : -0.6325, 'e10_l' : +2, 'e10_m' : 0, 'e1pl1_CG' : +0.5477, 'e1pl1_l' : +2, 'e1pl1_m' : -1}  
  
  
#11     Y21-1 = (1/sqrt(10)){Y20 * e1-1 - sqrt(3)Y2-1 * e10 + sqrt(6)Y2-2 * e1+1}  
Y_12min1 = {'e1min1_CG': +0.3162, 'e1min1_l': +2, 'e1min1_m' : 0, 'e10_CG' : -0.5477, 'e10_l' : +2, 'e10_m' : -1, 'e1pl1_CG' : +0.7746, 'e1pl1_l' : +2, 'e1pl1_m' : -2}  
  
  
#12     Y21+2 = Y1+1 * e1+1  
Y_21pl2 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : +1, 'e1pl1_l' : +1, 'e1pl1_m' : +1}  
  
  
#13     Y21+1 = (1/sqrt(2){Y1+1 * e10 + Y10 * e1+1}  
Y_21pl1 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : +0.7071, 'e10_l' : +1, 'e10_m' : +1, 'e1pl1_CG' : +0.7071, 'e1pl1_l' : +1, 'e1pl1_m' : 0}  
  
  
#14     Y210 = (1/sqrt(6){Y1+1 * e1-1 + 2Y10 * e10 + Y1-1 * e1+1}   
Y_210 = {'e1min1_CG': +0.4082, 'e1min1_l': +1, 'e1min1_m' : +1, 'e10_CG' : +0.8165, 'e10_l' : +1, 'e10_m' : 0, 'e1pl1_CG' : +0.4082, 'e1pl1_l' : +1, 'e1pl1_m' : -1}  
  
  
#15     Y21-1 = (1/sqrt(2)){Y10 * e1-1 + Y1-1 * e10}  
Y_21min1 = {'e1min1_CG': +0.7071, 'e1min1_l': +1, 'e1min1_m' : 0, 'e10_CG' : +0.7071, 'e10_l' : +1, 'e10_m' : -1, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' : 0}  
  
  
#16     Y21-2 = Y1-1 * e1-1  
Y_21min2 = {'e1min1_CG': +1, 'e1min1_l': +1, 'e1min1_m' : -1, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' : 0}  
  
  
#17     Y22+2 = (1/sqrt(3)){sqrt(@)Y2+2 * e10 - Y2+1 * e1+1}  
Y_22pl2 = {'e1min1_CG': 0, 'e1min1_l': 0, 'e1min1_m' : 0, 'e10_CG' : +0.8165, 'e10_l' : +2, 'e10_m' : +2, 'e1pl1_CG' : -0.5774, 'e1pl1_l' : +2, 'e1pl1_m' : +1}  
  
  
#18     Y22+1 = (1/ sqrt(6)){sqrt(2)Y2+2 * e1-1 + Y2+1 * e10 - sqrt(3)Y20 * e1+1}  
Y_22pl1 = {'e1min1_CG': +0.5774, 'e1min1_l': +2, 'e1min1_m' : +2, 'e10_CG' : +0.4082, 'e10_l' : +2, 'e10_m' : +1, 'e1pl1_CG' : -0.7071, 'e1pl1_l' : +2, 'e1pl1_m' : 0}  
  
  
#19     Y220 = (1/sqrt(2)){Y2+1 * e1-1 - Y2-1 * e1+1}  
Y_220 = {'e1min1_CG': +0.7071, 'e1min1_l': +2, 'e1min1_m' : +1, 'e10_CG' : 0, 'e10_l' : 0, 'e10_m' : 0, 'e1pl1_CG' : -0.7071, 'e1pl1_l' : +2, 'e1pl1_m' : -1}  
  
  
#20     Y22-1 = (1/sqrt(6)){sqrt(3)Y20 * e1-1 - Y2-1 * e10 - sqrt(2)Y2-2 * e1+1}  
Y_22min1 = {'e1min1_CG': +0.7071, 'e1min1_l': +2, 'e1min1_m' : 0, 'e10_CG' : -0.4082, 'e10_l' : +2, 'e10_m' : -1, 'e1pl1_CG' : -0.5774, 'e1pl1_l' : +2, 'e1pl1_m' : -2}  
  
  
#21     Y22-2 = (1/sqrt(3)){Y2-1 * e1-1 - sqrt(2)Y2-2 * e10}  
Y_22min2 = {'e1min1_CG': +0.5774, 'e1min1_l': +2, 'e1min1_m' : -1, 'e10_CG' : -0.8165, 'e10_l' : +2, 'e10_m' : -2, 'e1pl1_CG' : 0, 'e1pl1_l' : 0, 'e1pl1_m' : 0}  
  
  
#22     Y23+2 = (1/sqrt(21)){sqrt(15)Y3+3 * e1-1 - sqrt(5)Y3+2 * e10 + Y3+1 * e1+1}  
Y_23pl2 = {'e1min1_CG': +0.8452, 'e1min1_l': +3, 'e1min1_m' : +3, 'e10_CG' : -0.4880, 'e10_l' : +3, 'e10_m' : +2, 'e1pl1_CG' : +0.2182, 'e1pl1_l' : +3, 'e1pl1_m' : +1}  
  
  
#23     Y23+1 = (1/sqrt(21)){sqrt(15)Y3+3 * e1-1 - sqrt(15)Y3+2 * e10 + Y3+1 * e1+1}  
Y_23pl1 = {'e1min1_CG': +0.6901, 'e1min1_l': +3, 'e1min1_m' : +2, 'e10_CG' : -0.6172, 'e10_l' : +3, 'e10_m' : +1, 'e1pl1_CG' : +0.3780, 'e1pl1_l' : +3, 'e1pl1_m' : 0}  
  
  
#24     Y230 = (1/sqrt(7)){sqrt(2)Y3+1 * e1-1 - sqrt(3)Y30 * e10 + sqrt(2)Y3-1 * e1+1}  
Y_230 = {'e1min1_CG': 0.5345, 'e1min1_l': +3, 'e1min1_m' : +1, 'e10_CG' : -0.6547, 'e10_l' : +3, 'e10_m' : 0, 'e1pl1_CG' : +0.5345, 'e1pl1_l' : +3, 'e1pl1_m' : -1}  
  
  
#25     Y23-1 = (1/sqrt(21)){sqrt(3)Y30 * e1-1 - sqrt(8)Y3-1 *  e10 + sqrt(10)Y3-2 * e1+1}  
Y_23min1 = {'e1min1_CG': +0.3780, 'e1min1_l': +3, 'e1min1_m' : 0, 'e10_CG' : -0.6172, 'e10_l' : +3, 'e10_m' : -1, 'e1pl1_CG' : +0.6901, 'e1pl1_l' : +3, 'e1pl1_m' : -2}  
  
#26     Y23-1 = (1/sqrt(21)){sqrt(3)Y3-1 * e1-1 - sqrt(5)Y3-2 * e10 + sqrt(15)Y3-3 * e1+1}  
Y_23min2 = {'e1min1_CG': +0.2182, 'e1min1_l': +3, 'e1min1_m' : -1, 'e10_CG' : -0.4880, 'e10_l' : +3, 'e10_m' : -2, 'e1pl1_CG' : +0.8452, 'e1pl1_l' : +3, 'e1pl1_m' : -3}  
  
VSH = {'000' : Y_000, '010' : Y_010, '10+1' : Y_10pl1, '100' : Y_100, '10-1' : Y_10min1, '11+1' : Y_11pl1, '110' : Y_110, '11-1' : Y_11min1, '12+1' : Y_12pl1, '120' : Y_120, '12-1' : Y_12min1, '21+2' : Y_21pl2, '21+1' : Y_21pl1, '210' : Y_210, '21-1' : Y_21min1, '21-2' : Y_21min2, '22+2' : Y_22pl2, '22+1' : Y_22pl1, '220' : Y_220, '22-1' : Y_22min1, '22-2' : Y_22min2, '23+2' : Y_23pl2, '23+1' : Y_23pl1, '230' : Y_230, '23-1' : Y_23min1, '23-2' : Y_23min2}  
  
#Define a Custom plotting toolbar  
class SaveToolbar(NavigationToolbar2TkAgg):  
    toolitems = [('Home', 'Reset original view', 'home', 'home'),('Pan', 'Pan axes with left mouse, zoom with right', 'move', 'pan'),('Zoom', 'Zoom to rectangle', 'zoom_to_rect', 'zoom'),('Save', 'Save current plot.', 'filesave', 'save_figure')]  
    def __init__(self, plotCanvas,master_frame):  
        NavigationToolbar2TkAgg.__init__(self, plotCanvas,master_frame)  
  
class VSH_GUI(Frame):  
    def __init__(self,parent):                                           # reserved name defined by __ , self => the object we are in  
        self.parent = parent                                             # parent is the master frame   
        self.parent.title('VSH GUI')                                     # what appears in top left of window  
        self.parent.wm_protocol("WM_DELETE_WINDOW", self.destroyer)      # Clean exit  
        self.Fig = plt.figure(figsize=(6,6))                             # Initialise matplotlib plot, keep size x=y for spherical plots  
        self.make_widgets()  
    def destroyer(self):  
        self.parent.quit()  
        self.parent.destroy()  
    def make_widgets(self):                                              # defining a new function with access the attributes of class  
        LHS = Frame(self.parent)  
        LHS.pack(side=LEFT,expand=YES,padx=2)  
        Label(LHS,text='Vector Spherical Harmonics Visualiser').pack(side=TOP,pady=5)  
        Button(LHS, text='Quit',command=self.destroyer,height=2,width=15).pack(side=BOTTOM,pady=5)  
        Label(LHS,text='Scalar Field').pack(side=TOP,pady=5)  
        Input_Row = Frame(LHS)  
        Input_Row.pack(side=TOP,expand=YES,pady=2)  
        Label(Input_Row,text='l:').pack(side=LEFT,padx=2)  
        self.Entl = Entry(Input_Row,width=10,justify=CENTER)  
        self.Entl.pack(side=LEFT,padx=2)  
        Label(Input_Row,text='m:').pack(side=LEFT,padx=2)  
        self.Entm = Entry(Input_Row,width=10,justify=CENTER)  
        self.Entm.pack(side=LEFT,padx=2)  
        Label(LHS,text='Real/Imag/Mod:').pack(side=TOP,pady=2)  
        #ComboBox for real and imaginary  
        style = ttk.Style()  
        style.map('TCombobox',fieldbackground=[('readonly','white')])  
        self.ComplexPartBox = ttk.Combobox(LHS,width=8,state='readonly',values=['Real','Imag','Mod'])  
        self.ComplexPartBox.set('Real')  
        self.ComplexPartBox.pack(side=TOP,pady=5)  
        #Plotting Buttons  
        Button(LHS,text='Plot \n <Return>',height=3,width=15,justify=CENTER,command=self.Plot).pack(side=TOP,pady=5)  
        self.parent.bind('<Return>',self.PlotEvent)  
        #Vector Fields  
        Label(LHS,text='Vector Field').pack(side=TOP,pady=5)  
        Row1 = Frame(LHS)  
        Row1.pack(side=TOP,expand=YES,pady=2)  
        Label(Row1,text=r'factor').pack(side=LEFT,padx=2)  
        self.ent_f1 = Entry(Row1,width=10,justify=CENTER)  
        self.ent_f1.insert(0,'1')  
        self.ent_f1.pack(side=LEFT,padx=2)  
        Label(Row1,text=r'J').pack(side=LEFT,padx=2)  
        self.ent_j1 = Entry(Row1,width=10,justify=CENTER)  
        self.ent_j1.insert(0,'1')  
        self.ent_j1.pack(side=LEFT,padx=2)  
        Label(Row1,text='l:').pack(side=LEFT,padx=2)  
        self.ent_l1 = Entry(Row1,width=10,justify=CENTER)  
        self.ent_l1.insert(0,'0')  
        self.ent_l1.pack(side=LEFT,padx=2)  
        Label(Row1,text='M:').pack(side=LEFT,padx=2)  
        self.ent_m1 = Entry(Row1,width=10,justify=CENTER)  
        self.ent_m1.insert(0,'0')  
        self.ent_m1.pack(side=LEFT,padx=2)  
  
        Row2 = Frame(LHS)   
        Row2.pack(side=TOP,expand=YES,pady=2)  
        Label(Row2,text=r'factor').pack(side=LEFT,padx=2)  
        self.ent_f2 = Entry(Row2,width=10,justify=CENTER)  
        self.ent_f2.insert(0,'0')  
        self.ent_f2.pack(side=LEFT,padx=2)  
        Label(Row2,text=r'J').pack(side=LEFT,padx=2)  
        self.ent_j2 = Entry(Row2,width=10,justify=CENTER)  
        self.ent_j2.insert(0,'0')  
        self.ent_j2.pack(side=LEFT,padx=2)  
        Label(Row2,text='l:').pack(side=LEFT,padx=2)  
        self.ent_l2 = Entry(Row2,width=10,justify=CENTER)  
        self.ent_l2.insert(0,'0')  
        self.ent_l2.pack(side=LEFT,padx=2)  
        Label(Row2,text='M:').pack(side=LEFT,padx=2)  
        self.ent_m2 = Entry(Row2,width=10,justify=CENTER)  
        self.ent_m2.insert(0,'0')  
        self.ent_m2.pack(side=LEFT,padx=2)  
  
        Label(LHS, text = 'for plus put +, for minus put -').pack(side=TOP,padx=2)  
  
        #Plotting Buttons  
        Button(LHS,text='Plot',height=3,width=15,justify=CENTER,command=self.PlotVector).pack(side=TOP,pady=5)  
        RHS = Frame(self.parent)  
        RHS.pack(side=RIGHT,expand=YES,padx=2)  
        self.canvas = FigureCanvasTkAgg(self.Fig,master=RHS)  
        self.canvas.get_tk_widget().pack(side=TOP,expand=YES, pady=5)  
        toolbar = SaveToolbar(self.canvas, RHS)  
        toolbar.pack(side=TOP,expand=YES)  
    def PlotEvent(self,event):  
        self.PlotVector()  
    def Plot(self):  
        #Clear figure  
        plt.clf()  
        #Read in m and l  
        m = int(self.Entm.get())  
        l = int(self.Entl.get())  
        #Define phi and theta  
        theta = np.linspace(0,np.pi,101)  
        phi = np.linspace(0,2*np.pi,101)  
        theta,phi = np.meshgrid(theta,phi)  
        #Calculate scalar spherical harmonic  
        Y = scp.sph_harm(m,l,phi,theta)  
  
        if self.ComplexPartBox.get() == 'Real':  
            Y = Y.real  
        elif self.ComplexPartBox.get() == 'Imag':  
            Y = Y.imag  
        elif self.ComplexPartBox.get() == 'Mod':  
            Y = np.sqrt(Y.real**2+Y.imag**2)  
        #Normalize to between 0 - 1  
        Y_norm = (Y-Y.min())/(Y.max()-Y.min())  
        #Convert to Cartesian  
        x = np.sin(theta) * np.cos(phi)  
        y = np.sin(theta) * np.sin(phi)  
        z = np.cos(theta)  
        #Setup plot for 3D surface  
        ax = self.Fig.gca(projection='3d')  
        ax.plot_surface(x,y,z,rstride=1, cstride=1, facecolors=cm.seismic(Y_norm))  
        #Plot  
        ax.set_axis_off()  
        plt.gcf().canvas.draw()  
    def calc_y(self, e1min1_CG, e1min1_m, e1min1_l, e10_CG, e10_m, e10_l, e1pl1_CG, e1pl1_m, e1pl1_l, theta, phi):  
        def Rz(angle): #Rotate about z  
            return np.matrix([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])  
        def Ry(angle): #Rotate about y  
            return np.matrix([[np.cos(angle),0,np.sin(angle)],[0,1,0],[-np.sin(angle),0,np.cos(angle)]])  
        def D(alpha,beta,gamma): #Rotation matrix, for spherical polar coordinates: alpha = phi, beta = theta, gamma = 0   
            return Rz(alpha)*Ry(beta)*Rz(gamma)  
  
        #Define e1min1,e10,e1pl1 as vectors in (Theta,Phi,R) for all theta and phi  
        e1min1 = np.zeros(shape=(len(theta),len(phi),3),dtype='complex')  
        e10 = np.zeros(shape=(len(theta),len(phi),3),dtype='complex')  
        e1pl1 = np.zeros(shape=(len(theta),len(phi),3),dtype='complex')  
        for i in range(len(theta)):  
            for j in range(len(phi)):  
                e1min1[i,j] = np.array([np.exp(-(0+1j)*phi[j])*np.cos(theta[i])/np.sqrt(2),-(0+1j)*np.exp(-(0+1j)*phi[j])/np.sqrt(2),np.exp(-(0+1j)*phi[j])*np.sin(theta[i])/np.sqrt(2)])  
                e10[i,j] = np.array([-np.sin(theta[i]),0,np.cos(theta[i])])  
                e1pl1[i,j] = np.array([-np.exp((0+1j)*phi[j])*np.cos(theta[i])/np.sqrt(2),-(0+1j)*np.exp((0+1j)*phi[j])/np.sqrt(2),-np.exp((0+1j)*phi[j])*np.sin(theta[i])/np.sqrt(2)])  
  
        #Calculate Vector spherical harmonic vectors in (Theta,Phi,R) for all theta and phi  
        Y = np.zeros(shape=(len(theta),len(phi),3),dtype='complex')  
        for i in range(len(theta)):  
            for j in range(len(phi)):  
                Y[i,j] = e1min1_CG*scp.sph_harm(e1min1_m,e1min1_l,phi[j],theta[i])*e1min1[i,j,:]+ e10_CG*scp.sph_harm(e10_m,e10_l,phi[j],theta[i])*e10[i,j,:]+ e1pl1_CG*scp.sph_harm(e1pl1_m,e1pl1_l,phi[j],theta[i])*e1pl1[i,j,:]  
        #Rotate from (Theta,Phi,R) to (x,y,z)  
        for i in range(len(theta)):  
            for j in range(len(phi)):  
                Y[i,j] = np.array((D(phi[j],theta[i],0)*np.matrix(Y[i,j]).T).T)  
        return Y  
  
    def PlotVector(self):  
        #Clear figure  
        plt.clf()  
        #Read in CG, m and l for 3 polarisations  
        #e1min1 = Right Circ., e1pl1 = Left Circ., e10 = Longitudinally polarised.   
        f1 = complex(self.ent_f1.get())  
        j1 = (self.ent_j1.get())  
        m1 = (self.ent_m1.get())  
        l1 = (self.ent_l1.get())  
        f2 = complex(self.ent_f2.get())  
        j2 = (self.ent_j2.get())  
        m2 = (self.ent_m2.get())  
        l2 = (self.ent_l2.get())  
        #retrive from dictionary   
        key1 = j1+l1+m1  
        key2 = j2+l2+m2  
        y1 = VSH[key1]  
        y2 = VSH[key2]  
  
  
        #Define phi and theta  
        theta = np.linspace(0,np.pi,11)  
        phi = np.linspace(0,2*np.pi,21)  
  
        #calculate Y   
        Y1 = self.calc_y(y1['e1min1_CG'], y1['e1min1_m'],y1['e1min1_l'], y1['e10_CG'], y1['e10_m'], y1['e10_l'], y1['e1pl1_CG'], y1['e1pl1_m'], y1['e1pl1_l'], theta, phi)  
        Y2 = self.calc_y(y2['e1min1_CG'], y2['e1min1_m'],y2['e1min1_l'], y2['e10_CG'], y2['e10_m'], y2['e10_l'], y2['e1pl1_CG'], y2['e1pl1_m'], y2['e1pl1_l'], theta, phi)  
  
        #combine Y1 and Y2  
  
        Y = f1 * Y1 + f2 * Y2  
  
        if self.ComplexPartBox.get() == 'Real':  
            Y = Y.real  
        elif self.ComplexPartBox.get() == 'Imag':  
            Y = Y.imag  
        elif self.ComplexPartBox.get() == 'Mod':  
            Y = np.sqrt(Y.real**2+Y.imag**2)  
        #Convert theta & phi to Cartesian for plotting coordinates  
        x = np.zeros(shape=(len(theta),len(phi)))  
        y = np.zeros(shape=(len(theta),len(phi)))  
        z = np.zeros(shape=(len(theta),len(phi)))  
        for i in range(len(theta)):  
            for j in range(len(phi)):  
                x[i,j] = np.sin(theta[i])*np.cos(phi[j])  
                y[i,j] = np.sin(theta[i])*np.sin(phi[j])  
                z[i,j] = np.cos(theta[i])  
        #Setup plot for 3D surface  
        ax = self.Fig.gca(projection='3d')  
        ax.quiver(x, y, z, Y[:,:,0], Y[:,:,1], Y[:,:,2], length=0.2)#,pivot='middle')  
        #Plot  
        #ax.set_axis_off()  
        ax.view_init(elev=25,azim=42)  
        ax.set_xlabel(r'$\mathrm{x}$')  
        ax.set_ylabel(r'$\mathrm{y}$')  
        ax.set_zlabel(r'$\mathrm{z}$')  
        plt.gcf().canvas.draw()  
  
# Main program  
  
root= Tk()                             # starts up the tkinter package  
VSH_GUI(root)                          # defined the frame of the GUI  
root.mainloop()                        # wait for instructions from GUI  
sys.exit(1)                            # Close all top level processes  
 
