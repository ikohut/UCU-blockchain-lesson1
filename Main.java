import java.math.BigInteger;

/**
 * Created by cs.ucu.edu.ua on 30.09.2018.
 */
public class Main {
    public static void main(String args[]){
        Point point = new Point(2.78, 4.616);
        Point other = new Point(1.57, 2.214);
        point.add(other);
        //result should be x= -0.409, y = -1.715
//        System.out.print(point.x);
//        System.out.print(point.y);

        try{
            EllipticCurvePoint elPoint = new EllipticCurvePoint(new BigInteger("3"), new BigInteger("7"));
            EllipticCurvePoint otherPoint = new EllipticCurvePoint(new BigInteger("-1"), new BigInteger("-1"));
            elPoint.add(otherPoint);
            System.out.print("x: " + elPoint.x + "\n");//2
            System.out.print("y: " + elPoint.y);//12
        }catch (Exception e){
            System.out.print(e);
        }
    }
}
