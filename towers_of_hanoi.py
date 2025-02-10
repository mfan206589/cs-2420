def main():
    N =4 
    move(N, 1, 2, 3)
def move(N,fro, to, other):
    if N == 1:
        print('move 1 from', fro, 'to', to)
    else:
        move(N-1, fro, other, to)
        move(1, fro, to, other)
        move(N-1, other, to, fro)
main()