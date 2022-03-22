import transbigdata as tbd
import matplotlib.pyplot as plt


class TestPlotmap:
    def setup_method(self):
        pass

    def test_plot_map(self):
        bounds = [113.6, 22.4, 114.8, 22.9]
        fig = plt.figure(1, (8, 8), dpi=250)
        ax = plt.subplot(111)
        tbd.plotscale(ax, bounds=bounds, textsize=10, compasssize=1,
                      accuracy=2000, rect=[0.06, 0.03], zorder=10)
