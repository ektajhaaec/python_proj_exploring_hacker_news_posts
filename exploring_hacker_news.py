import csv
import datetime as dt


data = open("data/hacker_news.csv","r") 
hn = list(csv.reader(data))
#print(hn[:5]) 
headers =hn [0]
#print(headers)
hn = hn[1:]
#print(hn[:5])

ask_posts =[]
show_posts =[]
other_posts =[]

for row in hn:
    title = row[1]
    if title.lower().startswith("ask hn"):
        ask_posts.append(row)
    elif title.lower().startswith("show hn"):
        show_posts.append(row)
    else:
        other_posts.append(row)

# print(ask_posts)
# print(len(ask_posts))
# print(len(show_posts))
# print(len(other_posts))

total_ask_comments =0
for row in ask_posts:
   # print(row[4])
    total_ask_comments += int(row[4])
#print(total_ask_comments)

avg_ask_comments =total_ask_comments/len(ask_posts)
#print(avg_ask_comments)
total_show_comments= 0
for row in show_posts:
    total_show_comments += int(row[4])

avg_show_comments =total_show_comments/len(show_posts)

# print(avg_ask_comments)
# print(avg_show_comments)

result_list =[]
for row in ask_posts:
    created_at = row[6]
    num_comments = int(row[4])
    result_list.append([created_at, num_comments])

#print(result_list)

counts_by_hour ={}
comments_by_hour ={}
for row in result_list :
    date = dt.datetime.strptime(row[0],"%m/%d/%Y %H:%M")
    hour = date.strftime("%H")
    comments =row[1]

    if hour not in counts_by_hour :
        counts_by_hour[hour] =1
        #print(counts_by_hour)
        comments_by_hour[hour] =comments
        #print(comments_by_hour)
    else:
        counts_by_hour[hour] += 1
        #print(counts_by_hour)
        comments_by_hour[hour] += comments

# print(counts_by_hour)
# print(comments_by_hour)

avg_by_hour = []
for hour in comments_by_hour :
    avg_by_hour.append([hour,int(comments_by_hour[hour])/int(counts_by_hour[hour])])
swap_avg_by_hour =[]
for row in avg_by_hour:
    avg_comment =(row[1])
    swap_avg_by_hour.append([avg_comment,row[0]])
   # print(swap_avg_by_hour)


print(sorted(swap_avg_by_hour, reverse =True))





