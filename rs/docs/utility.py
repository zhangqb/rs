# -*- coding: utf-8 -*-
#accept a line of news and return the time in the form of a tuple
def split_data_by_date(line):
		temp = line.strip().split()
		temp = temp[-1]
                print 'temp: ',temp
#                temp = '2014年03月08日12:31'
		year, temp = temp.split('年')
		month, temp = temp.split('月')
		temp = temp.split('日')
		if len(temp) > 1:
			day = temp[0]
			hour,min = temp[1].split(':')
			time = (hour,min)
		else:
			day = temp[0]
			time = 'no'
	        return	(int(year),int(month),int(day),time)