# def make_chocolate(small, big, goal):
# 	bigCount = 0
# 	bigValue = 0
# 	for i in range(0,big):
# 		bigCount +=1
# 		bigValue +=5
# 		if bigValue + small > goal : break
# 	rest = goal - bigCount * 5
# 	if rest < small : return small - (small - rest)
# 	if rest == small : return rest
# 	if rest > small : return -1

# def make_chocolate(small, big, goal):
# 	bigCount = 0
# 	bigValue = 0
# 	rest = goal - bigCount * 5
# 	if rest < small : return small - (small - rest)
# 	if rest == small : return rest
# 	if rest > small : return -1


# print make_chocolate(6, 1, 10)



# status_code = 200 
# day = "Monday"
# timeStamp = "time"

# print "Status code is wrong. Expected 200, but was %s . Day is %s, timestamp is %s. Assertion error - " %(status_code,day,timeStamp)



# a = [1,2,"3",4,"5"]
# l = []
# for item in a:    
#    l.append(int(item)*3+10)    
# print l

# orList = [5,3,9,7,1]


# def sort(orList):
# 	for i in range(len(orList)-1,0):
# 		for j in range(1,i+1):
# 			print j
# 			print orList[j-1]
# 			print orList[j]
# 			if orList[j-1]>orList[j]:
# 				temp = orList[j-1]
# 				orList[j-1]=orList[j]
# 				orList[j]=temp
# 			j+=1
# 		i-=1
# 	return orList

# print sort(orList)
# 

# sf = "US,CA,San Francisco,94128,37.6198,-122.3802\
# US,CA,San Francisco,94105,37.7898,-122.3942\
# US,CA,San Francisco,94131,37.7463,-122.4438\
# US,CA,San Francisco,94143,37.7631,-122.4586\
# US,CA,San Francisco,94127,37.7367,-122.4572\
# US,CA,San Francisco,94116,37.7441,-122.4839\
# US,CA,San Francisco,94132,37.723,-122.4842\
# US,CA,San Francisco,94122,37.7607,-122.4842\
# US,CA,San Francisco,94112,37.7217,-122.4444\
# US,CA,San Francisco,94121,37.7772,-122.4931\
# US,CA,San Francisco,94136,37.7848,-122.7278\
# US,CA,San Francisco,94168,37.7828,-122.4974\
# US,CA,San Francisco,94118,37.7811,-122.4625\
# US,CA,San Francisco,94117,37.7691,-122.4449\
# US,CA,San Francisco,94167,37.7691,-122.4429\
# US,CA,San Francisco,94110,37.7484,-122.4156\
# US,CA,San Francisco,94013,37.7645,-122.4294\
# US,CA,San Francisco,94114,37.7587,-122.4381\
# US,CA,San Francisco,94124,37.7312,-122.3826\
# US,CA,San Francisco,94134,37.7217,-122.4112\
# US,CA,San Francisco,94103,37.7758,-122.4128\
# US,CA,San Francisco,94115,37.7862,-122.4371\
# US,CA,San Francisco,94102,37.7794,-122.417\
# US,CA,San Francisco,94107,37.7697,-122.3933\
# US,CA,San Francisco,94133,37.8033,-122.4108\
# US,CA,San Francisco,94108,37.7915,-122.4089\
# US,CA,San Francisco,94129,37.799,-122.466\
# US,CA,San Francisco,94109,37.7957,-122.4209\
# US,CA,San Francisco,94123,37.8018,-122.4382\
# US,CA,San Francisco,94111,37.7989,-122.3984\
# US,CA,San Francisco,94104,37.7909,-122.4017\
# US,CA,San Francisco,94130,37.8198,-122.369"

