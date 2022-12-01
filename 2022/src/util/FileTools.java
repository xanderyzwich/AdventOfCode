package util;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class FileTools {

    public static List<String> readLinesFromFile(Integer day, String fileName){
        List<String> lines = new LinkedList<>();
        try {
            String path = String.format("data/day%s-%s.txt", day, fileName);
            File myFile = new File(path);
            Scanner fileScanner = new Scanner(myFile);
            while(fileScanner.hasNextLine()){
                lines.add(fileScanner.nextLine());
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        return lines;
    }
}
