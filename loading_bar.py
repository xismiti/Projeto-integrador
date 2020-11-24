import progressbar


def loading(title: str):
    widgets = {f'Something: ${title}', progressbar.Bar(marker=progressbar.RotatingMarker())}
    bar = progressbar.ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        bar.update(10 * i + 1)
        bar.finish()
    print(loading(title="fades"))