# ny = "US,NY,New York,10002,40.7168,-73.9861\
# US,NY,New York,10242,40.7152,-74.0095\
# US,NY,New York,10280,40.7101,-74.0166\
# US,NY,New York,10006,40.7082,-74.0132\
# US,NY,New York,10004,40.6888,-74.0203\
# US,NY,New York,10271,40.7087,-74.0104\
# US,NY,New York,10041,40.7038,-74.0098\
# US,NY,New York,10048,40.7125,-74.0133\
# US,NY,New York,10285,40.7153,-74.0163\
# US,NY,New York,10281,40.7146,-74.015\
# US,NY,New York,10282,40.7165,-74.0131\
# US,NY,New York,10286,40.7142,-74.0119\
# US,NY,New York,10270,40.7069,-74.0082\
# US,NY,New York,10005,40.7055,-74.005\
# US,NY,New York,10007,40.7139,-74.0079\
# US,NY,New York,10279,40.7131,-74.0086\
# US,NY,New York,10045,40.7086,-74.0087\
# US,NY,New York,10278,40.7156,-74.0037\
# US,NY,New York,10038,40.7089,-74.0012\
# US,NY,New York,10012,40.7267,-73.9981\
# US,NY,New York,10014,40.733,-74.0078\
# US,NY,New York,10013,40.7214,-74.0052\
# US,NY,New York,10199,40.7503,-74.0006\
# US,NY,New York,10011,40.7421,-74.0018\
# US,NY,New York,10120,40.7506,-73.9894\
# US,NY,New York,10003,40.7317,-73.9885\
# US,NY,New York,10119,40.7505,-73.9931\
# US,NY,New York,10121,40.7496,-73.9919\
# US,NY,New York,10118,40.749,-73.9865\
# US,NY,New York,10098,40.7482,-73.9884\
# US,NY,New York,10018,40.7553,-73.9924\
# US,NY,New York,10036,40.7605,-73.9933\
# US,NY,New York,10001,40.7517,-73.9972\
# US,NY,New York,10122,40.7518,-73.9922\
# US,NY,New York,10123,40.7515,-73.9905\
# US,NY,New York,10175,40.7543,-73.9798\
# US,NY,New York,10168,40.7517,-73.9772\
# US,NY,New York,10178,40.7514,-73.9785\
# US,NY,New York,10010,40.7391,-73.9826\
# US,NY,New York,10009,40.7252,-73.9802\
# US,NY,New York,10158,40.7494,-73.9758\
# US,NY,New York,10016,40.7449,-73.9782\
# US,NY,New York,10170,40.7529,-73.9761\
# US,NY,New York,10110,40.754,-73.9808\
# US,NY,New York,10165,40.7524,-73.9789\
# US,NY,New York,10017,40.7528,-73.9725\
# US,NY,New York,10174,40.7517,-73.9752\\\
# US,NY,New York,10167,40.7549,-73.975\
# US,NY,New York,10111,40.7592,-73.9778\
# US,NY,New York,10169,40.7546,-73.9765\
# US,NY,New York,10176,40.7556,-73.9789\
# US,NY,New York,10173,40.7543,-73.9796\
# US,NY,New York,10020,40.7584,-73.9794\
# US,NY,New York,10177,40.7553,-73.9761\
# US,NY,New York,10166,40.7546,-73.9762\
# US,NY,New York,10105,40.7628,-73.9785\
# US,NY,New York,10104,40.7609,-73.9799\
# US,NY,New York,10112,40.7593,-73.9798\
# US,NY,New York,10075,40.7619,-73.9763\
# US,NY,New York,10103,40.7609,-73.9779\
# US,NY,New York,10155,40.7611,-73.968\
# US,NY,New York,10154,40.758,-73.9727\
# US,NY,New York,10171,40.7561,-73.974\
# US,NY,New York,10172,40.7555,-73.9745\
# US,NY,New York,10022,40.7588,-73.968\
# US,NY,New York,10152,40.7586,-73.9722\
# US,NY,New York,10151,40.7634,-73.974\
# US,NY,New York,10044,40.7625,-73.9503\
# US,NY,New York,10153,40.7637,-73.9727\
# US,NY,New York,10037,40.8132,-73.9386\
# US,NY,New York,10115,40.8109,-73.9638\
# US,NY,New York,10107,40.7664,-73.9827\
# US,NY,New York,10019,40.7662,-73.9862\
# US,NY,New York,10069,40.7759,-73.9902\
# US,NY,New York,10023,40.7769,-73.9813\
# US,NY,New York,10106,40.7652,-73.9804\
# US,NY,New York,10024,40.7958,-73.9775\
# US,NY,New York,10025,40.8006,-73.9653\
# US,NY,New York,10265,40.7808,-73.9772\
# US,NY,New York,10128,40.7805,-73.9512\
# US,NY,New York,10162,40.7694,-73.9503\
# US,NY,New York,10028,40.7762,-73.9548\
# US,NY,New York,10021,40.7694,-73.9609\
# US,NY,New York,10029,40.7921,-73.9439\
# US,NY,New York,10027,40.8116,-73.953\
# US,NY,New York,10026,40.8022,-73.9524\
# US,NY,New York,10035,40.791,-73.9256\
# US,NY,New York,10032,40.8399,-73.9422\
# US,NY,New York,10039,40.827,-73.9384\
# US,NY,New York,10031,40.8291,-73.9491\
# US,NY,New York,10030,40.8185,-73.943\
# US,NY,New York,10040,40.8596,-73.9314\
# US,NY,New York,10033,40.8504,-73.9369\
# US,NY,New York,10034,40.8626,-73.9218"

# def get_city_locations_dict(city,pattern):
# 	city_dict= city.split(pattern)
# 	city_locations = []
# 	for i in range(1,len(city_dict)):
# 		location =  "&lat=%s&lon=%s" %(city_dict[i].split(",")[1],city_dict[i].split(",")[2])
# 		city_locations.append(location)

# 	print city_locations
# 	print len(city_locations)

# get_city_locations_dict(ny,"US,NY,New York,")
# arr=[2,7,10,4,6,8,9,3,1,5]
# for j in range(0,len(arr)-1):
#     print ("j"+str(j))
#     i=0
#     for i in range(1,len(arr)-j):
#         print(arr[i],arr[i+1]);print("")
#         if arr[i]>arr[i+1]:
# 	        print("Yes")
# 	        temp=arr[i]
# 	        arr[i]=arr[i+1]
# 	        arr[i+1]=temp
# 	        print(arr)
# import random


