print('ax + bx = gcd(a,b)')

a = int(input('a='))
b = int(input('b='))
a_o = a  #  aの初期値保管用
b_o = b  #  bの初期値保管用
swap_flag = 0

if( b > a ):
    tmp = a
    a = b
    b = tmp
    swap_flag = 1

print('')

r = 1  #  次のループを動かすためのとりあえず代入
i = 0  #  式の番号
qlist = []

while( r != 0 ):
    q = a // b
    r = a % b
    
    print('({0}) {1} = {2} * {3} + {4}'.format(i, a, q, b, r))
    qlist.append(q)
    a = b
    b = r
    i += 1
gcd = a

print('GCD=',gcd,'\n')

n = i - 2
x1 = qlist[n]
x2 = x1
x3 = 1

for j in range(n, 0, -1):  #  ユークリッドの互除法を遡る
    x1 = x1 * qlist[j-1] + x3
    tmp = x2
    x2 = x1
    x3 = tmp

a = a_o // gcd
b = b_o // gcd

x = x3
y = x1

if( i % 2 == 1):  #  式の最後の番号(式の数-1)が奇数ならx,偶数ならyをマイナスにする
    x = -x
else:
    y = -y

print('{0}x + {1}y = {2}\n'.format(a_o, b_o, gcd))

if( swap_flag == 0):  #  a,bを入れ替えたかどうかの場合分け
    print('x0 = {0}, y0 = {1}'.format(x, y))
    print('x = {0} + {1}t, y = {2} - {3}t\n'.format(x, b, y, a))
else:
    print('x0 = {0}, y0 = {1}'.format(y, x))
    print('x = {0} - {1}t, y = {2} + {3}t\n'.format(y, b, x, a))