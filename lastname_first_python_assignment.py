data_str = { 'Python': { "2015": 9,
                                "2016": 22,
                                "2017": 27,
                                "2018": 32,
                               " 2019": 35},
                                  
                     'JavaScript': {"2015": 8,
                               "2016": 18,
                               "2017": 12,
                               "2018": 6,
                               "2019": 15}, 
                               
                               'Twitter': {"2015": 10,
                               "2016": 18,
                               "2017": 26,
                               "2018": 16,
                               "2019": 12}, 
                                'Github': {"2015": 2, "2016": 6, "2017": 17, "2018" : 5, "2019": 10},
                                'Gephi': {"2015": 11, "2016": 16, "2017": 14, "2018" : 10, "2019": 9},
                                'GeoNames': {"2015": 2, "2016": 4, "2017": 3, "2018" : 1, "2019": 8},
                                'Transkribus': {"2015": 0, "2016": 1, "2017": 2, "2018" : 1, "2019": 8},
                                 'Excel' : {"2015": 5, "2016": 9, "2017": 3, "2018" : 6, "2019": 7},
                                 'MySQL': {"2015": 0, "2016": 6, "2017": 9, "2018" : 5, "2019": 7}

                               }
                                 
sum2015 = 0
sum2019= 0
  

for key ,value in data_str.items():
  
    if value and "2015" in value.keys():
        
        sum2015 += value["2015"] 
  

print( "2015" + "Total Count" , sum2015)

for key ,value in data_str.items():
  
    if value and "2019" in value.keys():
        
        sum2019 += value["2019"] 
print ("2019 Total Count", sum2019)

print 

for key, value in data_str.items():
    print(key, sum(value.values()))
