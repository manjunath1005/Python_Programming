def normalize(s1,s2,s3):
    for i in s1:
        if i.isupper():
            s1.remove(i)
            s1.add(i.lower())
    for i in s2:
        if i.isupper():
            s2.remove(i)
            s2.add(i.lower())
    for i in s3:
        if i.isupper():
            s3.remove(i)
            s3.add(i.lower())
    return s1,s2,s3

def unique(s1,s2,s3):
    s=s1.union(s2).union(s3)
    print("Unique Students in all three days:",s)
    print("Total Unique Students in all three days:",len(s))

def common(s1,s2,s3):
    s=s1.intersection(s2).intersection(s3)
    print("Common Students in all three days:",s)
    print("Total Common Students in all three days:",len(s))

def attended_one_day(s1,s2,s3):
    s=s1.symmetric_difference(s2).symmetric_difference(s3)
    print("Students attended only one day:",s)
    print("Total Students attended only one day:",len(s))

def pairwise_overlap(s1,s2,s3):
    s12=s1.intersection(s2)
    s23=s2.intersection(s3)
    s31=s3.intersection(s1)
    print("Students attended day1 and day2:",s12)
    print("Total Students attended day1 and day2:",len(s12))
    print("Students attended day2 and day3:",s23)
    print("Total Students attended day2 and day3:",len(s23))
    print("Students attended day3 and day1:",s31)
    print("Total Students attended day3 and day1:",len(s31))

day1=set(input("Enter the emails of attendees on day 1:").split())
day2=set(input("Enter the emails of attendees on day 2:").split())
day3=set(input("Enter the emails of attendees on day 3:").split())
day1,day2,day3=normalize(day1,day2,day3)
unique(day1,day2,day3)
common(day1,day2,day3)
attended_one_day(day1,day2,day3)
pairwise_overlap(day1,day2,day3)
