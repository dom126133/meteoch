import matplotlib.pyplot as plt
import io

def coldwave_graph(x, y1, y2, y3):
    #print(x, y1, y2, y3)

    # define size of graph
    plt.figure(figsize=(12, 10))

    # define title
    plt.title(label='Prévision pour Genève : Température minimale',
              loc='center',
              pad=5,
              fontsize=20,
              )
    # define colors
    # bleu foncé, bleu moyen, bleu clair
    colors = ['#1605fc','#0579fc','#05c2fc']
    # define labels
    labels = ["Tmin < -5 °C", "Tmin < 0 °C", "Tmin < 5 °C"]
    # plot legend
    handles = [plt.Rectangle((0,0),1,1, color=color) for color in colors]
    plt.legend(handles, labels)
    # plot bars in stack manner
    plt.bar(x, y3, bottom=0, color=colors[2])
    plt.bar(x, y2, bottom=0, color=colors[1])
    plt.bar(x, y1, bottom=0, color=colors[0])
    plt.xticks(rotation=45)
    with io.BytesIO() as buffer:
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image = buffer.getvalue()
    #plt.show()
    return image
