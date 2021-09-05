def solution(files):
    answer = []
    compare = []
    index = 1
    for file in files:
        print(compare)
        head = ""
        number = ""
        tail = ""
        what = 0
        for i in file:
            if what == 0:
                if i.isdigit():
                    what = 1
                else:
                    head += i
            if what == 1:
                if len(number) <= 5 and i.isdigit():
                    number += i
                elif len(number) > 5 or i.isdigit() == False:
                    what = 2
            if what == 2:
                tail += i
        compare.append((head.lower(), int(number), tail, index, file))
        index += 1
    answer = sorted(compare, key=lambda x: (x[0], x[1], x[3]))
    real = []
    for e in answer:
        real.append(e[4])

    return real

# finish


print(solution(["img12.png", "img10.png", "img02.png",
      "img1.png", "IMG01.GIF", "img2.JPG"]))
