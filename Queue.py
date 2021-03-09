import time

import random





DURATION = 15

MAXSIZE = 200



class Queue:

    queue = []



    def __init__(self):

        self.length = 0



    def isFull(self):

        return self.length == MAXSIZE



    def size(self):

        return self.length



    def isEmpty(self):

        return self.length == 0



    def enqueue(self, item):

        if not self.isFull():

            self.queue.append(item)

            self.length += 1



    def dequeue(self):

        if not self.isEmpty():

            item = self.queue.pop(0)

            self.length -= 1

            return item





numberOfArrivedPerMinute = []

numberOfSentPerMinute = []

numberInQueuePerMinute = []

numberOfRequeuePerMinute = []





def printStatistics(totalProcessed):

    print("\nTotal number of messages processed:\t\t\t\t\t %d" %totalProcessed)

    totalNumberArrived = 0

    for i in numberOfArrivedPerMinute:

        totalNumberArrived += i



    averageNumberArrived = totalNumberArrived / DURATION



    print("Average arrival rate : \t\t\t\t\t\t\t %.2f" %averageNumberArrived)



    totalNumberOfSent = 0

    for i in numberOfSentPerMinute:

        totalNumberOfSent += i



    averageNumberOfSent = totalNumberOfSent / DURATION

    print("Average number of messages sent per minute : \t\t\t\t %.2f" % averageNumberOfSent)





    totalNumberInQueue = 0

    for i in numberInQueuePerMinute:

        totalNumberInQueue += i



    averageNumberInQueue = totalNumberInQueue / DURATION

    print("Average number of messages in quuee per minute : \t\t\t %.2f" % averageNumberInQueue)





    idx = 0

    for i in numberOfSentPerMinute:

        idx += 1

        print("Number of messages sent on attempt : %d, \t\t : %d" %(idx, i))



    totalNumberOfRequeue = 0

    for i in numberOfRequeuePerMinute:

        totalNumberOfRequeue += i

    averageNumberOfRequeue = totalNumberOfRequeue / DURATION

    print("Average number of messages had to be requeued : \t\t\t %.2f" % averageNumberOfRequeue)



def main():

    q = Queue()

    totalProcessed = 0

    minutesElapsed = 0

    while(minutesElapsed < DURATION):

        numberArriving = random.randint(1,60)

        numberOfArrivedPerMinute.append(numberArriving)



        #enqueue arriving mail

        for i in range(numberArriving):

            q.enqueue(i)



        #simulate processing emails

        numberofProcessing = random.randint(1,30)

        minimumFails = numberofProcessing % 4

        totalProcessed += numberofProcessing



        numberOfRequeue = 0

        #25% of mails cannot be sent

        for i in range(minimumFails):

            temp = q.dequeue()

            q.enqueue(temp)

            numberOfRequeue += 1

        numberOfRequeuePerMinute.append(numberOfRequeue)



        #the rest of processess

        numberOfSent = 0

        numberOfRequeue = 0

        for i in range(numberofProcessing - minimumFails):

            if random.randint(1,1000) > 25:

                item = q.dequeue()

                numberOfSent += 1

            else:

                temp = q.dequeue()

                q.enqueue(temp)

                numberOfRequeue += 1



            numberOfSentPerMinute.append(numberOfSent)

            numberOfRequeuePerMinute.append(numberOfRequeue)



        numberInQueuePerMinute.append(q.size())



        time.sleep(60)

        minutesElapsed += 1

        print("%d minute(s) elapsed" % minutesElapsed)





    printStatistics(totalProcessed)



if __name__ == "__main__":

    main()