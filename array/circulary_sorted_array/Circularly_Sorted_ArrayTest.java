/*
 * Tests for Circularly_Sorted_Array.java
 *
 * Compile & run (JUnit 5):
 *   javac -cp .:junit-platform-console-standalone.jar Circularly_Sorted_Array.java Circularly_Sorted_ArrayTest.java
 *   java  -cp .:junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --select-class=Circularly_Sorted_ArrayTest
 *
 */

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Circularly_Sorted_ArrayTest {

    @Test
    void testExampleFromMain() {
        // {15,22,23,28,31,38,5,6,8,10,12} — rotated 6 times
        int[] A = {15, 22, 23, 28, 31, 38, 5, 6, 8, 10, 12};
        assertEquals(6, Circularly_Sorted_Array.findRotationCount(A, 11));
    }

    @Test
    void testNotRotated() {
        // Already sorted — rotation count is 0
        int[] A = {1, 2, 3, 4, 5};
        assertEquals(0, Circularly_Sorted_Array.findRotationCount(A, 5));
    }

    @Test
    void testRotatedByLast() {
        // {2,3,4,5,1} — rotated 4 times (min is at index 4)
        int[] A = {2, 3, 4, 5, 1};
        assertEquals(4, Circularly_Sorted_Array.findRotationCount(A, 5));
    }

    @Test
    void testRotatedByHalf() {
        // {3,4,5,1,2} — rotated 3 times
        int[] A = {3, 4, 5, 1, 2};
        assertEquals(3, Circularly_Sorted_Array.findRotationCount(A, 5));
    }

    @Test
    void testSingleElement() {
        int[] A = {42};
        assertEquals(0, Circularly_Sorted_Array.findRotationCount(A, 1));
    }

    @Test
    void testTwoElementsRotatedOnce() {
        int[] A = {2, 1};
        assertEquals(1, Circularly_Sorted_Array.findRotationCount(A, 2));
    }

    @Test
    void testRotatedOnce() {
        // {5,1,2,3,4} — rotated 1 time, min at index 1
        int[] A = {5, 1, 2, 3, 4};
        assertEquals(1, Circularly_Sorted_Array.findRotationCount(A, 5));
    }
}
