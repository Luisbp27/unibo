package ADS.Algorithms.src;

public class HeapSort {

    private static int l(int n) {
        return 2 * n + 1;
    }

    private static int r(int n) {
        return 2 * n + 2;
    }

    /**
     * Sorts an array of integers using the heap sort algorithm.
     *
     * @param a
     * @param i
     * @param dim
     */
    private static void maxHeapRestore(int[] a, int i, int dim) {
        int l = l(i);
        int r = r(i);
        int max = i;
        if (l < dim && a[l] > a[max]) {
            max = l;
        }
        if (r < dim && a[r] > a[max]) {
            max = r;
        }
        if (max != i) {
            int tmp = a[i];
            a[i] = a[max];
            a[max] = tmp;
            maxHeapRestore(a, max, dim);
        }
    }

    private static void headBuild(int[] a, int n) {
        for (int i = n / 2 - 1; i >= 0; i--) {
            maxHeapRestore(a, i, n);
        }
    }

    public static void heapSort(int[] a) {
        int n = a.length;
        headBuild(a, n);
        for (int i = n - 1; i > 0; i--) {
            int tmp = a[0];
            a[0] = a[i];
            a[i] = tmp;
            maxHeapRestore(a, 0, i);
        }
    }

    public static void sort(int[] a) {
        for (int i = 0; i < a.length; i++) {
            int minIndex = a[i];
            for (int j = i + 1; j < a.length; j++) {
                if (a[j] < a[minIndex]) {
                    minIndex = j;
                }
            }

            if (minIndex != i) {
                int tmp = a[i];
                a[i] = a[minIndex];
                a[minIndex] = tmp;
            }
        }
    }

    public static void print(int[] a) {
        for (int i : a) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String args[]) {
        final int SIZE = 100;
        int[] a = new int[SIZE];
        int[] b = new int[SIZE];

        for (int i = 0; i < SIZE; i++) {
            a[i] = (int) (Math.random() * 1000);
            b[i] = a[i];
        }

        print(a);
        long start = System.currentTimeMillis();
        heapSort(a);
        long end = System.currentTimeMillis() - start;
        System.out.println("End: " + end + "ms");
        print(a);

        print(b);
        long start1 = System.currentTimeMillis();
        heapSort(b);
        long end2 = System.currentTimeMillis() - start1;
        System.out.println("End2: " + end2 + "ms");
        print(b);
    }
}