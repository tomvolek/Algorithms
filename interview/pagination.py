'''
Airbnb Online Assessment Paginate List 

5 
13 
1,28,310.6,SF 
4,5,204.1,SF 
20,7,203.2,Oakland 
6,8,202.2,SF 
6,10,199.1,SF 
1,16,190.4,SF 
6,29,185.2,SF 
7,20,180.1,SF 
6,21,162.1,SF 
2,18,161.2,SF 
2,30,149.1,SF 
3,76,146.2,SF 
2,14,141.1,San Jose 


Here is a sample input. It’s a list generated by user search. 
(1,28,100.3,Paris) corresponds to (Host ID, List ID, Points, City). 

5 in the first row tells each page at most keeps 5 records. 
13 in the second row is the number of records in the list. 

Please paginate the list for Airbnb by requirement: 
1. When possible, two records with same host ID shouldn’t be in a page. 
2. But if no more records with non-repetitive host ID can be found, fill up the page with the given input order (ordered by Points). 

Expected output: 
1,28,310.6,SF 
4,5,204.1,SF 
20,7,203.2,Oakland 
6,8,202.2,SF 
7,20,180.1,SF 

6,10,199.1,SF 
1,16,190.4,SF 
2,18,161.2,SF 
3,76,146.2,SF 
6,29,185.2,SF -- 6 repeats in page bec no more unique host ID available 

6,21,162.1,SF 
2,30,149.1,SF 
2,14,141.1,San Jose

'''

#  (Host ID, List ID, Points, City). 
results = [5,
    13,
    [1,28,310.6,'SF'],
    [4,5,204.1,'SF' ],
    [20,7,203.2,'Oakland' ],
    [6,8,202.2,'SF' ],
    [6,10,199.1,'SF' ],
    [1,16,190.4,'SF' ],
    [6,29,185.2,'SF' ],
    [7,20,180.1,'SF' ],
    [6,21,162.1,'SF' ],
    [2,18,161.2,'SF' ],
    [2,30,149.1,'SF' ],
    [3,76,146.2,'SF' ],
    [2,14,141.1,'San Jose']
]

record_per_page = results[0]
num_records_in_list = results[1]
pages= []   # array containing records for pages in order of requirment. 
for i  in range(0, num_records_in_list):
     print  (results[i+2][0])





