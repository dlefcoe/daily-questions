'''
MongoDB Atlas

Connect to Atlas
Connect to ClusterDL01


'''




def mainRoutine():
    ''' this is the main routine '''

    url = connectToDB('darren.11')
    print(u)


def connectToDB(p):
    ''' connect to database given string p '''
    print('connecting to database')
    url = 'mongodb+srv://dlefcoe:<' + p + '>@clusterdl01-qyqzc.mongodb.net/test?retryWrites=true&w=majority'
    # print(url)
    return url



if __name__ == "__main__":
    # run the main routine
    mainRoutine()

