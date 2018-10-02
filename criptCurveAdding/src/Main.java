import java.nio.channels.Pipe;

/**
 * Created by Victor on 02.10.2018.
 */
public class Main {

    public static void main(String[] args) {

        Point pointOne;
        Point pointTwo;
        CryptoCurvesOperations.init(3, 7);
        pointOne = CryptoCurvesOperations.getValidPoint();
        pointTwo = CryptoCurvesOperations.getValidPoint();
        Point res = CryptoCurvesOperations.add(pointOne, pointTwo);
        System.out.println(res);

    }
}
