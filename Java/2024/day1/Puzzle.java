
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.regex.Pattern;
import java.util.stream.IntStream;

public class Puzzle {
    private final List<Integer> leftList = new ArrayList<>();
    private final List<Integer> rightList = new ArrayList<>();

    public void readFile(String filePath) {
        try {
            Pattern pattern = Pattern.compile("(\\d+)\\s+(\\d+)");
            Files.lines(Path.of(filePath))
                    .map(pattern::matcher)
                    .filter(matcher -> matcher.matches())
                    .forEach(matcher -> {
                        leftList.add(Integer.parseInt(matcher.group(1)));
                        rightList.add(Integer.parseInt(matcher.group(2)));
                    });
        } catch (Exception e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }

    public int computeTotalDistance() {
        var sortedLeft = leftList.stream().sorted().toList();
        var sortedRight = rightList.stream().sorted().toList();
        return IntStream.range(0, sortedLeft.size())
                .map(i -> Math.abs(sortedLeft.get(i) - sortedRight.get(i)))
                .sum();
    }

    public int computeSimilarityScore() {
        return leftList.stream()
                .mapToInt(n -> n * Collections.frequency(rightList, n))
                .sum();
    }

    public static void main(String[] args) {
        var puzzle = new Puzzle();
        puzzle.readFile("input.txt");
        System.out.println("Total distance (sorted): " + puzzle.computeTotalDistance());
        System.out.println("Similarity score: " + puzzle.computeSimilarityScore());
    }
}
