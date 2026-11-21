import random
import matplotlib.pyplot as plt
random.seed(44)

slots=500000
posibility=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
delays=[]
throughputs=[]
lossRate=[]

for p in posibility:
    queues = [[] for _ in range(8)]
    totalTime = 0
    packetsSent = 0
    packetsLost = 0
    totalArrivals = 0
    for slot in range(slots):
        for w in range(4):
            pc1=2*w
            pc2=2*w+1
            for pc in (pc1,pc2):
                if random.random()<p:
                    totalArrivals += 1
                    if len(queues[pc])<5:
                        queues[pc].append(slot)
                    else:
                        packetsLost+=1
            if len(queues[pc1])>0 and random.random()<0.5:
                if not (len(queues[pc2])>0 and random.random()<0.5):
                    arrive=queues[pc1].pop(0)
                    totalTime+=slot-arrive+1
                    packetsSent+=1
            else:
                if len(queues[pc2])>0 and random.random()<0.5:
                    arrive=queues[pc2].pop(0)
                    totalTime+=slot-arrive+1
                    packetsSent+=1

    if packetsSent > 0:
        avgDelay=totalTime/packetsSent
    else:
        avgDelay=0

    throughput=packetsSent/slots

    if totalArrivals>0:
        loss=packetsLost/totalArrivals
    else:
        loss=0

    delays.append(avgDelay)
    throughputs.append(throughput)
    lossRate.append(loss)

    print(f"p={p:.1f} | Average Delay={avgDelay:.2f} | Throughput={throughput:.3f} | Packet Loss Rate={loss:.4f}")


plt.figure()
plt.plot(posibility, delays, marker='o')
plt.title("Average Delay")
plt.xlabel("p")
plt.ylabel("Delay in slots")
plt.xticks(posibility)
plt.grid(True)


plt.figure()
plt.plot(posibility, throughputs, marker='o')
plt.title("Throughput")
plt.xlabel("p")
plt.ylabel("Throughput")
plt.xticks(posibility)
plt.grid(True)

plt.figure()
plt.plot(posibility, lossRate, marker='o')
plt.title("Packet Loss Rate")
plt.xlabel("p")
plt.ylabel("Packet Loss Rate")
plt.xticks(posibility)
plt.grid(True)

plt.show()