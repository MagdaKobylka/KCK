import matplotlib.pyplot as plt


def readfile(file):
    points = []
    results = []
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines[1:]):
            split = line.split(',')
            for element in split[2:]:
                results.append(float(element))
            points.append([int(split[1]), (sum(results)/len(results))])
            results.clear()
    return points


def main():
    plt.figure(figsize=(12, 8))
    plt.xlabel('Rozegranych gier', fontsize=16)
    plt.ylabel('Odsetek wygranych gier', fontsize=16)
    plt.gca().margins(tight=True, y=.05)

    points = readfile('cel.csv')
    plt.plot(*zip(*points), label='cel.csv')
    points = readfile('2cel.csv')
    plt.plot(*zip(*points), label='2cel.csv')
    points = readfile('2cel-rs.csv')
    plt.plot(*zip(*points), label='2cel-rs.csvv')
    points = readfile('cel-rs.csv')
    plt.plot(*zip(*points), label='cel-rs.csv')
    points = readfile('rsel.csv')
    plt.plot(*zip(*points), label='rsel.csv')

    plt.legend(loc=4)
    plt.savefig('myplot.pdf')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
