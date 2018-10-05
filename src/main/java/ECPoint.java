import exceptions.ConstraintsViolationException;

import java.math.BigInteger;

/**
 * Point on the curve y^2 = x^3 + ax + b.
 *
 * This class is mutable,
 * addition performed on a particular instance
 * will modify its state.
 */

public class ECPoint {

    private static final BigInteger PRIME = BigInteger.valueOf(37);

    private ECCurve curve;

    private BigInteger x;
    private BigInteger y;

    public ECPoint(ECCurve curve, BigInteger x, BigInteger y) throws ConstraintsViolationException {
        if (!belongsToCurve(curve, x, y)) {
            throw new ConstraintsViolationException("Provided point does not belong to the curve");
        }
        this.curve = curve;
        this.x = x;
        this.y = y;
    }

    /**
     * Modifies the instance called upon.
     * Sets the coordinates to the result of addition
     * of the existing and provided ECPoint as an argument.
     *
     * @param otherPoint: another ECPoint to be added to this one.
     */
    public void add(ECPoint otherPoint) {
        BigInteger slope;
        if(x.equals(otherPoint.getX()) && y.equals(otherPoint.getY())) {
            BigInteger numerator = BigInteger.valueOf(3).multiply(x.pow(2)).add(curve.getA());
            BigInteger denominator = BigInteger.valueOf(2).multiply(y);
            slope = (numerator.divide(denominator.modInverse(PRIME))).mod(PRIME);
        } else {
            BigInteger numerator = otherPoint.getY().subtract(y);
            BigInteger denominator = otherPoint.getX().subtract(x);
            slope = (numerator.divide(denominator.modInverse(PRIME))).mod(PRIME);
        }
        BigInteger newX = (slope.pow(2).subtract(x).subtract(otherPoint.getX())).mod(PRIME);
        BigInteger newY = (slope.multiply(newX.subtract(x)).add(y)).mod(PRIME);
        this.x = newX;
        this.y = newY;
    }

    /**
     * y^2 == x^3 + ax + b
     *
     * @return true if the point with (x,y) coordinates belong to the curve,
     * false otherwise
     */
    private boolean belongsToCurve(ECCurve curve, BigInteger x, BigInteger y) {
        BigInteger ySquared = y.pow(2);
        BigInteger xCube = x.pow(3);
        BigInteger aX = curve.getA().multiply(x);
        BigInteger b = curve.getB();
        return ySquared.mod(PRIME).equals((xCube.add(aX).add(b)).mod(PRIME));
    }

    public ECCurve getCurve() {
        return curve;
    }

    public BigInteger getX() {
        return x;
    }

    public BigInteger getY() {
        return y;
    }
}
