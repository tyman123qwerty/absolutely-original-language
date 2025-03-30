from .interpreter import run_code

def c(s):
    x = ''
    for i in range(len(s)):
        if s[i] == '.':
            x += 'dotdotdotd'
        if s[i] == ',':
            x += 'commacomma'
        if s[i] == '+':
            x += 'pluspluspl'
        if s[i] == '-':
            x += 'minusminus'
        if s[i] == '[':
            x += 'startstart'
        if s[i] == ']':
            x += 'endendende'
        if s[i] == 'm':
            i += 1
            x += 'nummultby' + s[i]
        if s[i] == '>':
            x += 'rightright'
        if s[i] == '<':
            x += 'leftleftle'

def test_output():
    res = run_code(c("."))

    assert res == chr(0)

def test_increament_and_output():
    res = run_code(c("+."))

    assert res == chr(1)

def test_decreament_and_output():
    res = run_code(c("-."))

    assert res == chr(255)

def test_input_and_output():
    res = run_code(c(",."), chr(10))

    assert res == chr(10)

def test_go_right_and_output():
    res = run_code(c("+>."))

    assert res == chr(0)

def test_go_left_and_output():
    res = run_code(c("+<."))

    assert res == chr(0)

def test_multiple_output():
    res = run_code(c('..'))

    assert res == chr(0) + chr(0)

def test_start_and_end_cycle():
    res = run_code(c('++[>++<-]>.')) # ++[>++<-]>.

    assert res == chr(4)


def test_multiple_cycles():
    #               +         +         [         >         +         +         [         >         +         +         <         -        ]          <         -         ]         >         >         .
    res = run_code(c("++[>++[>++<-]<-]>>.")) # ++[>++[>++<-]<-]>>.

    assert res == chr(8)

def test_mult_by_smth():
    res = run_code(c("+.m2.m0."))

    assert  res == chr(1) + chr(2) + chr(0)