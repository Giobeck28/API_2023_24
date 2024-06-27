import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from PIL import Image
import time
import plotly.figure_factory as ff
import matplotlib.ticker as mtick
import itertools

vacs =[7,14, 20, 27]
#file_name = '/Users/gio/Downloads/stats_2023_24.xlsm'
file_name = 'stats_2023_24.xlsm'
nombre_manche_Y = 33
nombre_manche_Q = 11
nombre_manche_V = 5

sleep_presences_on_off = "off"
#sleep_presences_on_off = "on"
sleep_presences = 0.01
sleep_vacances = 1
sleep_ranking_start = 1
sleep_ranking = 0.001


st.title("Season 2023-2024")
df_points = pd.read_excel(file_name, \
    sheet_name = 'For stats end Y points', index_col = 0)

df_score = pd.read_excel(file_name, \
    sheet_name = 'For stats end Y Score', index_col = 0)

df_average = pd.read_excel(file_name, \
    sheet_name = 'Moy')

df_pres = pd.read_excel(file_name, \
    sheet_name = 'Pres-NumPlayers')

df_pres_var = pd.read_excel(file_name, \
    sheet_name = 'VDistribP')

df_score = df_score.iloc[:,0:nombre_manche_Y]

presences = 110 - (df_points == 0).sum(axis=0)
manches_variantes = [13.5, 19.5, 27.5 ,31.5, 33.5]
presences_variantes = [33,30,29,26,0]
vacs_variantes = [19.5 , 27.5]
vacs_variantes_pres = [30,29]


#df_score

total_score = df_score.cumsum(axis = 1)
#total_score 





#imageLocation.image(old_image)
#if st.checkbox('New Layer'):
#    imageLocation.image(new_image)




## Sidebar
#image = Image.open('/Users/gio/Downloads/testlogo.png')
image = Image.open('testlogo.png')
st.sidebar.image(image, caption='ASSOCIATION DE POKER ISSEENNE')
pages = ['', 'Evolution Présences', 'Distribution Présences API & GO','Distribution Présences Irish','Moyennes API & GO', 'Championat API & GO', ]
pages_2 = ['', 'Evolution Présences', 'Distribution Présences API & GO','Moyennes API & GO', 'Championat API & GO', ]
pages_3 = ['', 'Evolution Présences', 'Distribution Présences API & GO', 'Championat API & GO', ]
page = st.sidebar.radio("Menu", options = pages_2)
#API_GO = Image.open('/Users/gio/Downloads/API&GO.jpg')
API_GO = Image.open('API&GO.jpg')
    

if page == pages[0]:
    st.image(API_GO)
        # title (ou of chart) 
    #original_title = '<p style="font-family:Courier; color:Black; font-size: 50px;">Season 2021-2022 </p>'
    #st.markdown(original_title, unsafe_allow_html=True)

