# We're going to implement a simple CSV parsing function.
# There are two things to focus on. The first (and most importantly)
# is correctly parsing the CSV format. The second is writing
# clean code that another engineer would enjoy using.
#
# You may assume that the CSV file is correctly formatted.
#
# An ideal parse will look like this:
# [['John', 'Smith', 'john.smith@gmail.com', 'Los Angeles', '1'],
#  ['Jane', 'Roberts', 'janer@msn.com', 'San Francisco, CA', '0'],
#  ['Alexandra "Alex"', 'Menendez', 'alex.menendez@gmail.com', 'Miami', '1'],
#  ['1','2','','4','5']]


csv_lines = [
  'John,Smith,john.smith@gmail.com,Los Angeles,10',
  'Jane,Roberts,janer@msn.com,"San Francisco, CA",0',
  '"Alexandra ""Alex""",Menendez,alex.menendez@gmail.com,Miami,1', 
  '1,2,,4,"5"'
]

# our new parsed output array 
outputline = []
double_quote_flag=0

for line in csv_lines:
    token = ''
    for x in line:  
        if (x == '"' ): 
            if double_quote_flag == 1:
               outputline.append(token)
               double_quote_flag = 0 
               token = ''  # null the token  
            else: 
                double_quote_flag = 1  # x is initial doubel quote
        else: 
            if double_quote_flag == 1: 
                token += x
            elif (x ==',' ): 
                outputline.append(token) 
                token = ''  # null the token 
            else:
                    token += x 
                    
    outputline.append(token)  # to add last token parsed into outline list  
    print(outputline)
    outputline= []