# def task301_1(input_line):
# 	return input_line[::3]

# print task301_1('   c34o56o78l12!12!12!')

# def task301_2(input_line):
# 	return input_line.replace('home', 'family')

# print task301_2("this is my home")

# def task301_3(input_line):
# 	return input_line[-4:]

# print task301_3("your balance is 20.0")

# def task301_4(input_line):
# 	count = 0
# 	for i in range(len(input_line)-1):
# 		if input_line[i:i+4] == 'code' : count+=1
# 	return count

# print task301_4("codexxcode")

# def task302_1(a,b):
# 	return a % b


# def task302_2(a,b):
# 	return ((a+b)*0.2)**3

# print task302_2(100,133)

# def task302_3():
# 	return round(random.random(),2)
# print task302_3()



# def generate_array():
# 	result = []
# 	result_len = random.randint(5,10)
# 	for i in range(result_len):
# 		inner_array = []
# 		inner_array_len = random.randint(5,10)
# 		for j in range(inner_array_len):
# 			inner_array.append(random.randint(0,10))
# 		result.append(inner_array)
# 		print 'Array is ' + str(result)
# 	return result

# def sum_of_two_last_elements_of_first_inner_array(array):
# 	last_element = array[0][-1:][0]
# 	before_last_element = array[0][-2:-1][0]
# 	print "Sum is "+str(sum)
# 	return last_element + before_last_element

# print sum_of_two_last_elements_of_first_inner_array(generate_array())

# def get_minimal_value_from_second_array(array):
# 	array_of_max_values = []
# 	for i in range(len(array)-1):
# 		array_of_max_values.append(max(array[i]))
# 	print "max value is " + str(max(array_of_max_values))
#  	return max(array_of_max_values)

# def get_array_index_where_4_is_present(array):
# 	indexes_array = []
# 	for el in array: 
# 		if el.__contains__(4):
# 			indexes_array.append(array.index(el))
# 	print "Here are the indexes of the arrays that contain number 4" + str(indexes_array)
# 	return indexes_array


# print get_array_index_where_4_is_present(generate_array())


# array = [1 , 3, 6, 4, 2, 8, 9, 7]

# def merge_sort(array):
# 	if len(array)<=1 : 
# 		return array
# 	middle = len(array) / 2
# 	left = merge_sort(array[:middle])
# 	right = merge_sort(array[middle:])
# 	return merger(left,right)

# def merger(left, right):
# 	result = []
# 	while len(left) > 0 and len(right) > 0:
# 		if left[0] <= right[0]:
# 			result.append(left[0])
# 			left = left[1:]
# 		else : 
# 			result.append(right[0])
# 			right = right[1:]
# 	if len(left) > 0 : 
# 		result+=left
# 	if len(right) > 0 : 
# 		result+=right
# 	return result

# print merge_sort(array)		

# import json
# # f = open("/Users/biercoff/Work/IdeaWorkspace/Pure/src/main/resources/want.json")
# # data = json.load(f)
# # want = data.get("want")
# # result = []
# # for el in want: 
# # 	if el.get("fields").get("orientation") == "gay":
# # 		result.append(el.get("pk"))

# # print result
# import MySQLdb


# class MySqlDB(object):

#     def __init__(self, host, user, password, database):

#         # connecting to MySQL DB
#         self.db = MySQLdb.connect(host=host, user=user, passwd=password, db=database)
#         self.cursor = self.db.cursor()

#     def execute(self, query):

#         #executing mysql query and commiting execution
#         self.cursor.execute(query)
#         self.db.commit()

#     def return_query_result(self, query):
#         c = self.cursor
#         c.execute(query)
#         result = c.fetchall()
#         return result

#     def close(self):
        
#         #closing db connection
#         self.cursor.close()
#         self.db.close()

# host = 'bmw.velti.kyiv.cogniance.com'
# db_port = "3306"
# base = "bb_console"
# db_user = "root"
# db_pass = "ep3z3ena"

# mysqlIstance = MySqlDB(host=host, user=db_user, password=db_pass, database=base)
# original_value = mysqlIstance.return_query_result("select parent_category_id, category_name, tier, removed from m_iab_category_original;")
# new_value = mysqlIstance.return_query_result("select parent_category_id, category_name, tier, removed from m_iab_category;")
# mysqlIstance.close()
# print "Original value length is " + str(len(original_value))
# print "New value len is "+ str(len(new_value))
# together = zip(original_value,new_value)
# for item in together : 
#     if item[0] != item[1]:
#         print " We have difference"
#         print "original values is %s and new values is %s" %(item[0],item[1])


list = [['/Users/biercoff/Work', 'folder exist'], ['/Users/biercoff/Dropbox/', 'folder exist'], ['/Users/biercoff/Google', "folder doesn't exist"]]

for i, item in enumerate(list, start=0):
    print i 
    print item[0]
    print item [1]



