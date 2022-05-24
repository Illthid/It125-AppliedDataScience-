import pandas as pd
import numpy as np
import scipy.stats as st
import math

# Quick applogy, I dont know anything about NBA so this could feel ackward

nba_players_hist = pd.read_csv('historical_RAPTOR_by_player.csv', usecols=['player_name', 'season', 'pace_impact'])
df_1977 = nba_players_hist.loc[nba_players_hist['season'] == 1977 ]
df_1977 = df_1977[df_1977.pace_impact == df_1977.pace_impact.max()]
df_1978 = nba_players_hist.loc[nba_players_hist['season'] == 1978 ]
df_1978 = df_1978[df_1978.pace_impact == df_1978.pace_impact.max()]
df_1979 = nba_players_hist.loc[nba_players_hist['season'] == 1979 ]
df_1979 = df_1979[df_1979.pace_impact == df_1979.pace_impact.max()]
df_1980 = nba_players_hist.loc[nba_players_hist['season'] == 1980 ]
df_1980 = df_1980[df_1980.pace_impact == df_1980.pace_impact.max()]
df_1981 = nba_players_hist.loc[nba_players_hist['season'] == 1981 ]
df_1981 = df_1981[df_1981.pace_impact == df_1981.pace_impact.max()]
df_1982 = nba_players_hist.loc[nba_players_hist['season'] == 1982 ]
df_1982 = df_1982[df_1982.pace_impact == df_1982.pace_impact.max()]
df_1983 = nba_players_hist.loc[nba_players_hist['season'] == 1983 ]
df_1983 = df_1983[df_1983.pace_impact == df_1983.pace_impact.max()]
df_1984 = nba_players_hist.loc[nba_players_hist['season'] == 1984 ]
df_1984 = df_1984[df_1984.pace_impact == df_1984.pace_impact.max()]
df_1985 = nba_players_hist.loc[nba_players_hist['season'] == 1985 ]
df_1985 = df_1985[df_1985.pace_impact == df_1985.pace_impact.max()]
df_1986 = nba_players_hist.loc[nba_players_hist['season'] == 1986 ]
df_1986 = df_1986[df_1986.pace_impact == df_1986.pace_impact.max()]
df_1987 = nba_players_hist.loc[nba_players_hist['season'] == 1987 ]
df_1987 = df_1987[df_1987.pace_impact == df_1987.pace_impact.max()]
df_1988 = nba_players_hist.loc[nba_players_hist['season'] == 1988 ]
df_1988 = df_1988[df_1988.pace_impact == df_1988.pace_impact.max()]
df_1989 = nba_players_hist.loc[nba_players_hist['season'] == 1989 ]
df_1989 = df_1989[df_1989.pace_impact == df_1989.pace_impact.max()]
df_1990 = nba_players_hist.loc[nba_players_hist['season'] == 1990 ]
df_1990 = df_1990[df_1990.pace_impact == df_1990.pace_impact.max()]
df_1991 = nba_players_hist.loc[nba_players_hist['season'] == 1991 ]
df_1991 = df_1991[df_1991.pace_impact == df_1991.pace_impact.max()]
df_1992 = nba_players_hist.loc[nba_players_hist['season'] == 1992 ]
df_1992 = df_1992[df_1992.pace_impact == df_1992.pace_impact.max()]
df_1993 = nba_players_hist.loc[nba_players_hist['season'] == 1993 ]
df_1993 = df_1993[df_1993.pace_impact == df_1993.pace_impact.max()]
df_1994 = nba_players_hist.loc[nba_players_hist['season'] == 1994 ]
df_1994 = df_1994[df_1994.pace_impact == df_1994.pace_impact.max()]
df_1995 = nba_players_hist.loc[nba_players_hist['season'] == 1995 ]
df_1995 = df_1995[df_1995.pace_impact == df_1995.pace_impact.max()]
df_1996 = nba_players_hist.loc[nba_players_hist['season'] == 1996 ]
df_1996 = df_1996[df_1996.pace_impact == df_1996.pace_impact.max()]
df_1997 = nba_players_hist.loc[nba_players_hist['season'] == 1997 ]
df_1997 = df_1997[df_1997.pace_impact == df_1997.pace_impact.max()]
df_1998 = nba_players_hist.loc[nba_players_hist['season'] == 1998 ]
df_1998 = df_1998[df_1998.pace_impact == df_1998.pace_impact.max()]
df_1999 = nba_players_hist.loc[nba_players_hist['season'] == 1999 ]
df_1999 = df_1999[df_1999.pace_impact == df_1999.pace_impact.max()]
df_2000 = nba_players_hist.loc[nba_players_hist['season'] == 2000 ]
df_2000 = df_2000[df_2000.pace_impact == df_2000.pace_impact.max()]
df_2001 = nba_players_hist.loc[nba_players_hist['season'] == 2001 ]
df_2001 = df_2001[df_2001.pace_impact == df_2001.pace_impact.max()]
df_2001 = nba_players_hist.loc[nba_players_hist['season'] == 2001 ]
df_2001 = df_2001[df_2001.pace_impact == df_2001.pace_impact.max()]
df_2002 = nba_players_hist.loc[nba_players_hist['season'] == 2002 ]
df_2002 = df_2002[df_2002.pace_impact == df_2002.pace_impact.max()]
df_2003 = nba_players_hist.loc[nba_players_hist['season'] == 2003 ]
df_2003 = df_2003[df_2003.pace_impact == df_2003.pace_impact.max()]
df_2004 = nba_players_hist.loc[nba_players_hist['season'] == 2004 ]
df_2004 = df_2004[df_2004.pace_impact == df_2004.pace_impact.max()]
df_2005 = nba_players_hist.loc[nba_players_hist['season'] == 2005 ]
df_2005 = df_2005[df_2005.pace_impact == df_2005.pace_impact.max()]
df_2006 = nba_players_hist.loc[nba_players_hist['season'] == 2006 ]
df_2006 = df_2006[df_2006.pace_impact == df_2006.pace_impact.max()]
df_2007 = nba_players_hist.loc[nba_players_hist['season'] == 2007 ]
df_2007 = df_2007[df_2007.pace_impact == df_2007.pace_impact.max()]
df_2008 = nba_players_hist.loc[nba_players_hist['season'] == 2008 ]
df_2008 = df_2008[df_2008.pace_impact == df_2008.pace_impact.max()]
df_2009 = nba_players_hist.loc[nba_players_hist['season'] == 2009 ]
df_2009 = df_2009[df_2009.pace_impact == df_2009.pace_impact.max()]
df_2010 = nba_players_hist.loc[nba_players_hist['season'] == 2010 ]
df_2010 = df_2010[df_2010.pace_impact == df_2010.pace_impact.max()]
df_2011 = nba_players_hist.loc[nba_players_hist['season'] == 2011 ]
df_2011 = df_2011[df_2011.pace_impact == df_2011.pace_impact.max()]
df_2012 = nba_players_hist.loc[nba_players_hist['season'] == 2012 ]
df_2012 = df_2012[df_2012.pace_impact == df_2012.pace_impact.max()]
df_2013 = nba_players_hist.loc[nba_players_hist['season'] == 2013 ]
df_2013 = df_2013[df_2013.pace_impact == df_2013.pace_impact.max()]
df_2014 = nba_players_hist.loc[nba_players_hist['season'] == 2014 ]
df_2014 = df_2014[df_2014.pace_impact == df_2014.pace_impact.max()]
df_2015 = nba_players_hist.loc[nba_players_hist['season'] == 2015 ]
df_2015 = df_2015[df_2015.pace_impact == df_2015.pace_impact.max()]
df_2016 = nba_players_hist.loc[nba_players_hist['season'] == 2016 ]
df_2016 = df_2016[df_2016.pace_impact == df_2016.pace_impact.max()]
df_2016 = nba_players_hist.loc[nba_players_hist['season'] == 2016 ]
df_2016 = df_2016[df_2016.pace_impact == df_2016.pace_impact.max()]
df_2017 = nba_players_hist.loc[nba_players_hist['season'] == 2017 ]
df_2017 = df_2017[df_2017.pace_impact == df_2017.pace_impact.max()]
df_2018 = nba_players_hist.loc[nba_players_hist['season'] == 2018 ]
df_2018 = df_2018[df_2018.pace_impact == df_2018.pace_impact.max()]
df_2019 = nba_players_hist.loc[nba_players_hist['season'] == 2019 ]
df_2019 = df_2019[df_2019.pace_impact == df_2019.pace_impact.max()]
df_2020 = nba_players_hist.loc[nba_players_hist['season'] == 2020 ]
df_2020 = df_2020[df_2020.pace_impact == df_2020.pace_impact.max()]
df_2021 = nba_players_hist.loc[nba_players_hist['season'] == 2021 ]
df_2021 = df_2021[df_2021.pace_impact == df_2021.pace_impact.max()]
# print("The NBA player with highest impact on possessions per 48 minutes, from 1977 to 2021\n" , df_1977[df_1977.pace_impact == df_1977.pace_impact.max()])

