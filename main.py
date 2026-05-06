from giftball import GiftBall


def demo():
    g = GiftBall(initial_balls=2)
    print(g)
    print('Insert token ->', g.insert_token())
    print(g)
    print('Turn crank ->', g.turn_crank())
    print(g)
    print('Insert token ->', g.insert_token())
    print('Eject token ->', g.eject_token())
    print(g)
    print('Refill 3 ->', g.refill(3))
    print(g)


if __name__ == '__main__':
    demo()
