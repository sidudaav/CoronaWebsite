import pandas as pd     
import pathlib
import seaborn as sns
from datetime import datetime
import os                   
from pytrends.request import TrendReq
import time
from time import sleep
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.image as mpimg
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader

files = pathlib.Path(__file__).parent.absolute()
MapsHolder_dir  = str(files) + '/static/MapsHolder/'

pytrend = TrendReq()




def rank_simple(vector):
    return sorted(range(len(vector)), key=vector.__getitem__)



def date_diff(d1, d2):
  date_format = '%Y-%m-%d'
  a = datetime.strptime(d1, date_format)
  b = datetime.strptime(d2, date_format)
  delta = str(b - a)
  delta_split = delta.split(' ')
  return delta_split[0]




def rankdata(a):
    n = len(a)
    ivec=rank_simple(a)
    svec=[a[rank] for rank in ivec]
    sumranks = 0
    dupcount = 0
    newarray = [0]*n
    for i in range(n):
        sumranks += i
        dupcount += 1
        if i==n-1 or svec[i] != svec[i+1]:
            averank = sumranks / float(dupcount) + 1
            for j in range(i-dupcount+1,i+1):
                newarray[ivec[j]] = averank
            sumranks = 0
            dupcount = 0
    return newarray

case_list = ['NY', 'NJ', 'MI', 'LA', 'CA', 'MA', 'PA', 'FL', 'IL',
             'GA', 'TX', 'CT', 'WA', 'MD', 'IN', 'CO', 'OH', 'TN', 'VA',
             'NC', 'MO', 'WI', 'AZ', 'SC', 'AL', 'NV', 'MS', 'UT',
             'OK', 'RI', 'ID', 'OR', 'MN', 'KY', 'IA', 'AR', 'DE', 'KS', 'NM',
             'NH', 'VT', 'ME', 'NE', 'WV', 'HI', 'MT', 'SD', 'ND',
             'WY', 'AK']

state_list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
                'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
                'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

new_case_list = case_list[::-1]





def case_MSQE(in_list):
  rank = rankdata(in_list)
  MSQE = 0
  for i in range(0, 50): 
    state = state_list[i]
    if   rank[i] - new_case_list.index(state) - 1:
      MSQE = MSQE + (( rank[i] - new_case_list.index(state) - 1)**2)
      
  MSQE = MSQE / 50

  return MSQE




def get_diff(in_list):
  out_list = []
  rank = rankdata(in_list)
  for i in range(0, 50):
    state = state_list[i]
    diff = rank[i] - new_case_list.index(state) - 1
    out_list.append(diff)
  
  return out_list





def convert(in_list):
  out_list = []
  for i in range(0, len(in_list)):
      if in_list[i] == 'AK':
        out_list.append('Alaska')
      if in_list[i] == 'AL':
        out_list.append('Alabama')
      if in_list[i] == 'AR':
        out_list.append('Arkansas')
      if in_list[i] == 'AZ':
        out_list.append('Arizona')
      if in_list[i] == 'CA':
        out_list.append('California')
      if in_list[i] == 'CO':
        out_list.append('Colorado')
      if in_list[i] == 'CT':
        out_list.append('Connecticut')
      if in_list[i] == 'DE':
        out_list.append('Delaware')
      if in_list[i] == 'FL':
        out_list.append('Florida')
      if in_list[i] == 'GA':
        out_list.append('Georgia')
      if in_list[i] == 'HI':
        out_list.append('Hawaii')
      if in_list[i] == 'IA':
        out_list.append('Iowa')
      if in_list[i] == 'ID':
        out_list.append('Idaho')
      if in_list[i] == 'IL':
        out_list.append('Illinois')
      if in_list[i] == 'IN':
        out_list.append('Indiana')
      if in_list[i] == 'KS':
        out_list.append('Kansas')
      if in_list[i] == 'KY':
        out_list.append('Kentucky')
      if in_list[i] == 'LA':
        out_list.append('Louisiana')
      if in_list[i] == 'MA':
        out_list.append('Massachusetts')
      if in_list[i] == 'MD':
        out_list.append('Maryland')
      if in_list[i] == 'ME':
        out_list.append('Maine')
      if in_list[i] == 'MI':
        out_list.append('Michigan')
      if in_list[i] == 'MN':
        out_list.append('Minnesota')
      if in_list[i] == 'MO':
        out_list.append('Missouri')
      if in_list[i] == 'MS':
        out_list.append('Mississippi')
      if in_list[i] == 'MT':
        out_list.append('Montana')
      if in_list[i] == 'NC':
        out_list.append('North Carolina')
      if in_list[i] == 'ND':
        out_list.append('North Dakota')
      if in_list[i] == 'NE':
        out_list.append('Nebraska')
      if in_list[i] == 'NH':
        out_list.append('New Hampshire')
      if in_list[i] == 'NJ':
        out_list.append('New Jersey')
      if in_list[i] == 'NM':
        out_list.append('New Mexico')
      if in_list[i] == 'NV':
        out_list.append('Nevada')
      if in_list[i] == 'NY':
        out_list.append('New York')
      if in_list[i] == 'OH':
        out_list.append('Ohio')
      if in_list[i] == 'OK':
        out_list.append('Oklahoma')
      if in_list[i] == 'OR':
        out_list.append('Oregon')
      if in_list[i] == 'PA':
        out_list.append('Pennsylvania')
      if in_list[i] == 'RI':
        out_list.append('Rhode Island')
      if in_list[i] == 'SC':
        out_list.append('South Carolina')
      if in_list[i] == 'SD':
        out_list.append('South Dakota')
      if in_list[i] == 'TN':
        out_list.append('Tennessee')
      if in_list[i] == 'TX':
        out_list.append('Texas')
      if in_list[i] == 'UT':
        out_list.append('Utah')
      if in_list[i] == 'VA':
        out_list.append('Virginia')
      if in_list[i] == 'VT':
        out_list.append('Vermont')
      if in_list[i] == 'WA':
        out_list.append('Washington')
      if in_list[i] == 'WI':
        out_list.append('Wisconsin')
      if in_list[i] == 'WV':
        out_list.append('West Virginia')
      if in_list[i] == 'WY':
        out_list.append('Wyoming')

  return out_list






