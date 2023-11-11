a=float(input())
if a==130:
    print("jackhammer")
elif a==106:
    print("Gas lawnmower")
elif a==70:
    print("alarm clock")
elif a==40:
    print("quiet room")
elif a>130:
    print("so noise")
elif a<40:
    print("so quiet")
elif (106<a<130):
    print("between the noises jackhammer and gas lawnmower")
elif (70<a<106):
    print("between the noises gas lawnmower and alarm clock")
elif (40<a<70):
    print("between the noises alarm clock and quiet room")