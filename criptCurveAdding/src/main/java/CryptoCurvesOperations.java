import java.math.BigDecimal;

/**
 * Created by Victor on 02.10.2018.
 */
public class CryptoCurvesOperations {

    private static double a;
    private static double b;
    private static  boolean inited;

    static {
        inited = false;
    }
    public static  void init(double paramA, double paramB){
        a = paramA;
        b = paramB;
        System.out.println("Your crypto curve is: y^2 = x^3 + "+a+"x"+" + " + b);
        inited = true;
    }

    public  static  Point add(Point first, Point second){
        if(!inited){
            throw  new RuntimeException("You must init criptoCurve with your a , b params.\n Call \"init\" method");
        }

        if(!validatePoint(first) || !validatePoint(second)){
            throw  new RuntimeException("One of your point`s or both isn`t on curve : "+ "y^2 = x^3 + "+a+"x"+" + " + b);
        }

        double slope;
        if(first.equals(second)){
            slope = (3*Math.pow(first.getX(), 2) + a)/(2*first.getY());
        }else {
            slope = (second.getY() - first.getY())/(second.getX() - first.getX());
        }
        double x;
        double y;

        x = Math.pow(slope, 2) - (first.getX() + second.getX());
        y = -1*(second.getY() + slope*(x - second.getX()));
        return  new Point(x, y);
    }

    private static boolean validatePoint(Point point){



        BigDecimal ysqr = new BigDecimal(Math.pow(point.getY(), 2)).setScale(6, BigDecimal.ROUND_HALF_DOWN);
        BigDecimal funct = new BigDecimal(Math.pow(point.getX(), 3) + point.getX()*a + b).setScale(6, BigDecimal.ROUND_HALF_DOWN);
        System.out.println(ysqr + " " + funct);
        if(!ysqr.abs().equals(funct.abs())){
            return  false;
        }
        return true;
    }

    public static Point getValidPoint(){
        if(!inited){
            throw  new RuntimeException("You must init criptoCurve with your a , b params.\n Call \"init\" method");
        }

        double x = (Math.random()*100);
        if(Math.random() < 0.5){
            x = -x;
        }
        double res = Math.pow(x, 3) + x*a + b;
        if(res < 0){
            return null;
        }
        double y = Math.sqrt(res);

        return new Point(x, y);
    }
}
