import time
from itertools import count
from multiprocessing import Process

def generate_input():
    fuzzer = grafuzz.GramFuzzer()
    fuzzer.load_grammar("./bc_grammar.py")
    bc_inputs = fuzzer.gen(cat="bc_input", num=1)
    with open('input', 'w') as f:
        for bc_input in bc_inputs:
            f.write(bc_input.decode('utf-8' + '\n')
        #f.write('quit')


def bc():
    print('Starting fuzzing bc...')

    while True:
        # time.sleep(1)
        # print(next(counter))

        filename = 'bc.csv'

        try:
            # feed grammfuzz's output to bc 
            print('feed grammfuzz output to bc ')
        except:
            # print('bc fuzzing error is found.')
            with open(filename, 'w') as file_object:
                file_object.write('Input\t')
                file_object.write('Error found\n')
            file_object.close()
        else:
            # write bc running results to a .csv file
            with open(filename, 'a') as file_object:
                file_object.write('Input\t')  # replace Input
                file_object.write('Output\n')  # replace Output
            file_object.close()


def calc():
    print('Starting fuzzing calc...')

    while True:
        # time.sleep(1)
        # print(next(counter))

        filename = 'calc.csv'

        try:
            # feed grammfuzz's output to calc
            print('feed grammfuzz output to calc')
        except:
            # print('bc fuzzing error is found.')
            with open(filename, 'w') as file_object:
                file_object.write('Input\t')
                file_object.write('Error found\n')
            file_object.close()
        else:
            # write bc running results to a .csv file
            with open(filename, 'a') as file_object:
                file_object.write('Input\t')  # replace Input
                file_object.write('Output\n')  # replace Output
            file_object.close()




if __name__ == '__main__':
    # counter is an infinite iterator
    counter = count(0)  # count starting from 0

    p1 = Process(target=bc, name='Process:(bc)')
    p2 = Process(target=calc, name='Process:(calc)')
    p1.start()
    p2.start()
    p1.join(timeout=1)
    p2.join(timeout=1)
    p1.terminate()
    p2.terminate()

if p1.exitcode is None:
    print(f'Oops, {p1} timeouts!')

if p2.exitcode is None:
    print(f'Oops, {p2} timeouts!')


