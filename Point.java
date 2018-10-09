/**
 * Created by cs.ucu.edu.ua on 30.09.2018.
 */

import java.lang.Math;

public class Point {
    public double y;
    public double x;

    public Point(double x, double y) {
        //point on elliptic curve y^2 = x^3 + ax + b
        this.y = y;
        this.x = x;
    }

    public void add(Point other) {
        //should modify the self instance
        double s;
        if (other.x - this.x != 0) { //if point are not equal
            //s=(y2−y1)/(x2−x1)
            s = (other.y - this.y) / (other.x - this.x);
            //x3=s^2−x1−x2
            double x3 = Math.pow(s, 2) - this.x - other.x;
            //y3=y1+s(x3−x1)
            double y3 = this.y + s * (x3 - this.x);
            //modify the self
            this.x = x3;
            this.y = y3;
        } else {
            System.out.print("Points are equal, you should use addEqualPoints method!");
        }
    }

    public void addEqualPoints(Point other, double a) {
        // need a coefficient from elliptic curve y^2 = x^3 + ax + b
        // s=(3x1^2+a)/2y1
        double s = (3 * Math.pow(this.x, 2) + a) / (2 * this.y);
        //x3=s^2−x1−x2
        double x3 = Math.pow(s, 2) - this.x - other.x;
        //y3=y1+s(x3−x1)
        double y3 = this.y + s * (x3 - this.x);
        //modify the self
        this.x = x3;
        this.y = y3;
    }
}
