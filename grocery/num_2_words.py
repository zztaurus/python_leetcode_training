
import inflect

def main(number):
    p = inflect.engine()
    return p.number_to_words(number)


if __name__ == "__main__":
    print(main(2))