master_table= pd.concat([df_1977 , df_1978 , df_1979 , df_1980 , df_1981 , df_1982 , df_1983 , df_1984 , df_1985 , df_1986 , df_1987 , df_1988 , df_1989 , df_1990 , df_1991 , df_1992 , df_1993 , df_1994 , df_1995 , df_1996 , df_1997 , df_1998 , df_1999 , df_2000 , df_2001 , df_2002 , df_2003 , df_2004 , df_2005 , df_2006 , df_2007 , df_2008 , df_2009 , df_2010 , df_2011 , df_2012 , df_2013 , df_2013 , df_2014 , df_2015 , df_2016 , df_2017 , df_2018 , df_2019 , df_2020 , df_2021])
print("These are the NBA players with highest impact on possessions per 48 minutes,\n from seasons 1977 to 2021\n", master_table)
print("This is the NBA player with highest impact on possessions per 48 minutes,\n from seasons 1977 to 2021\n", master_table[master_table.pace_impact == master_table.pace_impact.max()])
sample_mean=master_table.pace_impact.mean(axis='index')
print("This is the mean of all years highest impacts\n", sample_mean)

std_dev = master_table.pace_impact.std()
print("sample std deviation",std_dev)
stderr = std_dev/math.sqrt(46)
print("sample std error", stderr)
int1 = st.norm.interval(0.95, sample_mean, stderr)
print(int1)
pop_mean= nba_players_hist.pace_impact.mean(axis='index')
print("This is the Population mean of all the players impact", pop_mean)

if int1[0] <= pop_mean <= int1[1]:
  print("the mean,",pop_mean, ", is within 95% confidence interval")
else:
  print("the mean," ,pop_mean," is not within the 95% confidence interval")

n=46

t = (sample_mean - pop_mean)/(std_dev/math.sqrt(46))
prob = st.t.sf(t,(n-1))
print("This is the probablity" + str(prob) + "." )
