import exceptions.ConstraintsViolationException;
import org.junit.Test;

import java.math.BigInteger;

public class ECPointTest {

    @Test
    public void validPointOnCurveTest() throws ConstraintsViolationException {
        // y^2 == x^3 - 4x + 0
        ECCurve curve = new ECCurve(BigInteger.valueOf(-4), BigInteger.valueOf(0));
        // Point belongs to the curve
        new ECPoint(curve, BigInteger.valueOf(2), BigInteger.valueOf(0));
    }

    @Test(expected = ConstraintsViolationException.class)
    public void invalidPointOnCurveTest() throws ConstraintsViolationException {
        // y^2 == x^3 - 4x + 0
        ECCurve curve = new ECCurve(BigInteger.valueOf(-4), BigInteger.valueOf(0));
        // Point doesn't belong to the curve and won't be initialized.
        // Expect ConstraintsViolationException to be thrown.
        new ECPoint(curve, BigInteger.valueOf(6), BigInteger.valueOf(3));
    }

}
