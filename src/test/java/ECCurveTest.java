import exceptions.ConstraintsViolationException;
import org.junit.Test;

import java.math.BigInteger;

public class ECCurveTest {

    @Test
    public void validArgsInitializationTest() throws ConstraintsViolationException {
        // valid ECCurve y^2 == x^3 - 4x + 0
        new ECCurve(BigInteger.valueOf(-4), BigInteger.valueOf(0));
    }

    @Test(expected = ConstraintsViolationException.class)
    public void invalidArgsInitializationTest() throws ConstraintsViolationException {
        // y^2 == x^3 + 0x + 0
        // discriminant is zero, constrains are violated, expect exception to be thrown
        new ECCurve(BigInteger.valueOf(0), BigInteger.valueOf(0));
    }

}
