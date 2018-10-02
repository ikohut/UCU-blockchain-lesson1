import javafx.scene.chart.XYChart;
import javafx.util.Pair;
import org.knowm.xchart.QuickChart;
import org.knowm.xchart.SwingWrapper;
import org.knowm.xchart.XYChartBuilder;
import org.knowm.xchart.XYSeries;
import org.knowm.xchart.style.Styler;
import org.knowm.xchart.style.markers.SeriesMarkers;

import java.nio.channels.Pipe;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Victor on 02.10.2018.
 */
public class Main {

    public static void main(String[] args) {
        Point pointOne = null;
        Point pointTwo;
        CryptoCurvesOperations.init(1000, 5);
        PlotDrawer plotDrawer = new PlotDrawer();
        for(int i = 0; i< 100; i++){
            do {
                pointOne = CryptoCurvesOperations.getValidPoint();
           }while (pointOne == null);
            do {
                pointTwo = CryptoCurvesOperations.getValidPoint();
            }while (pointTwo == null);
            Point res = CryptoCurvesOperations.add(pointOne, pointTwo);
            plotDrawer.addDot(pointOne);
            plotDrawer.addDot(pointTwo);
            plotDrawer.addResDot(res);
        }
        plotDrawer.showPlot();
    }
}
