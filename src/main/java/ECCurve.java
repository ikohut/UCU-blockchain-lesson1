import exceptions.ConstraintsViolationException;

import java.math.BigInteger;

public class ECCurve {

    private final BigInteger a;
    private final BigInteger b;

    public ECCurve(BigInteger a, BigInteger b) throws ConstraintsViolationException {
        BigInteger discriminant = getDiscriminant(a, b);
        if(discriminant.equals(BigInteger.ZERO)) {
            throw new ConstraintsViolationException("Discriminant is zero. Provided arguments violate constraints.");
        }

        this.a = a;
        this.b = b;
    }

    public BigInteger getA() {
        return a;
    }

    public BigInteger getB() {
        return b;
    }

    private BigInteger getDiscriminant(BigInteger a, BigInteger b) {
        BigInteger sum = BigInteger.valueOf(4).multiply(a.pow(3))
                        .add(BigInteger.valueOf(27).multiply(b.pow(2)));
        return BigInteger.valueOf(-16).multiply(sum);
    }

}