#################
### PRESENCES ###
#################
if page == pages[1]:
    # title (ou of chart) 
    #original_title = '<p style="font-family:Courier; color:Black; font-size: 50px;">Evolution des présences </p>'
    #st.markdown(original_title, unsafe_allow_html=True)
    
    
    placeholder = st.empty()
    # set layout parameters
    size_ticks = 25
    size_title = 200
    size_axes = 30
    size_title = 50
    marker = 'o'
    marker_size  = 35
    marker_size_d  = 25
    mfc_ = 'g'
    mec_ = 'g'
    line_width = 0
    for j in range(nombre_manche_Y):
        manche = j + 1
        if sleep_presences_on_off == 'on' : 
            time.sleep(sleep_presences)
        fig, ax = plt.subplots(figsize =(20,10))
        fig.set_facecolor('#15B01A')
        fig.set_facecolor('#04D8B2')
        fig.set_facecolor("green")
        
        #ax.set_title('Evolution des présences', fontsize = size_title, fontweight='bold')
        ax.set_ylabel('Jouers', fontsize = size_axes, color ='w', fontweight='bold')
        ax.set_xlabel('Manches', fontsize = size_axes,  color ='w', fontweight='bold')
        ax.set_title('Evolution des Présences', fontsize=size_title, color= 'w')#fontweight='bold',
        ax.set_xlim(0, nombre_manche_Y+1)
        ax.set_ylim(20, 70)
        ax.spines['bottom'].set_color('w')
        ax.spines['left'].set_color('w')
        ax.spines['top'].set_color('green')
        ax.spines['right'].set_color('green')
        ax.set(facecolor = "green")
        ax.grid(visible=None, which='major', axis='both', color='w', linestyle=':', linewidth=2)

        #ax.set_yticks(fontsize=20)
        plt.yticks(fontsize=size_ticks, color ='w')
        plt.xticks(fontsize=size_ticks,  color ='w')

        #if j in range(12,25,1):
        #    mfc_ = 'w'
        #    start = j//nombre_manche_Q * nombre_manche_Q
        #    ax.plot(df_points.columns[start:j], presences[start:j], marker=marker,         
        #        markersize = marker_size,
        #       mfc = mfc_,
        #        mec = mec_,
        #        linewidth= line_width)
        #    mfc_ = 'w'
        if j in range(nombre_manche_Q):
            mfc_ = 'black'
            start = j//nombre_manche_Q * nombre_manche_Q
            ax.plot(df_points.columns[start:j+1], presences[start:j+1], marker=r'$\spadesuit$', #marker=marker,         
                markersize = marker_size,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            
            placeholder.pyplot(fig)
        if j in range(nombre_manche_Q,nombre_manche_Q*2): 
            mfc_ = 'black'
            ax.plot(df_points.columns[:nombre_manche_Q], presences[0:nombre_manche_Q], marker=r'$\spadesuit$',         
                markersize = marker_size,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            
            mfc_ = 'red'
            start = j//nombre_manche_Q * nombre_manche_Q
            ax.plot(df_points.columns[start:j+1], presences[start:j+1], marker='D',         
                markersize = marker_size_d,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            
            placeholder.pyplot(fig)
        if j in range(nombre_manche_Q*2,nombre_manche_Y):        
            mfc_ = 'black'
            ax.plot(df_points.columns[:nombre_manche_Q], presences[0:nombre_manche_Q], marker=r'$\spadesuit$',         
                markersize = marker_size,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            
            mfc_ = 'r'
            ax.plot(df_points.columns[nombre_manche_Q:nombre_manche_Q*2], presences[nombre_manche_Q:nombre_manche_Q*2], marker=r'D',        
                markersize = marker_size_d,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            
            mfc_ = '#2E3033'#'k'
            start = j//nombre_manche_Q * nombre_manche_Q
            ax.plot(df_points.columns[start:j+1], presences[start:j+1], marker=r'$\clubsuit$',         
                markersize = marker_size,
                mfc = mfc_,
                mec = mec_,
                linewidth= line_width)
            if j == nombre_manche_Y -1 :
                time.sleep(sleep_vacances)
                for vac in vacs:
                   # ax.scatter(df_points.columns[vac-1], presences[vac], marker='o',
                   #     s= 20, facecolors='none', edgecolors='gold')
                    ax.plot(df_points.columns[vac-1], presences[vac], marker='o',
                    markersize = marker_size,
                    mfc = "none",
                    mec = "gold",
                    linewidth= line_width)      
                i = 1
                #TEST VARIANTES
                #mfc_list =['c','b','aqua']
                mfc_list =['b','b','b']
                for n in range(3):
                    mfc_ = mfc_list[n]     
                    ax.plot(manches_variantes[3*n:3*(n+1)] ,presences_variantes[3*n:3*(n+1)] , marker='*',         
                    markersize = int(marker_size),
                    mfc = mfc_,
                    mec = mec_,
                    linewidth= line_width)

                ax.plot(vacs_variantes, vacs_variantes_pres, marker='o',
                    markersize = marker_size,
                    mfc = "none",
                    mec = "gold",
                    linewidth= line_width)  
                ###

                ax.plot((0,40) , (presences[0:nombre_manche_Y].mean(),presences[0:nombre_manche_Y].mean()), linewidth= 5, color = 'y', linestyle=':')
                ax.plot((1,nombre_manche_Q) , (presences[0:nombre_manche_Q].mean(),presences[0:nombre_manche_Q].mean()), linewidth= 3, color = 'k', linestyle='-')
                ax.plot((nombre_manche_Q+1 ,nombre_manche_Q*2) , (presences[nombre_manche_Q:nombre_manche_Q*2].mean(),presences[nombre_manche_Q:nombre_manche_Q*2].mean()), linewidth= 3, color = 'r', linestyle='-')
                ax.plot((nombre_manche_Q*2 + 1,nombre_manche_Y) , (presences[nombre_manche_Q*2:nombre_manche_Y].mean(),presences[nombre_manche_Q*2:nombre_manche_Y].mean()), linewidth= 3, color = '#2E3033', linestyle='-')
                

            placeholder.pyplot(fig)
    m_T1 = str(round(presences[0:nombre_manche_Q].mean()))
    m_T2 = str(round(presences[nombre_manche_Q:nombre_manche_Q*2].mean()))
    m_T3 = str(round(presences[nombre_manche_Q*2:nombre_manche_Y].mean()))
    m_Y = str(round(presences[0:nombre_manche_Y].mean()))
    #m_v = str(round(sum(presences_variantes)/len(presences_variantes)))
    m_v = str(round(sum(presences_variantes)/(4)))

    st.write('Moyennes API & GO:  ', 'T1= ' , m_T1, '  ; T2=', m_T2, '  ; T3=', m_T3, '  ; Année=', m_Y)
    st.write('Moyenne Irish:  ' , m_v)

        
#################
### Distribution Presences ###
#################
if page == pages[2]:
    placeholder_p = st.empty()
    slider_range = st.slider("Range de présences", min_value=1, max_value=nombre_manche_Y, value=[1,nombre_manche_Y])
    a = slider_range[0]
    b = slider_range[1]
    tot_players =  df_pres['Players'][a:b+1].sum()
    #st.write(tot_players)
    prob =[]
    for n_players in df_pres['Players'][a:b+1]:
        prob.append(n_players/tot_players)
    cum= []
    for i in range(b+1-a):
        cum.append(sum(prob[i:b+1-a]))
   

    size_ticks = 25
    size_title = 200
    size_axes = 30
    size_title = 50
    marker = 'o'
    marker_size  = 35
    marker_size_d  = 25
    mfc_ = 'y'
    mec_ = 'y'
    line_width = 0
    fig, ax_p = plt.subplots(figsize =(20,10))
    #fig.set_facecolor('#15B01A')
    

    
    #ax.set_title('Evolution des présences', fontsize = size_title, fontweight='bold')
    ax_p.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax_p.set_ylabel('% de Jouers', fontsize = size_axes, color ='k', fontweight='bold')
    ax_p.set_xlabel('Manches disputées', fontsize = size_axes,  color ='k', fontweight='bold')
    title_= f"Distribution Cumulative des Présences\n API & GO - {tot_players} Jouers"
    ax_p.set_title(title_, fontsize=size_title, color= 'k')#fontweight='bold',
    ax_p.set_xlim(a, b)
    ax_p.set_ylim(0, 1)
    ax_p.spines['bottom'].set_color('k')
    ax_p.spines['left'].set_color('k')
    ax_p.spines['top'].set_color('k')
    ax_p.spines['right'].set_color('k')
    ax_p.set(facecolor = "w")
    ax_p.grid(visible=None, which='major', axis='both', color='k', linestyle=':', linewidth=2)

    #ax.set_yticks(fontsize=20)

  
    plt.yticks(fontsize=size_ticks, color ='k')
    plt.xticks(fontsize=size_ticks,  color ='k')
    if a ==1:
        #plt.xticks(itertools.chain(range(1,2),range(a-1, b+1,5)))
        plt.xticks(range(a-1, b+1,5))
    else:
        plt.xticks(range(a, b+1,5))
    plt.xlim(a, b)

    ax_p.fill_between(range(a,b+1), cum,
                 color="lime", alpha=0.3)
    ax_p.plot(range(a,b+1), cum , marker=marker,         
            markersize = 0,
            mfc = mfc_,
            mec = mec_,
            c='g',
            linewidth=  5)

    #ax_2p = ax_p.twinx()

    secax = ax_p.secondary_yaxis('right', 
        functions=(lambda x: x*tot_players, lambda x: x/tot_players))
    secax.set_ylabel('Nombre de Jouers', fontsize = size_axes, color ='k', fontweight='bold')
    ticks = [round(tot_players/5) * i for i in range(6)]
    if tot_players - ticks[5] > 3 :
        ticks.append(tot_players)
    else:
        ticks.pop()
        ticks.append(tot_players)
    secax.set_yticks(ticks)
    secax.tick_params(axis = 'y', labelsize = size_ticks, color ='k')


        
    placeholder_p.pyplot(fig)
    


        
#################
### Distribution Presences Variantes###
#################
if page == pages[3]:
    placeholder_p = st.empty()
    slider_range = st.slider("Range de présences", min_value=1, max_value=nombre_manche_V, value=[1,nombre_manche_V])
    a = slider_range[0]
    b = slider_range[1]
    tot_players =  df_pres_var['Players'][a:b+1].sum()
    #st.write(tot_players)
    prob =[]
    for n_players in df_pres_var['Players'][a:b+1]:
        prob.append(n_players/tot_players)
    cum= []
    for i in range(b+1-a):
        cum.append(sum(prob[i:b+1-a]))
   

    size_ticks = 25
    size_title = 200
    size_axes = 30
    size_title = 50
    marker = 'o'
    marker_size  = 35
    marker_size_d  = 25
    mfc_ = 'y'
    mec_ = 'y'
    line_width = 0
    fig, ax_p = plt.subplots(figsize =(20,10))
    #fig.set_facecolor('#15B01A')
    

    
    #ax.set_title('Evolution des présences', fontsize = size_title, fontweight='bold')
    ax_p.yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1, decimals=0))
    ax_p.set_ylabel('% of Jouers', fontsize = size_axes, color ='k', fontweight='bold')
    ax_p.set_xlabel('Manches disputées', fontsize = size_axes,  color ='k', fontweight='bold')
    title_= f"Distribution Cumulative des Présences\n Irish - {tot_players} Jouers"
    ax_p.set_title(title_, fontsize=size_title, color= 'k')#fontweight='bold',
    ax_p.set_xlim(a, b)
    ax_p.set_xticks(range(a, b+1))
    ax_p.set_ylim(0, 1)
    ax_p.spines['bottom'].set_color('k')
    ax_p.spines['left'].set_color('k')
    ax_p.spines['top'].set_color('k')
    ax_p.spines['right'].set_color('k')
    ax_p.set(facecolor = "w")
    ax_p.grid(visible=None, which='major', axis='both', color='k', linestyle=':', linewidth=2)

    #ax.set_yticks(fontsize=20)

  
    plt.yticks(fontsize=size_ticks, color ='k')
    plt.xticks(fontsize=size_ticks,  color ='k')

    ax_p.fill_between(range(a,b+1), cum,
                 color="skyblue", alpha=0.4)
    ax_p.plot(range(a,b+1), cum , marker=marker,         
            markersize = 0,
            mfc = mfc_,
            mec = mec_,
            linewidth=  5)

    #ax_2p = ax_p.twinx()

    secax = ax_p.secondary_yaxis('right', 
        functions=(lambda x: x*tot_players, lambda x: x/tot_players))
    secax.set_ylabel('Nombre de Jouers', fontsize = size_axes, color ='k', fontweight='bold')
    ticks = [round(tot_players/5) * i for i in range(6)]
    if tot_players - ticks[5] > 3 :
        ticks.append(tot_players)
    else:
        ticks.pop()
        ticks.append(tot_players)
    secax.set_yticks(ticks)
    secax.tick_params(axis = 'y', labelsize = size_ticks, color ='k')


        
    placeholder_p.pyplot(fig)
    




#################
### AVERAGES ####
#################
if page == pages[4]:
    #from bokeh.models.tools import LassoSelectTool
    #lasso = LassoSelectTool()
  # title (ou of chart) 
    original_title = '<p style="font-family:Courier; color:Black; font-size: 50px;">Moyennes vs. Présences </p>'
    st.markdown(original_title, unsafe_allow_html=True)

    from bokeh.plotting import figure
    from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, Scatter, Circle
    from bokeh.palettes import Magma, Inferno, Plasma, Viridis, Cividis, Oranges
    from bokeh.transform import transform


    
    #source = ColumnDataSource(dict(x=x, y=y))

    source = ColumnDataSource(df_average)
    plot = Plot(
     title=None, width=400, height=500,
     min_border=0, toolbar_location="below")


    from bokeh.models import LinearColorMapper, ColorBar
    import matplotlib as mpl
    #import numpy as np
  
    #colors = ["#%02x%02x%02x" % (int(r), int(g), int(b)) for r, g, b, _ in 255*mpl.cm.viridis(mpl.colors.Normalize()(16))]
    
    #glyph = Scatter(x="P", y="Moyenne", size=10, fill_color= colors)  #fill_color="#74add1")
    #glyph = Scatter(x="P", y="Moyenne", size=10, fill_color="#74add1")
    color = LinearColorMapper(palette = 'Inferno256',
                          low = df_average.Moyenne.max(),
                          high = df_average.Moyenne.min())
    
    glyph = Circle (x="P", y="Moyenne",
                fill_color = transform('Moyenne', color),
                radius = 0.4, fill_alpha = 0.5)
    plot.add_glyph(source, glyph)
    xaxis = LinearAxis()
    plot.add_layout(xaxis, 'below')
    plot.xaxis.major_label_text_font_size = "15pt"
    

    yaxis = LinearAxis()
    plot.add_layout(yaxis, 'left')
    plot.yaxis.major_label_text_font_size = "15pt"

    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

    from bokeh.models import HoverTool

    tooltips =[('Pseudo:', '@Pseudo'),('Moyenne, Présences:','@Moyenne{0.0}, @P')]

    #p = figure(plot_width = 600, plot_height = 400)

    #c = p.circle(x ='x' , y = 'y', source = source)

    hover = HoverTool(tooltips = tooltips)# , renderers = [c])

    plot.add_tools(hover)
    #plot.add_tools(lasso)
    #gio = source.selected.indices


    #p = figure(
    #    title='simple line example',
    #    x_axis_label='x',
    #    y_axis_label='y')

    #p.Scatter(x, y, legend_label='Trend', size = 20)

    st.bokeh_chart(plot, use_container_width=True)
    #st.write(gio)

#################
### Ranking ###
#################
if page == pages[5]:
    
    #original_title = '<p style="font-family:Courier; color:Black; font-size: 50px;">Deroulement du Championnat </p>'
    #st.markdown(original_title, unsafe_allow_html=True)

    placeholder_c = st.empty()
    st.image(API_GO)

    size_ticks = 25
    size_title = 200
    size_axes = 30
    size_title = 50
    

    #time.sleep(sleep_ranking_start)
    for j in range(nombre_manche_Y):
        if j == 1:
            time.sleep(sleep_ranking_start)
    #for j in range(3):
        time.sleep(sleep_ranking)
        figc, ax1 = plt.subplots(figsize =(20,10))
        ax1.set_ylabel('Points', fontsize = size_axes, fontweight='bold', color ='k')
        ax1.set_xlabel('Manches', fontsize = size_axes, fontweight='bold', color ='k')
        ax1.set_title('Déroulement du Championnat', fontsize=size_title, color= 'k')#fontweight='bold',

        ax1.set_xlim(0, nombre_manche_Y+1)
        ax1.set_ylim(0, 350)
        plt.yticks(fontsize=size_ticks, color ='k')
        plt.xticks(fontsize=size_ticks,  color ='k')
        ax1.grid(visible=None, which='major', axis='both', color='k', linestyle=':', linewidth=2)


        winner = df_score[nombre_manche_Y-1].idxmax() 
        runner_up = df_score.drop(winner)[nombre_manche_Y-1].idxmax() 
        third = df_score.drop([winner, runner_up])[nombre_manche_Y-1].idxmax() 

        #for i in range(110):
        for i, player  in enumerate(list(df_score.index.values)):
            size_ = 2 
            if player  == winner:
                size_ = 7
                #color_ = 'gold'
                color_ = 'b'
                ax1.plot(df_score.columns[0:j+1], df_score.iloc[i,:j+1], linewidth= size_, color = color_)
            elif player == runner_up:
                size_ = 7
                #color_ = 'silver'
                color_ = 'r'
                ax1.plot(df_score.columns[0:j+1], df_score.iloc[i,:j+1], linewidth= size_, color = color_)
            elif player == third:
                size_ = 7
                #color_ = 'brown'
                color_ = 'k'
                ax1.plot(df_score.columns[0:j+1], df_score.iloc[i,:j+1], linewidth= size_, color = color_)    
            else:
                ax1.plot(df_score.columns[0:j+1], df_score.iloc[i,:j+1], linewidth= size_)
     
        placeholder_c.pyplot(figc)
    #plt.show()


     
