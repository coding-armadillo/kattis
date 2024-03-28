table = """
qwerty	dvorak	bjarki
~	~	0
1	1	2
2	2	4
3	3	8
4	4	6
5	5	1
6	6	3
7	7	5
8	8	7
9	9	9
0	0	=
-	[	-
=	]	/
q	'	b
w	,	j
e	.	a
r	p	r
t	y	k
y	f	i
u	g	g
i	c	u
o	r	s
p	l	t
[	/	.
]	=	,
a	a	l
s	o	o
d	e	e
f	u	m
g	i	p
h	d	d
j	h	c
k	t	n
l	n	v
;	s	q
'	-	;
z	;	[
x	q	]
c	j	y
v	k	z
b	x	h
n	b	w
m	m	f
,	w	x
.	v	'
/	z	~
""".strip()

m = {
    "qwerty": [row.split("\t")[0] for row in table.split("\n")[1:]],
    "dvorak": [row.split("\t")[1] for row in table.split("\n")[1:]],
    "bjarki": [row.split("\t")[2] for row in table.split("\n")[1:]],
}
k, _, v = input().split()
mapping = dict(zip(m[k], m[v]))

s = input()
print("".join(mapping.get(c, c) for c in s))
