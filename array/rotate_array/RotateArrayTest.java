/*
 * Tests for the rotation logic in RotateArray.java
 *
 * Compile & run (JUnit 5):
 *   javac -cp .:junit-platform-console-standalone.jar RotateArrayTest.java
 *   java  -cp .:junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --select-class=RotateArrayTest
 *
 * The rotation logic is extracted here because RotateArray.main() uses Scanner (stdin).
 */

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class RotateArrayTest {

    /** Extracted from RotateArray.main() — rotate array right by `order` positions. */
    private static int[] rotate(int[] array_num, int order) {
        int array_length = array_num.length;
        order = order % array_length;
        int[] results = new int[array_length];
        int k = 0;
        for (int i = array_length, j = 0; j < array_length; j++, i--) {
            if (j < order) {
                results[order - j - 1] = array_num[i - 1];
            }
            if (j >= order) {
                results[j] = array_num[k];
                k++;
            }
        }
        return results;
    }

    @Test
    void testRotateByTwo() {
        assertArrayEquals(new int[]{4, 5, 1, 2, 3}, rotate(new int[]{1, 2, 3, 4, 5}, 2));
    }

    @Test
    void testRotateByOne() {
        assertArrayEquals(new int[]{5, 1, 2, 3, 4}, rotate(new int[]{1, 2, 3, 4, 5}, 1));
    }

    @Test
    void testRotateByThree() {
        assertArrayEquals(new int[]{3, 4, 5, 1, 2}, rotate(new int[]{1, 2, 3, 4, 5}, 3));
    }

    @Test
    void testRotateByZero() {
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, rotate(new int[]{1, 2, 3, 4, 5}, 0));
    }

    @Test
    void testRotateByFullLength() {
        // Rotating by the full length returns the same array
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, rotate(new int[]{1, 2, 3, 4, 5}, 5));
    }

    @Test
    void testSingleElement() {
        assertArrayEquals(new int[]{7}, rotate(new int[]{7}, 0));
    }

    @Test
    void testTwoElements() {
        assertArrayEquals(new int[]{2, 1}, rotate(new int[]{1, 2}, 1));
    }

    @Test
    void testOrderLargerThanLength() {
        // order=7 on length-5 array is equivalent to order=2
        assertArrayEquals(new int[]{4, 5, 1, 2, 3}, rotate(new int[]{1, 2, 3, 4, 5}, 7));
    }

    @Test
    void testOrderMultipleOfLength() {
        // order=10 on length-5 array is equivalent to order=0
        assertArrayEquals(new int[]{1, 2, 3, 4, 5}, rotate(new int[]{1, 2, 3, 4, 5}, 10));
    }
}
