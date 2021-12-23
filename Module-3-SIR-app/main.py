import streamlit as st
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', True)

import matplotlib.pyplot as plt
import numpy as np








header = st.beta_container()
body = st.beta_container()
decsription = st.beta_container()



with header:

	st.title('SIR Model')
	st.markdown('Enrico Borriello,\n**Latest update:** Dec 22, 2021\n**contact:** enrico.borriello@asu.edu')


with body:

	col_A, col_B, col_C, col_D = st.beta_columns([1,1,1,3])

	c = col_A.number_input('contact rate',format='%.4f',value=0.001)
	r = col_B.number_input('recovery rate',format='%.4f',value=0.1)
	col_C.text(' ')
	col_C.text(' ')
	col_C.text(' ')
	col_C.text(' ')
	col_C.text(' ') # is there a better way of doing this?

	N = col_C.text('\n')

	S0 = col_A.number_input('susceptible individuals',value=999,step=1)
	I0 = col_B.number_input('infected individuals',value=1,step=1)
	R0 = col_C.number_input('recovered individuals',value=0,step=1)

	t1 = col_A.number_input('initial time',format='%.2f',value=0)
	t2 = col_B.number_input('final time',format='%.2f',value=100)
	Nt = col_C.number_input('number of time bins',value=100,step=1)

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

# initial condition
x0 = [S0,I0,R0]

# ODEs
def odes(x,t):
    S = x[0]
    I = x[1]
    R = x[2]
    dSdt = -c*I*S 
    dIdt = c*I*S -r*I
    dRdt = r*I 
    return [dSdt,dIdt,dRdt]

t = np.linspace(t1,t2,Nt)
x = odeint(odes,x0,t)

S = x[:,0]
I = x[:,1]
R = x[:,2]



fig, ax = plt.subplots(figsize=(5,2.5))
plt.plot(t,S,label='S')
plt.plot(t,I,label='I')
plt.plot(t,R,label='R')
plt.legend()
plt.xlabel('time')
#plt.savefig('SIR_solution.pdf')
col_D.pyplot(fig)


with decsription:

	st.header('Description of the model')

	f = open('SIR_text_1.txt')
	content = f.read()
	st.markdown(content)
	st.image('fig1.png',width=500)
	f = open('SIR_text_2.txt')
	content = f.read()
	st.markdown(content)
	r'''
	$$\frac{dS}{dt} = -cSI$$ 
	'''
	r'''
	$$\frac{dI}{dt} = cSI -rI$$ 
	'''
	r'''
	$$\frac{dR}{dt} = rI$$ 
	'''
	f = open('SIR_text_3.txt')
	content = f.read()
	st.markdown(content)










