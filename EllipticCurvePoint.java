/**
 * Created by cs.ucu.edu.ua on 08.10.2018.
 */
import java.math.*;
import java.lang.Math;
public class EllipticCurvePoint {
    public BigInteger y;
    public BigInteger x;
    public BigInteger p = new BigInteger("17");//prime number
    public BigInteger a = new BigInteger("5");
    public BigInteger b = new BigInteger("7");

    public EllipticCurvePoint(BigInteger x, BigInteger y) {
        //point on elliptic curve y^2 = x^3 + ax + b
        this.y = y;
        this.x = x;
    }

    private boolean isPointOnSameCurve(EllipticCurvePoint point){
       BigInteger left =  point.y.pow(2).mod(this.p);
        BigInteger right = point.x.pow(3).add(this.a.multiply(point.x)).add(this.b).mod(this.p);
        return left.equals(right);
    }

    private BigInteger getSlope(BigInteger numerator, BigInteger denominator){
       BigInteger den = denominator.modInverse(this.p);
       BigInteger sl = numerator.divide(denominator);
        return sl.mod(this.p);
    }

    public void add(EllipticCurvePoint other) throws Exception{
        if (!isPointOnSameCurve(other)){
            throw new Exception("Points are not on same elliptic curve");
        }
        BigInteger numerator;
        BigInteger denominator;
        BigInteger slope;
        if (this.equals(other)){
            numerator = this.x.pow(2).multiply(new BigInteger("3")).add(this.a);
            denominator = this.y.multiply(new BigInteger("2"));
            slope = getSlope(numerator, denominator);
        }else{
            numerator = other.y.subtract(this.y);
            denominator = other.x.subtract(this.x);
            slope = getSlope(numerator, denominator);
        }
        BigInteger x3 = (slope.pow(2).subtract(this.x).subtract(other.x)).mod(this.p);
        BigInteger y3 = (slope.multiply(this.x.subtract(x3)).subtract(this.y)).mod(this.p);
        this.x = x3;
        this.y = y3;
    }


}
