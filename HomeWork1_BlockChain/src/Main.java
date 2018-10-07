public class Main {
    private static double f(double x){
        double a = 3;
        double bb = 7;
        return Math.pow(x, 3) -a*x + bb;
    }

    private static Point add(Point p, Point q){
        double k = (q.getY() - p.getY())/(q.getX() - p.getX());

        return new Point(Math.pow(k,2) - q.getX() - p.getX(), q.getY() + k * (Math.pow(k,2) - q.getX() - p.getX() - q.getX()));

    }


    public static void main(String[] args) {

        Point p = new Point(-2, Math.sqrt(f(-2)));
        Point q = new Point(-0.5, Math.sqrt(f(-0.5)));

        Point r = add(p, q);
        System.out.println("X: " + r.getX());
        System.out.println("Y: " + r.getY());
    }
}
