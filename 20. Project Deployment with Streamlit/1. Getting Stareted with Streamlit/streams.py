################################## REQUIREMENTS #########################################

# 1. Your favorite IDE or text editor
# 2. Python 3.7 - Python 3.9 ( Focus on the version )
# 3. PIP

# Installation 
  # 1. pip/pip3 install streamlit
  # 2. py -m pip install streamlit (On windows if python is not added 
  #                              to path variable.)


# Test that the installation worked:
  # C:\Users\xxx\xxx>streamlit hello (on windows)
  # for mac/linux visit https://docs.streamlit.io/library/get-started/installation#install-streamlit-on-macoslinux

################################## REQUIREMENTS ENDS  #########################################










####################################### CONCEPTS #########################################

# sprinkle a few Streamlit commands into a normal Python script,
# then you run it with streamlit run
### C:\Users\xxx\xxx>streamlit run your_script.py (don't worry it should work from any dir if prev steps works.)


# As soon as you run the script as shown above, 
# A local Streamlit server will spin up and your app will open 
# in a new tab in your default web browser

# You can also pass a URL to streamlit run! This is great
# when combined with Github Gists. For example:
# $ streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

####################################### CONCEPTS ENDS  #########################################








######################### Flow Exaplianed  ############################

# Every time you want to update your app, save the source file. When you do that, 
# Streamlit detects if there is a change and asks you whether you want to rerun your app
# Choose "Always rerun" at the top-right of your screen
# Streamlit apps have a unique data flow: any time something must be updated on the screen,
# Streamlit reruns your entire Python script from top to bottom.And to make all of this fast and seamless,
# streamlit does some heavy lifting for you behind the scenes. A big player in this story is the @st.cache decorator.

######################### Flow Explanation ENDS  ############################















#########################   Magic Meaning  ############################################

# Streamlit that allows you to write almost anything (markdown, data, charts)
# without having to type an explicit command at all. Here's an example:
# Just write df , 'x',x or fig 

############ -------------------------------------------------------------------------------##############
##### Uncomment the """  """ to execute the code till next block ################


"""
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3]})
df  

x = 10
'x', x 

# Also works with most supported chart types
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig

"""

#########################   Magic Meaning ENDS   ############################################













######################### First Code Using Magic #####################################

######### My first app
######### Here's our first App on streamlit:





#import streamlit as st
#import pandas as pd
#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})

#df





######################### First Code Using Magic  ENDS  #####################################














##################### st.Write can take anything #####################################


### Along with magic commands as discussed above , st.write() is Streamlit's "Swiss Army knife".
### You can pass almost anything to st.write(): text, data, Matplotlib figures, Altair charts, and more.
### Don't worry, Streamlit will figure it out and render things the right way.
##### Uncomment the """  """ to execute the code till next block ################




#import streamlit as st
#import pandas as pd

#st.write("Here's our first attempt at using data to create a table:")
#st.write(pd.DataFrame({'first column': [1, 2, 3, 4],'second column': [10, 20, 30, 40]}))





##################### st.Write can take anything ENDS  #####################################




















############################ "Why Don't use st.write()? for everything ? " ######################


#   Sometimes you want to draw it another way 
 

############################ "Why Don't use st.write()? for everything ? ENDS  " ######################






























#######################################   Caching Basic Usage  ######################################


# The Streamlit cache allows your app to execute quickly even when loading data from the web,
#  manipulating large datasets, or performing expensive computations.



#### STARTS HERE #######



# 1. Without Caching Simple use case.


#import streamlit as st
#import time

#def expensive_computation(a, b):
    #time.sleep(2)  
    #return a * b

#a = 2
#b = 21
#res = expensive_computation(a, b)

#st.write("Result:", res)





# 2. With Caching. Do subsequent  refresh in no time.


#import streamlit as st
#import time

#@st.cache  
#def expensive_computation(a, b):
    #time.sleep(2)  # This makes the function take 2s to run
    #return a * b

#a = 2
#b = 21
#res = expensive_computation(a, b)

#st.write("Result:", res)



# 3. With Caching. First time executes st.write with cache miss
# statement but then just subsequent calls just returns the result of expensive_computation 
# on further reloads.


#import streamlit as st
#import time

#@st.cache(suppress_st_warning=True)
#def expensive_computation(a, b):
    #st.write("cache miss: expensive_computation(", a, ",", b, ") ran")
    #time.sleep(2) 
    #return a * b+1

#a = 2
#b = 22
#res = expensive_computation(a, b)

#st.write("result:", res)


# So reload on cache is done when 

# 1. The input parameters that you called the function with
# 2. The value of any external variable used in the function
# 3. The body of the function
# 4. The body of any function used inside the cached function



# Change b and execute and compare 

# Now the first time you rerun the app it's a cache miss. This is evidenced by the "Cache miss" text showing up
# and the app taking 2s to finish running. After that, if you press R to rerun, it's always a cache hit.
# That is, no such text shows up and the app is fast again.
# This is because Streamlit notices whenever the arguments a and b change and determines whether 
# the function should be re-executed and re-cached.




