/*
 * Tests for MissingNumberInArray.java
 *
 * Compile & run (JUnit 5):
 *   javac -cp .:junit-platform-console-standalone.jar MissingNumberInArray.java MissingNumberInArrayTest.java
 *   java  -cp .:junit-platform-console-standalone.jar org.junit.platform.console.ConsoleLauncher --select-class=MissingNumberInArrayTest
 *
 * NOTE: getMissingNumber() is private, so reflection is used to access it.
 */

import org.junit.jupiter.api.Test;
import java.lang.reflect.Method;
import static org.junit.jupiter.api.Assertions.*;

public class MissingNumberInArrayTest {

    private int getMissingNumber(int[] numbers, int totalCount) throws Exception {
        Method method = MissingNumberInArray.class.getDeclaredMethod(
            "getMissingNumber", int[].class, int.class);
        method.setAccessible(true);
        return (int) method.invoke(null, numbers, totalCount);
    }

    @Test
    void testExampleFromMain() throws Exception {
        // From main: int[] iArray = {1, 2, 3, 5}; missing = getMissingNumber(iArray, 5)
        assertEquals(4, getMissingNumber(new int[]{1, 2, 3, 5}, 5));
    }

    @Test
    void testMissingLastNumber_oddTotal() throws Exception {
        assertEquals(5, getMissingNumber(new int[]{1, 2, 3, 4}, 5));
    }

    @Test
    void testMissingFirstNumber_oddTotal() throws Exception {
        assertEquals(1, getMissingNumber(new int[]{2, 3, 4, 5}, 5));
    }

    @Test
    void testNoMissingNumber() throws Exception {
        assertEquals(0, getMissingNumber(new int[]{1, 2, 3, 4, 5}, 5));
    }

    @Test
    void testMissingMiddleNumber_evenTotal() throws Exception {
        assertEquals(5, getMissingNumber(new int[]{1, 2, 3, 4, 6}, 6));
    }

    @Test
    void testMissingNumber_oddTotal_9() throws Exception {
        assertEquals(7, getMissingNumber(new int[]{1, 2, 3, 4, 5, 6, 8, 9}, 9));
    }
}
