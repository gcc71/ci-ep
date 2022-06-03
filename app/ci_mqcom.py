import pika, sys, os

def transmit(mq,msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    #create the queue
    channel.queue_declare(queue=mq)
    #send through default exchange via empty string
    channel.basic_publish(exchange='',
                      routing_key=mq,
                      body=msg)
    print("Message " + msg + " sent to queue " + mq)
    #close
    connection.close()

def recieve(mq):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue=mq)

    def callback(ch, method, properties, body):
        print("got message from " + mq + ":", body.decode())
        #do work here

    channel.basic_consume(queue=mq, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages on hello. press ctl-c to exit')
    channel.start_consuming()
