# input(): ユーザーの入力した値(文字列)を取得

age = int(input("何歳ですか？"))
limit_age = 18
game_txt = """どのゲーム？
1.pk
2.bj
3.r
"""
if age >= limit_age:
    print("ok")
    game = (input(game_txt))
    if game == '1':
        print('pk')
    elif game == '2':
        print('pk')
    elif game == '3':
        print('pk')
    else:
        print('ban')
else:
    print(f"no under {limit_age}")