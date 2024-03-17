import matplotlib.pyplot as plt
import io
from meteoch.config import PRODUCTS


def coldwave_graph(x, y1, y2, y3, title):
    #print(x, y1, y2, y3)

    # define size of graph
    plt.figure(figsize=(PRODUCTS['coldwave']['figsize_width'], PRODUCTS['coldwave']['figsize_height']))

    # define title
    plt.title(label=title,
              loc='center',
              pad=5,
              fontsize=20,
              )
    # define colors
    colors = PRODUCTS['coldwave']['colors']
    # define labels
    threshold0 = PRODUCTS['coldwave']['thresholds'][0]
    threshold1 = PRODUCTS['coldwave']['thresholds'][1]
    threshold2 = PRODUCTS['coldwave']['thresholds'][2]

    labels = [f"Tmin < {threshold0} °C", f"Tmin < {threshold1} °C", f"Tmin < {threshold2} °C"]
    # plot legend
    handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
    plt.legend(handles, labels)
    # plot bars in stack manner
    plt.bar(x, y3, bottom=0, color=colors[2])
    plt.bar(x, y2, bottom=0, color=colors[1])
    plt.bar(x, y1, bottom=0, color=colors[0])
    plt.xticks(rotation=45)
    plt.tight_layout()
    with io.BytesIO() as buffer:
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image = buffer.getvalue()
    #plt.show()
    return image

def diffdruck_graph(quantiles):
    # extract x
    x = quantiles.get['time']
    # plot
    fig, ax = plt.subplots()

    ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
    ax.plot(x, (y1 + y2)/2, linewidth=2)