def get_map(word, t1, t2, youtube):
  plt.switch_backend('Agg')
  sig_lev = None
  kw_list = [word]

  #for i in range(0, n): 
      #keyword = input()
      #kw_list.append(keyword) # adding the element 

  for kw in kw_list: 
    globals()[kw + '_counter'] = 0
    globals()[kw + '_states'] = []
    globals()[kw + '_increase_states'] = []
    globals()[kw + '_significance_level'] = []
    globals()[kw + '_all_significance_level'] = []

  for state in state_list:
    significant_keyword = True
    increase = True
    significant_list = []
    increase_list = []
    occurrences_list = []

    for kw in kw_list:
      new_kw_list = [kw]

      if youtube == False:
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t1, geo='US-' + state, gprop='')
        df1 = pytrend.interest_over_time()
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t2, geo='US-' + state, gprop='')
        df2 = pytrend.interest_over_time()
      else:
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t1, geo='US-' + state, gprop= youtube)
        df1 = pytrend.interest_over_time()
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t2, geo='US-' + state, gprop= youtube)
        df2 = pytrend.interest_over_time()

      val_start = df1[kw].mean()
      val_end = df2[kw].mean()

      if val_end >= val_start:
        globals()[kw + '_all_significance_level'].append(val_end / max(val_start, 1))
        globals()[kw + '_increase_states'].append(state)
      if val_start > val_end:
        globals()[kw + '_all_significance_level'].append(val_start / max(1, val_end))

      if val_end > 1.3 * val_start:
        significant_keyword = True
        increase = True
        sig_lev = val_end / max(val_start, 1)
        globals()[kw + '_significance_level'].append(sig_lev)
      elif 1.3 * val_end < val_start:
        significant_keyword = True
        increase = False
        sig_lev = val_start / max(val_end, 1)
        globals()[kw + '_significance_level'].append(sig_lev)
      else:
        significant_keyword = False
        increase = 'N/A'
      
      if significant_keyword == True:
        globals()[kw + '_counter'] = globals()[kw + '_counter'] + 1
        globals()[kw + '_states'].append(state)

      significant_list.append(significant_keyword)
      increase_list.append(increase)

      time.sleep(0.5)

    globals()[state + '_df'] = pd.DataFrame(
        {'Keyword': kw_list,
        'Significance?': significant_list,
        'Increase?': increase_list
        })
    
  for kw in kw_list: 
    occurrences_list.append(globals()[kw + '_counter'])

  occurrences_df = pd.DataFrame(
      {'Keyword': kw_list,
      'Occurrecnes': occurrences_list,
      })

  kw = word

  full_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
                'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
                  'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
                  'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                  'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

  fig = plt.figure()
  ax = fig.add_axes([0, 0, 1, 1], projection=ccrs.LambertConformal())

  ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

  shapename = 'admin_1_states_provinces_lakes_shp'
  states_shp = shpreader.natural_earth(resolution='110m',
                                      category='cultural', name=shapename)


  popdensity = dict(zip(full_states, globals()[kw + '_all_significance_level']))  

  ax.background_patch.set_visible(False)
  ax.outline_patch.set_visible(False)

  ax.set_title('State Search Trend Change For ' + str(word))

  #for state in shpreader.Reader(states_shp).geometries():
  for astate in shpreader.Reader(states_shp).records():

      ### You want to replace the following code with code that sets the
      ### facecolor as a gradient based on the population density above
      #facecolor = [0.9375, 0.9375, 0.859375]

      edgecolor = 'black'
      facecolor = "white"

      try:
          # use the name of this state to get pop_density
          state_dens = popdensity[ astate.attributes['name'] ]
      except:
          state_dens = 0

      # simple scheme to assign color to each state
      if astate.attributes['name'] in convert(globals()[kw + '_increase_states']):
        if 1.3 < state_dens <= 1.5:
          facecolor = '#C8C8FF'
        if 1.5 < state_dens <= 1.7:
          facecolor = '#AFAFFF'
        if 1.7 < state_dens <= 1.9:
          facecolor = '#9696FF'
        if 1.9 < state_dens <= 2.1:
          facecolor = '#7D7DFF'
        if 2.1 < state_dens <= 2.3:
          facecolor = '#6464FF'
        if 2.3 < state_dens <= 2.5:
          facecolor = '#4B4BFF'
        if 2.5 < state_dens <= 2.7:
          facecolor = '#3232FF'
        if 2.7 < state_dens <= 2.9:
          facecolor = '#1919FF'
        if 2.9 < state_dens:
          facecolor = '#0000FF'
      else:
        if 1.3 < state_dens <= 1.5:
          facecolor = '#FFC8C8'
        if 1.5 < state_dens <= 1.7:
          facecolor = '#FFAFAF'
        if 1.7 < state_dens <= 1.9:
          facecolor = '#FF9696'
        if 1.9 < state_dens <= 2.1:
          facecolor = '#FF7D7D'
        if 2.1 < state_dens < 2.3:
          facecolor = '#FF6464'
        if 2.3 < state_dens < 2.5:
          facecolor = '#FF4B4B'
        if 2.5 < state_dens < 2.7:
          facecolor = '#FF3232'
        if 2.7 < state_dens < 2.9:
          facecolor = '#FF1919'  
        if 2.9 < state_dens:
          facecolor = '#FF0000'
        
      # `astate.geometry` is the polygon to plot
      ax.add_geometries([astate.geometry], ccrs.PlateCarree(),
                          facecolor=facecolor, edgecolor=edgecolor)
  
  blue_patch1 = mpatches.Patch(color='#C8C8FF', label='The red data')
  blue_patch2 = mpatches.Patch(color='#AFAFFF', label='The red data')
  blue_patch3 = mpatches.Patch(color='#9696FF', label='The red data')
  blue_patch4 = mpatches.Patch(color='#7D7DFF', label='The red data')
  blue_patch5 = mpatches.Patch(color='#6464FF', label='The red data')
  blue_patch6 = mpatches.Patch(color='#4B4BFF', label='The red data')
  blue_patch7 = mpatches.Patch(color='#3232FF', label='The red data')
  blue_patch8 = mpatches.Patch(color='#1919FF', label='The red data')
  blue_patch9 = mpatches.Patch(color='#0000FF', label='The red data')
  red_patch1 = mpatches.Patch(color='#FF0000', label='The red data')
  red_patch2 = mpatches.Patch(color='#FF1919', label='The red data')
  red_patch3 = mpatches.Patch(color='#FF3232', label='The red data')
  red_patch4 = mpatches.Patch(color='#FF4B4B', label='The red data')
  red_patch5 = mpatches.Patch(color='#FF6464', label='The red data')
  red_patch6 = mpatches.Patch(color='#FF7D7D', label='The red data')
  red_patch7 = mpatches.Patch(color='#FF9696', label='The red data')
  red_patch8 = mpatches.Patch(color='#FFAFAF', label='The red data')
  red_patch9 = mpatches.Patch(color='#FFC8C8', label='The red data')

  plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0., handles=[blue_patch1, blue_patch2, blue_patch3, blue_patch4, blue_patch5, blue_patch6, blue_patch7,
  blue_patch8, blue_patch9, red_patch1, red_patch2, red_patch3, red_patch4, red_patch5, red_patch6, red_patch7,
  red_patch8, red_patch9])
                        
  ax.background_patch.set_alpha(0)
  fig.patch.set_alpha(0)

  save_results_to = str(MapsHolder_dir) 
  plt.savefig(save_results_to +  'Map.png', dpi = 1000, tansparent = True)
  