#######################################   Caching Basic Usage ENDS   ######################################













#######################################   Text Elements  ######################################


#import streamlit as st


############## Display text as a Header,Subheader,Title,Markdown,Caption demo

#st.header('This is a header Text')
#st.subheader('This is a subheader Text')
#st.title('This is a title Text')
#st.markdown('This is an example of  **MARKDOWN TEXT**.')
#st.caption('This is a string that explains something above.')



############## Embed Piece of code in your Webapp Demo



#code = '''def hello():
     #print("Hello, Streamlit!")'''
#st.code(code, language='python')

############## Normal Text display demo


#st.text('This is some text.')


############## Embed Equations in your webapp demo

#st.latex(r'''
     #a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     #\sum_{k=0}^{n-1} ar^k =
     #a \left(\frac{1-r^{n}}{1-r}\right)
     #''')


#######################################   Text Elements ENDS ######################################












#######################################  Data display elements  ######################################


#import streamlit as st
#import pandas as pd
#import numpy as np


############## Display Data as a Dataframe demo

#df = pd.DataFrame(
    #np.random.randn(50, 20),
    #columns=('col %d' % i for i in range(20)))

#st.dataframe(df)



############## Display Data as a Metric demo

#col1, col2, col3 = st.columns(3)
#col1.metric("Temperature", "70 F", "1.2 F")
#col2.metric("Wind", "9 mph", "-8%")
#col3.metric("Humidity", "86%", "4%")


#######################################  Data display elements ENDS ######################################









####################################### Chart elements  ######################################



#import streamlit as st
#import pandas as pd
#import numpy as np

##############  Line-Chart demo


#chart_data = pd.DataFrame(
     #np.random.randn(20, 3),
     #columns=['a', 'b', 'c'])

#st.line_chart(chart_data)



##############  Area Chart demo

#st.area_chart(chart_data)
#st.bar_chart(chart_data)



##############  Altair library chart demo


#import altair as alt

#df = pd.DataFrame(
     #np.random.randn(200, 3),
     #columns=['a', 'b', 'c'])

#c = alt.Chart(df).mark_circle().encode(
     #x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

#st.altair_chart(c, use_container_width=True)

# Examples of Altair charts can be found at https://altair-viz.github.io/gallery/.







####################################### Chart elements ENDS ######################################













####################################### Input widgets ######################################


#import streamlit as st


############## Button demo

#if st.button('Say hello'):
     #st.write('Why hello there')
#else:
     #st.write('Goodbye')




##############  Download Button demo


#text_contents = '''This is some text'''
#st.download_button('Download some text', text_contents)




##############  Checkbox demo


#agree = st.checkbox('I agree')

#if agree:
     #st.write('Great!')


##############  Radio button demo

#genre = st.radio(
     #"What's your favorite movie genre",
     #('Comedy', 'Drama', 'Documentary'))

#if genre == 'Comedy':
     #st.write('You selected comedy.')
#else:
     #st.write("You didn't select comedy.")

#title = st.text_input('Movie title', 'Life of Brian')
#st.write('The current movie title is', title)

####################################### Input widgets ENDS ######################################














####################################### Media elements ######################################


############## Loading iamge file demo


#import streamlit as st
#from PIL import Image
#image = Image.open('sunrise.jpg')

#st.image(image, caption='Sunrise by the mountains')



############## Loading Audio file demo

#audio_file = open('myaudio.ogg', 'rb')
#audio_bytes = audio_file.read()

#st.audio(audio_bytes, format='audio/ogg')



############## Loading Video file demo

#video_file = open('myvideo.mp4', 'rb')
#video_bytes = video_file.read()

#st.video(video_bytes)


####################################### Media elements ENDS  ######################################














#######################################  SideBarLayouts   ######################################

#import streamlit as st


############## SideBar Layout demo

#add_selectbox = st.sidebar.selectbox(
    #"How would you like to be contacted?",
    #("Email", "Home phone", "Mobile phone")
#)


#######################################  SideBarLayouts ENDS  ######################################












#######################################  Display progress and status   ######################################

#import time
#import streamlit as st


############## Progress bars demo
#my_bar = st.progress(0)
#for percent_complete in range(100):
     #time.sleep(0.001)
     #my_bar.progress(percent_complete + 1)


############## Spinners demo


#with st.spinner('Wait for it...'):
    #time.sleep(5)
#st.success('Done!')



############## Ballons for celebration demo


#st.balloons()




############## error demo

#st.error('This is an error')




############## warning demo

#st.warning('This is a warning')




############## Info demo

#st.info('This is a purely informational message')




############## Success celebration demo

#st.success('This is a success message!')




############## Exception demo
#e = RuntimeError('This is an exception of type RuntimeError')
#st.exception(e)


#######################################  Display progress and status ENDS   ######################################
