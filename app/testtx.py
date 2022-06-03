import ci_mqcom as tx
def main():
    mq = 'wfetx'
    msg = ""
    while msg != "exit":
        msg = input(">> ")
        if msg != "exit":
            tx.transmit(mq,msg)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