def get_data(word, t1, t2, youtube):

  state_list = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
                'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY',
                'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

  full_states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
                'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
                'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
                  'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma',
                  'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                  'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
  
  sig_lev = None
  kw_list = [word]

  #for i in range(0, n): 
      #keyword = input()
      #kw_list.append(keyword) # adding the element 

  for kw in kw_list: 
    globals()[kw + '_counter'] = 0
    globals()[kw + '_states'] = []
    globals()[kw + '_increase_states'] = []
    globals()[kw + '_significance_level'] = []
    globals()[kw + '_all_significance_level'] = []
    globals()[kw + '_all_increase_level'] = []

  for state in state_list:
    significant_keyword = True
    increase = True
    significant_list = []
    increase_list = []
    occurrences_list = []

    for kw in kw_list:
      new_kw_list = [kw]

      if youtube == False:
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t1, geo='US-' + state, gprop='')
        df1 = pytrend.interest_over_time()
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t2, geo='US-' + state, gprop='')
        df2 = pytrend.interest_over_time()
      else:
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t1, geo='US-' + state, gprop= youtube)
        df1 = pytrend.interest_over_time()
        pytrend.build_payload(new_kw_list, cat=0, timeframe= t2, geo='US-' + state, gprop= youtube)
        df2 = pytrend.interest_over_time()        

      val_start = df1[kw].mean()
      val_end = df2[kw].mean()

      if val_end >= val_start:
        globals()[kw + '_all_increase_level'].append('Increase')
        globals()[kw + '_all_significance_level'].append(val_end / max(val_start, 1))
        globals()[kw + '_increase_states'].append(state)
      if val_start > val_end:
        globals()[kw + '_all_increase_level'].append('Decrease')
        globals()[kw + '_all_significance_level'].append(val_start / max(1, val_end))

      if val_end > 1.3 * val_start:
        significant_keyword = True
        increase = True
        sig_lev = val_end / max(val_start, 1)
        globals()[kw + '_significance_level'].append(sig_lev)
      elif 1.3 * val_end < val_start:
        significant_keyword = True
        increase = False
        sig_lev = val_start / max(val_end, 1)
        globals()[kw + '_significance_level'].append(sig_lev)
      else:
        significant_keyword = False
        increase = 'N/A'
      
      if significant_keyword == True:
        globals()[kw + '_counter'] = globals()[kw + '_counter'] + 1
        globals()[kw + '_states'].append(state)

      significant_list.append(significant_keyword)
      increase_list.append(increase)

      time.sleep(0.5)

    globals()[state + '_df'] = pd.DataFrame(
        {'Keyword': kw_list,
        'Significance?': significant_list,
        'Increase?': increase_list
        })
    
  for kw in kw_list: 
    occurrences_list.append(globals()[kw + '_counter'])

  occurrences_df = pd.DataFrame(
      {'Keyword': kw_list,
      'Occurrecnes': occurrences_list,
      })
  
  for i in range(0, 50):
    globals()[kw + '_all_significance_level'][i] = (globals()[kw + '_all_significance_level'][i] - 1) * 100

  data_df = pd.DataFrame(
    {
      'State': full_states,
      '% Change': globals()[kw + '_all_significance_level'],
      'Direction': globals()[kw + '_all_increase_level']
    }
  )

  inc_list = globals()[kw + '_increase_states']
  dec_list = []
  
  for ele in state_list:
    if ele not in  globals()[kw + '_increase_states']:
      dec_list.append(ele)
  
  inc_list = convert(inc_list)
  dec_list = convert(dec_list)


  return data_df

def kw_plot(t, kw_list, location, youtube):
  plt.switch_backend('Agg')

  if youtube == False:
    pytrend.build_payload(kw_list, timeframe= t, geo = location)
  else:
    pytrend.build_payload(kw_list, timeframe= t, geo = location, gprop = youtube)


  df = pytrend.interest_over_time()
  sns.set(color_codes=True)
  dx = df.plot.line(figsize = (9,6), title = "Interest Over Time")
  dx.set_xlabel('Date')
  dx.set_ylabel('Trends Index')
  dx.tick_params(axis='both', which='major', labelsize=13)

  save_results_to = str(MapsHolder_dir) 
  plt.savefig(save_results_to + 'ComparisonPlot.png', dpi = 1000, tansparent = True)
