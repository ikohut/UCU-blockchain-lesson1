import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYSeries;
import org.knowm.xchart.style.markers.SeriesMarkers;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by Victor on 02.10.2018.
 */
public class PlotDrawer {

    private List<Point> dots;
    private List<Point> results;


    public PlotDrawer() {
        dots = new ArrayList<>();
        results = new ArrayList<>();
    }



    public void  addDot(Point dot){
        dots.add(dot);
        dots.add(new Point(dot.getX(), -dot.getY()));
    }
    public void  addResDot(Point resulDot){
        results.add(resulDot);

    }

    public void showPlot(){



        List<Double> x = new ArrayList<>();
        List<Double> y = new ArrayList<>();
        List<Double> x_res = new ArrayList<>();
        List<Double> y_res = new ArrayList<>();


        for (Point p:
             dots) {
            x.add(p.getX());
            y.add(p.getY());
        }

        for (Point p:
             results) {
            x_res.add(p.getX());
            y_res.add(p.getY());
        }



        org.knowm.xchart.XYChart chart = QuickChart.getChart("Sample Chart", "X", "Y", "y(x)", x, y);
        chart.getStyler().setDefaultSeriesRenderStyle(XYSeries.XYSeriesRenderStyle.Scatter);
        chart.getStyler().setChartTitleVisible(false);
        chart.getStyler().setMarkerSize(5);
        chart.addSeries("dots", x, y);

        XYSeries series = chart.addSeries("result", x_res, y_res);
        series.setMarker(SeriesMarkers.DIAMOND);

// Show it

        new SwingWrapper<>(chart).displayChart();
    }

}
