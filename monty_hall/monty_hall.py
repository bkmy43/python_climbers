import random

__author__ = "Ilya Vladimirskiy"
__email__ = "bkmy43@googlemail.com"


NUMBER_OR_TRIES = 10000
NUMBER_OF_BOXES = 3

# def new_try():
#     return True

def main():
    total_changed_count = total_unchanged_count = 0
    changed_success_count = unchanged_success_count = 0
    boxes = [True] + [False] * (NUMBER_OF_BOXES - 1)

    for i in range(NUMBER_OR_TRIES):
        random.shuffle(boxes)
        strategy = random.choice(('CHANGED  ', 'UNCHANGED'))
        guess1 = random.choice(range(NUMBER_OF_BOXES))
        guess2 = guess1
        success = False

        if strategy == 'CHANGED  ':
            total_changed_count += 1

            for j in range(len(boxes)):
                if j != guess1 and boxes[j] is False:
                    empty_box = j
                    break

            guess2 = guess1
            while guess2 == guess1 or guess2 == empty_box:
                guess2 = random.choice(range(NUMBER_OF_BOXES))

            if boxes[guess2]:
                success = True
                changed_success_count += 1
            else:
                success = False

        else:
            total_unchanged_count +=1
            if boxes[guess2] is True:
                success = True
                unchanged_success_count += 1
            else:
                success = False

        print("Try {}: Boxes {}, Strategy {}\t\t guesses: {}, {}\t\t {}".format(i, boxes, strategy, guess1, guess2, success))


    print("---------------------------------------------------------------------------------------------\n" \
            "\t{} tests done\n\tCHANGED {}/{} success {}%\n\tUNCHANGED {}/{} success {}%".format(
            i + 1, changed_success_count, total_changed_count, round(100*changed_success_count/total_changed_count),
            unchanged_success_count, total_unchanged_count, round(100*unchanged_success_count/total_unchanged_count)))

if __name__ == "__main__":
    main()